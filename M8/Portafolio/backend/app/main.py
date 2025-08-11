from fastapi import FastAPI, Depends, HTTPException, Request, Response, status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from loguru import logger
from typing import List
import os
from .db import Base, engine, SessionLocal
from .models import Client
from .schemas import ClientIn, ClientOut
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI(title="API Vulnerable – Proyecto Final M8")

# CORS intencionalmente laxo para práctica (mitigar en la Parte 4)
origins = os.getenv("CORS_ALLOW_ORIGINS", "*").split(",")
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # inseguro si "*"
    allow_credentials=True, # y además con credenciales 😉
    allow_methods=["*"],
    allow_headers=["*"],
)

# DB bootstrap
Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Prometheus
Instrumentator().instrument(app).expose(app, include_in_schema=False, endpoint="/metrics")

@app.get("/health")
def health():
    return {"status":"ok"}

# ---- Auth insegura (para práctica) ----
@app.post("/auth/login")
def login(payload: dict):
    """
    Inseguro por diseño:
    - No rate limiting
    - Retorna 'token' plano y estático
    - Sin verificación real (para ejercicios de fuerza bruta / enumeración)
    """
    username = payload.get("username")
    password = payload.get("password")
    if not username or not password:
        raise HTTPException(status_code=400, detail="Missing credentials")
    return {"token": "static-dev-token", "role": "user", "username": username}

# ---- CRUD Clients ----
@app.post("/clients", response_model=ClientOut, status_code=201)
def create_client(data: ClientIn, db: Session = Depends(get_db)):
    c = Client(name=data.name, email=data.email, notes=data.notes)
    db.add(c)
    db.commit()
    db.refresh(c)
    return c

@app.get("/clients", response_model=List[ClientOut])
def list_clients(db: Session = Depends(get_db)):
    # Sin auth por diseño (para pruebas de control de acceso)
    return db.query(Client).all()

@app.get("/clients/{cid}", response_model=ClientOut)
def get_client(cid: int, db: Session = Depends(get_db)):
    c = db.get(Client, cid)
    if not c:
        raise HTTPException(404, "Client not found")
    return c

@app.put("/clients/{cid}", response_model=ClientOut)
def update_client(cid: int, data: ClientIn, db: Session = Depends(get_db)):
    c = db.get(Client, cid)
    if not c:
        raise HTTPException(404, "Client not found")
    c.name, c.email, c.notes = data.name, data.email, data.notes
    db.commit()
    db.refresh(c)
    return c

@app.delete("/clients/{cid}", status_code=204)
def delete_client(cid: int, db: Session = Depends(get_db)):
    c = db.get(Client, cid)
    if not c:
        return Response(status_code=204)
    db.delete(c)
    db.commit()
    return Response(status_code=204)

# ---- Endpoint vulnerable a XSS reflejado ----
@app.get("/search")
def search(q: str):
    """
    Devuelve el término de búsqueda sin sanitizar (para evidenciar reflected XSS)
    """
    # No sanitizar (intencional)
    return Response(
        content=f"<h3>Resultados para: {q}</h3><p>(demo)</p>",
        media_type="text/html"
    )

# ---- Manejo de errores verboso (para práctica) ----
@app.middleware("http")
async def error_verbosity(request: Request, call_next):
    try:
        return await call_next(request)
    except Exception as e:
        # stacktrace en respuesta (mala práctica intencional)
        import traceback
        tb = traceback.format_exc()
        logger.error(tb)
        return Response(content=f"Internal Error:\n{tb}", status_code=500, media_type="text/plain")
