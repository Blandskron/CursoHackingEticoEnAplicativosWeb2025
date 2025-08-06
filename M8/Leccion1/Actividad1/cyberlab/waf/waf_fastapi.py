from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, Response
from fastapi.middleware.cors import CORSMiddleware
import httpx
import re
import logging

# === Configuración ===
BACKEND_URL = "http://backend:8000"
BLOCK_LIMIT = 100
LOG_LEVEL = logging.DEBUG

# === Logger ===
logging.basicConfig(level=LOG_LEVEL)
logger = logging.getLogger("WAF")

# === Inicializar FastAPI ===
app = FastAPI(
    title="WAF - Web Application Firewall",
    description="Firewall con detección de XSS, SQLi y fuerza bruta",
    version="1.0.0"
)

# === Middleware CORS ===
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# === Intentos por IP ===
ip_attempts = {}

# === Regex para ataques comunes (solo body y query) ===
WAF_PATTERN = re.compile(
    rb"(<script|</script>|javascript:|onerror=|onload=|eval\(|alert\(|--|/\*|\*/|union\s+select|drop\s+table|select\s+\*|insert\s+into)",
    re.IGNORECASE
)

@app.middleware("http")
async def waf_middleware(request: Request, call_next):
    client_ip = request.client.host or "unknown"
    method = request.method
    path = request.url.path

    # Liberar preflight CORS
    if method == "OPTIONS":
        logger.debug(f"🔓 CORS preflight liberado desde {client_ip}")
        return Response(
            status_code=204,
            headers={
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "*",
                "Access-Control-Allow-Headers": "*",
                "Access-Control-Allow-Credentials": "true",
            }
        )

    # Leer body y query
    body = await request.body()
    query = str(request.query_params).encode()
    combined = body + query  # ⛔️ No escaneamos los headers

    logger.debug(f"🔍 IP: {client_ip} - {method} {path}")

    # Reglas WAF (solo si el path no es Swagger)
    if path not in ["/docs", "/openapi.json", "/favicon.ico"] and WAF_PATTERN.search(combined):
        ip_attempts[client_ip] = ip_attempts.get(client_ip, 0) + 1
        logger.warning(f"🚫 Payload malicioso detectado desde {client_ip}")
        if ip_attempts[client_ip] >= BLOCK_LIMIT:
            return JSONResponse(status_code=403, content={"msg": f"WAF: IP {client_ip} bloqueada"})
        return JSONResponse(status_code=403, content={"msg": "WAF: patrón malicioso detectado"})

    # Control fuerza bruta en login
    if path == "/login" and method == "POST":
        ip_attempts[client_ip] = ip_attempts.get(client_ip, 0) + 1
        logger.info(f"🔑 Intento login #{ip_attempts[client_ip]} desde {client_ip}")
        if ip_attempts[client_ip] >= BLOCK_LIMIT:
            return JSONResponse(status_code=403, content={"msg": f"WAF: IP {client_ip} bloqueada por fuerza bruta"})

    # Proxy al backend
    try:
        headers = dict(request.headers)
        headers["X-Forwarded-For"] = client_ip

        async with httpx.AsyncClient() as client:
            backend_response = await client.request(
                method=method,
                url=f"{BACKEND_URL}{path}",
                content=body,
                headers=headers,
                params=request.query_params
            )
    except httpx.RequestError as e:
        logger.error(f"⚠️ Error al contactar backend: {str(e)}")
        return JSONResponse(status_code=502, content={"msg": "WAF: backend no responde"})

    return Response(
        content=backend_response.content,
        status_code=backend_response.status_code,
        headers={
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "*",
            "Access-Control-Allow-Headers": "*",
            "Access-Control-Allow-Credentials": "true",
            **dict(backend_response.headers),
        }
    )

@app.get("/", tags=["Estado"])
def root_status():
    return {
        "msg": "🛡️ WAF activo",
        "ips_bloqueadas": [ip for ip, v in ip_attempts.items() if v >= BLOCK_LIMIT],
        "intentos_por_ip": ip_attempts
    }
