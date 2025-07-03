from pydantic import BaseModel, constr

class UserCreate(BaseModel):
    username: constr(strip_whitespace=True, min_length=3)
    password: constr(min_length=6)
    role: str

class UserLogin(BaseModel):
    username: str
    password: str
