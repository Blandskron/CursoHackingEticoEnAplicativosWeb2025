from fastapi import FastAPI, Request
from pydantic import BaseModel
from .database import Base, engine, SessionLocal
from .models import LoginAttempt, Comment
from .logger import log_event

Base.metadata.create_all(bind=engine)

app = FastAPI()

class LoginData(BaseModel):
    username: str
    password: str

class CommentData(BaseModel):
    comment: str

@app.post("/login")
async def login(data: LoginData, request: Request):
    ip = request.headers.get("X-Forwarded-For") or request.client.host
    session = SessionLocal()
    session.add(LoginAttempt(username=data.username, password=data.password, ip_address=ip))
    session.commit()
    session.close()
    log_event("login_attempt", f"{data.username} desde {ip}")
    return {"msg": "Intento registrado"}

@app.post("/comment")
async def comment(data: CommentData):
    session = SessionLocal()
    session.add(Comment(content=data.comment))
    session.commit()
    session.close()
    log_event("comment", f"Comentario registrado: {data.comment}")
    return {"msg": "Comentario recibido"}

@app.get("/comments")
async def get_comments():
    session = SessionLocal()
    comments = session.query(Comment).all()
    return [c.content for c in comments]

@app.get("/admin/export")
async def export_data():
    log_event("export_access", "Se accedió al endpoint /admin/export sin control")
    return {"data": "user,password\nadmin,admin123"}
