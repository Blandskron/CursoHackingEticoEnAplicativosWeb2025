from database import engine, SessionLocal
from models import User, Base

# Crear las tablas
Base.metadata.create_all(bind=engine)

db = SessionLocal()

usuarios = [
    {"name": "Alice", "email": "alice@example.com"},
    {"name": "Bob", "email": "bob@example.com"},
    {"name": "Charlie", "email": "charlie@example.com"},
    {"name": "Diana", "email": "diana@example.com"},
    {"name": "Ethan", "email": "ethan@example.com"},
    {"name": "Fiona", "email": "fiona@example.com"},
    {"name": "George", "email": "george@example.com"},
    {"name": "Hannah", "email": "hannah@example.com"},
    {"name": "Ian", "email": "ian@example.com"},
    {"name": "Jenna", "email": "jenna@example.com"},
    {"name": "Kevin", "email": "kevin@example.com"},
    {"name": "Laura", "email": "laura@example.com"},
    {"name": "Michael", "email": "michael@example.com"},
    {"name": "Nina", "email": "nina@example.com"},
    {"name": "Oscar", "email": "oscar@example.com"},
    {"name": "Paula", "email": "paula@example.com"},
    {"name": "Quinn", "email": "quinn@example.com"},
    {"name": "Ryan", "email": "ryan@example.com"},
    {"name": "Sophia", "email": "sophia@example.com"},
    {"name": "Thomas", "email": "thomas@example.com"}
]

for u in usuarios:
    db.add(User(name=u["name"], email=u["email"]))

db.commit()
db.close()
