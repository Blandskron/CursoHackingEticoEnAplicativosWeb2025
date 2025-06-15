```bash
# ===============================
# COMANDOS PARA LABORATORIO LECCIÓN 5 - INTRANET LOCAL
# ===============================

# 1. Crear estructura del proyecto
mkdir lab-intranet
cd lab-intranet
mkdir app

# 2. Crear archivo index.html con el contenido de la intranet
echo '<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>Intranet de Mi Empresa</title>
</head>
<body>
  <h1>Bienvenido a la intranet de miempresa.local</h1>
  <p>Este sitio simula una intranet interna de empresa.</p>
</body>
</html>' > app/index.html

# 3. Crear archivo nginx.conf para configuración del servidor
echo 'server {
    listen 80;
    server_name intranet.miempresa.local;

    root /usr/share/nginx/html;
    index index.html;

    location / {
        try_files \$uri \$uri/ =404;
    }
}' > nginx.conf

# 4. Crear Dockerfile base
echo 'FROM nginx:alpine' > Dockerfile

# 5. Crear archivo docker-compose.yml
echo 'version: "3.8"

services:
  nginx:
    build: .
    container_name: intranet
    ports:
      - "80:80"
    volumes:
      - ./nginx.conf:/etc/nginx/conf.d/default.conf
      - ./app:/usr/share/nginx/html:ro
    networks:
      - red_intranet

networks:
  red_intranet:
    driver: bridge' > docker-compose.yml

# 6. Editar el archivo HOSTS (realizar manualmente con permisos de administrador)
# Windows: C:\Windows\System32\drivers\etc\hosts
# Agregar al final:
# 127.0.0.1    intranet.miempresa.local

# 7. Levantar el entorno Docker
docker compose up --build -d

# 8. Probar acceso desde navegador:
# http://intranet.miempresa.local

# 9. (Opcional) Ver tráfico con Wireshark
# Filtro sugerido:
# http.host contains "miempresa.local"
```
