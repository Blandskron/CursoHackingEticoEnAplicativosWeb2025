from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from .database import Base

class LoginAttempt(Base):
    __tablename__ = "login_attempts"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    password = Column(String)
    ip_address = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)

class Comment(Base):
    __tablename__ = "comments"
    id = Column(Integer, primary_key=True, index=True)
    content = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)

class EventLog(Base):
    __tablename__ = "logs"
    id = Column(Integer, primary_key=True, index=True)
    type = Column(String)
    message = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)
