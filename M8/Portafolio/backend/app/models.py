from sqlalchemy import Column, Integer, String, Text
from .db import Base

class Client(Base):
    __tablename__ = "clients"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200), nullable=False)
    email = Column(String(200), nullable=False, unique=False)  # intencionalmente sin unique
    notes = Column(Text, nullable=True)  # puede contener XSS si no se sanea en el front
