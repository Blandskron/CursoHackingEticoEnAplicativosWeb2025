import logging
from logging.handlers import RotatingFileHandler
from .database import SessionLocal
from .models import EventLog
import os

# Asegura que exista la carpeta logs (dentro del contenedor)
os.makedirs("logs", exist_ok=True)

logger = logging.getLogger("cyberlab")
logger.setLevel(logging.INFO)
handler = RotatingFileHandler("logs/app.log", maxBytes=1000000, backupCount=3)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

def log_event(tipo: str, mensaje: str):
    db = SessionLocal()
    db.add(EventLog(type=tipo, message=mensaje))
    db.commit()
    db.close()
    logger.info(f"[{tipo}] {mensaje}")
