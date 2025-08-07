from fastapi import FastAPI, Request, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import PlainTextResponse, JSONResponse
from sqlalchemy.orm import Session
from models import Base, User
from database import SessionLocal, engine

# Crear tablas si no existen
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependencia para obtener sesión DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def root():
    return {"message": "Backend operativo con SQLite"}

@app.get("/search")
def search(q: str):
    # Vulnerabilidad XSS persistente
    return PlainTextResponse(f"Resultados para: {q}")

@app.get("/admin/users/export")
def export_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    csv = "id,name,email\n"
    for user in users:
        csv += f"{user.id},{user.name},{user.email}\n"
    return PlainTextResponse(csv, media_type="text/csv", headers={"Access-Control-Allow-Origin": "*"})

@app.get("/users")
def get_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return [{"id": u.id, "name": u.name, "email": u.email} for u in users]

@app.post("/delete-user")
async def delete_user(request: Request, db: Session = Depends(get_db)):
    body = await request.json()
    user_id = body.get("id")
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()
        return {"message": f"Usuario {user_id} eliminado"}
    return {"message": "Usuario no encontrado"}
