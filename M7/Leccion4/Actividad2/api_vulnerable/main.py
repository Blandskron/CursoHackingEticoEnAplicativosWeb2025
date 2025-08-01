from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from models import fake_users_db
from schemas import UserCreate, UserOut

app = FastAPI()

@app.get("/api/users", response_model=List[UserOut])
def get_users():
    return list(fake_users_db.values())

@app.post("/api/users", response_model=UserOut)
def create_user(user: UserCreate):
    new_id = max(fake_users_db.keys()) + 1 if fake_users_db else 1
    fake_users_db[new_id] = {
        "id": new_id,
        "username": user.username,
        "email": user.email,
        "password": "default123"
    }
    return fake_users_db[new_id]

@app.delete("/api/users/{user_id}")
def delete_user(user_id: int):
    if user_id in fake_users_db:
        del fake_users_db[user_id]
        return {"msg": f"User {user_id} deleted"}
    raise HTTPException(status_code=404, detail="User not found")
