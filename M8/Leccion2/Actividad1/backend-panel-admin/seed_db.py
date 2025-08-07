from database import engine, SessionLocal
from models import User, Base

# Crear las tablas
Base.metadata.create_all(bind=engine)

db = SessionLocal()

usuarios = [
    {"name": "Alice", "email": "alice@example.com"},
    {"name": "Bob", "email": "bob@example.com"},
    {"name": "Charlie", "email": "charlie@example.com"},
]

for u in usuarios:
    db.add(User(name=u["name"], email=u["email"]))

db.commit()
db.close()
