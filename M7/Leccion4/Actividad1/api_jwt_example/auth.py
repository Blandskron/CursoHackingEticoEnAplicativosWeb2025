from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from models import fake_users_db
from schemas import User
from datetime import datetime, timedelta

SECRET_KEY = "secret"
ALGORITHM = "HS256"
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def create_access_token(data: dict, expires_delta: timedelta = timedelta(hours=1)):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


def decode_token(token: str):
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except JWTError:
        raise HTTPException(status_code=403, detail="Invalid token")


def get_current_user(token: str = Depends(oauth2_scheme)) -> User:
    payload = decode_token(token)
    username = payload.get("sub")
    role = payload.get("role")
    if username is None or role is None:
        raise HTTPException(status_code=403, detail="Invalid token")
    for user in fake_users_db.values():
        if user["username"] == username:
            return User(username=username, email=user["email"], role=role)
    raise HTTPException(status_code=404, detail="User not found")


def get_admin_user(current_user: User = Depends(get_current_user)) -> User:
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Not enough privileges")
    return current_user


def authenticate_user(username: str, password: str):
    for user in fake_users_db.values():
        if user["username"] == username and user["password"] == password:
            return user
    return None
