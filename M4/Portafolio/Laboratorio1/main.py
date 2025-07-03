from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import init_db
from models import UserLogin, UserCreate
from database import get_connection
from fastapi import HTTPException

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()  # se ejecuta al iniciar la app
    yield
    # puedes poner cleanup aquí si deseas

app = FastAPI(lifespan=lifespan)

@app.post("/register")
def register(user: UserCreate):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            f"INSERT INTO users (username, password, role) VALUES ('{user.username}', '{user.password}', '{user.role}')"
        )
        conn.commit()
        return {"message": "Usuario registrado"}
    except Exception as e:
        raise HTTPException(status_code=400, detail="Error al registrar usuario")

@app.post("/login")
def login(user: UserLogin):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        f"SELECT * FROM users WHERE username = '{user.username}' AND password = '{user.password}'"
    )
    result = cursor.fetchone()
    if result:
        return {
            "message": f"Bienvenido {result['username']}",
            "role": result["role"],
            "token": "insecure-token"
        }
    raise HTTPException(status_code=401, detail="Credenciales inválidas")

@app.get("/panel")
def panel():
    return {"message": "Todos los usuarios acceden al mismo panel sin restricción"}
