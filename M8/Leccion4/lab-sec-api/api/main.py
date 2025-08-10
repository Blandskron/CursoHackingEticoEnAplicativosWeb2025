import os, time, uuid
from fastapi import FastAPI, Request, HTTPException, Depends
from fastapi.responses import JSONResponse
from jose import jwt, JWTError
from prometheus_fastapi_instrumentator import Instrumentator
from prometheus_client import Counter
from logstash_logger import build_logger

# ---- Config JWT (demo) ----
JWT_PUBLIC = os.getenv("JWT_PUBLIC", "changeme")
ALGO = "HS256"  # en real usa RS256 y valida firma con clave pública

# ---- Tracing (Jaeger) ----
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.exporter.jaeger.thrift import JaegerExporter
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor

JAEGER_HOST = os.getenv("JAEGER_AGENT_HOST", "jaeger")
JAEGER_PORT = int(os.getenv("JAEGER_AGENT_PORT", "6831"))

provider = TracerProvider()
jaeger = JaegerExporter(agent_host_name=JAEGER_HOST, agent_port=JAEGER_PORT)
provider.add_span_processor(BatchSpanProcessor(jaeger))
trace.set_tracer_provider(provider)

# ---- App & métricas ----
app = FastAPI(title="Secure API Demo")
FastAPIInstrumentor.instrument_app(app)
Instrumentator().instrument(app).expose(app)  # /metrics

AUTH_FAILED = Counter("auth_failed_total", "Intentos de autenticación fallidos")

log = build_logger()

def _cid(h: str | None = None) -> str:
    return h if h else str(uuid.uuid4())

async def auth_guard(request: Request):
    auth = request.headers.get("authorization", "")
    if not auth.startswith("Bearer "):
        AUTH_FAILED.inc()
        raise HTTPException(status_code=401, detail="Unauthorized")
    token = auth.split(" ", 1)[1]
    try:
        # En demo no verificamos firma; en real: options={"verify_signature": True}
        jwt.decode(token, JWT_PUBLIC, algorithms=[ALGO], options={"verify_signature": False})
        return {"sub": "demo-user"}
    except JWTError:
        AUTH_FAILED.inc()
        raise HTTPException(status_code=401, detail="Unauthorized")

@app.middleware("http")
async def observability_mw(request: Request, call_next):
    cid = _cid(request.headers.get("x-correlation-id"))
    start = time.time()
    try:
        resp = await call_next(request)
        log.info({
            "cid": cid, "path": request.url.path, "method": request.method,
            "status": resp.status_code, "latency_ms": round((time.time()-start)*1000,2)
        })
        resp.headers["X-Correlation-Id"] = cid
        return resp
    except Exception:
        log.error({
            "cid": cid, "path": request.url.path, "method": request.method,
            "error": "internal_error", "latency_ms": round((time.time()-start)*1000,2)
        })
        return JSONResponse(status_code=500, content={"message": "Internal server error", "cid": cid})

@app.get("/public/health")
def health():
    return {"ok": True}

@app.get("/private/data")
def private_data(user=Depends(auth_guard)):
    return {"message": "ok", "user": user}

@app.get("/private/admin")
def admin_only(user=Depends(auth_guard)):
    # autenticado pero sin permiso => 403
    raise HTTPException(status_code=403, detail="Forbidden")
