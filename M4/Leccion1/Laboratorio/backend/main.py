from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import sqlite3
from database import init_db

app = FastAPI()
init_db()

app.mount("/static", StaticFiles(directory="frontend"), name="static")
templates = Jinja2Templates(directory="frontend")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/login")
async def login(email: str = Form(...), password: str = Form(...)):
    conn = sqlite3.connect("vulnerable.db")
    cursor = conn.cursor()
    # Vulnerable a SQL Injection
    query = f"SELECT * FROM users WHERE email = '{email}' AND password = '{password}'"
    cursor.execute(query)
    user = cursor.fetchone()
    conn.close()

    if user:
        # Información sensible expuesta directamente
        return JSONResponse(content={"email": email, "password": password, "token": "abc123", "role": "admin"})
    return JSONResponse(content={"error": "Invalid credentials"}, status_code=401)

@app.get("/search")
async def search(q: str):
    conn = sqlite3.connect("vulnerable.db")
    cursor = conn.cursor()
    # Vulnerable a SQL Injection
    cursor.execute(f"SELECT * FROM products WHERE name LIKE '%{q}%'")
    products = cursor.fetchall()
    conn.close()

    # Vulnerable a XSS: sin escapar
    return JSONResponse(content={"results": [{"name": row[1], "description": row[2]} for row in products]})
