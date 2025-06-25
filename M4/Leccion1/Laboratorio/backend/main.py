from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import sqlite3
from database import init_db
from pathlib import Path

# Inicializar base de datos
init_db()

# Base directory: subir desde backend/ hacia la raíz del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent
FRONTEND_DIR = BASE_DIR / "frontend"

# Crear instancia FastAPI
app = FastAPI()

# Montar archivos estáticos
app.mount("/static", StaticFiles(directory=FRONTEND_DIR), name="static")

# Configurar plantilla HTML
templates = Jinja2Templates(directory=str(FRONTEND_DIR))

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/login")
async def login(email: str = Form(...), password: str = Form(...)):
    conn = sqlite3.connect("vulnerable.db")
    cursor = conn.cursor()
    # ❗️ Vulnerabilidad: Inyección SQL
    query = f"SELECT * FROM users WHERE email = '{email}' AND password = '{password}'"
    cursor.execute(query)
    user = cursor.fetchone()
    conn.close()

    if user:
        # ❗️ Vulnerabilidad: exposición de datos sensibles
        return JSONResponse(content={
            "email": email,
            "password": password,
            "token": "abc123",
            "role": "admin"
        })
    return JSONResponse(content={"error": "Invalid credentials"}, status_code=401)

@app.get("/search")
async def search(q: str):
    conn = sqlite3.connect("vulnerable.db")
    cursor = conn.cursor()
    # ❗️ Vulnerabilidad: Inyección SQL
    cursor.execute(f"SELECT * FROM products WHERE name LIKE '%{q}%'")
    products = cursor.fetchall()
    conn.close()

    # ❗️ Vulnerabilidad: XSS reflejado
    return JSONResponse(content={
        "results": [{"name": row[1], "description": row[2]} for row in products]
    })
