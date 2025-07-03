from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from database import get_connection, init_db
from models import UserCreate, UserLogin
from security import hash_password, verify_password, create_access_token, decode_token
from datetime import timedelta
from jose import JWTError

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

@app.on_event("startup")
def startup():
    init_db()

@app.post("/register")
def register(user: UserCreate):
    conn = get_connection()
    cursor = conn.cursor()
    hashed_pw = hash_password(user.password)
    try:
        cursor.execute(
            "INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
            (user.username, hashed_pw, user.role)
        )
        conn.commit()
        return {"message": "Usuario registrado correctamente"}
    except:
        raise HTTPException(status_code=400, detail="Usuario ya existe")

@app.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ?", (form_data.username,))
    user = cursor.fetchone()
    if not user or not verify_password(form_data.password, user["password"]):
        raise HTTPException(status_code=401, detail="Credenciales inválidas")
    
    token = create_access_token(
        data={"sub": user["username"], "role": user["role"]},
        expires_delta=timedelta(minutes=30)
    )
    return {"access_token": token, "token_type": "bearer"}

@app.get("/panel")
def access_panel(token: str = Depends(oauth2_scheme)):
    try:
        payload = decode_token(token)
    except JWTError:
        raise HTTPException(status_code=403, detail="Token inválido o expirado")
    return {
        "message": f"Bienvenido {payload['sub']}",
        "role": payload["role"]
    }
