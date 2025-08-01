from fastapi import FastAPI, Depends, HTTPException, status
from auth import get_current_user, get_admin_user, create_access_token, authenticate_user
from models import UserDB, fake_users_db
from schemas import Token, User, UserUpdateRole
from fastapi.security import OAuth2PasswordRequestForm

app = FastAPI()


@app.post("/token", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Incorrect credentials")
    access_token = create_access_token(data={"sub": user["username"], "role": user["role"]})
    return {"access_token": access_token, "token_type": "bearer"}


@app.get("/api/users/me", response_model=User)
def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user


@app.get("/api/users", response_model=list[User])
def get_all_users(current_user: User = Depends(get_admin_user)):
    return list(fake_users_db.values())


@app.put("/api/users/{user_id}/role")
def update_user_role(user_id: int, body: UserUpdateRole, admin: User = Depends(get_admin_user)):
    if user_id not in fake_users_db:
        raise HTTPException(status_code=404, detail="User not found")
    fake_users_db[user_id]["role"] = body.role
    return {"msg": f"Role updated to {body.role}"}
