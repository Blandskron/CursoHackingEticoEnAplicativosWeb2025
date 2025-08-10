FROM python:3.11-slim

# Sugerencias para menos sorpresas
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Instala deps primero (mejor cache)
COPY requirements.txt .
RUN pip install -U pip && pip install -r requirements.txt

# Copia el resto de la app (main.py, logstash_logger.py, .env.example, etc.)
COPY . .

# EntryPoint de depuración (verifica imports y archivos)
RUN chmod +x /app/entrypoint.sh

EXPOSE 8000
ENTRYPOINT ["/app/entrypoint.sh"]
