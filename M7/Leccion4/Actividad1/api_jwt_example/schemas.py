from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str


class User(BaseModel):
    username: str
    email: str
    role: str


class UserUpdateRole(BaseModel):
    role: str
