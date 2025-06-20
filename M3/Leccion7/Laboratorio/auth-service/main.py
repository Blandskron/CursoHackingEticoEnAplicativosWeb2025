from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class LoginRequest(BaseModel):
    username: str
    password: str

@app.post("/login")
def login(request: LoginRequest):
    if request.username == "admin" and request.password == "admin":
        return {"token": "fake-jwt-token"}
    raise HTTPException(status_code=401, detail="Invalid credentials")
