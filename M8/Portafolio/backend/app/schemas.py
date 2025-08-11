from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class ClientIn(BaseModel):
    name: str = Field(min_length=1, max_length=200)
    email: EmailStr
    notes: Optional[str] = None

class ClientOut(BaseModel):
    id: int
    name: str
    email: EmailStr
    notes: Optional[str] = None

    class Config:
        from_attributes = True
