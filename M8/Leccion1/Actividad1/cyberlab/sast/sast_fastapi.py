from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

ip_scans = {}
SCAN_LIMIT = 5

@app.get("/scan")
def sast(request: Request):
    client_ip = request.client.host
    ip_scans[client_ip] = ip_scans.get(client_ip, 0) + 1

    if ip_scans[client_ip] > SCAN_LIMIT:
        return JSONResponse(status_code=429, content={"msg": "Límite de escaneos alcanzado para esta IP"})

    return {
        "vulnerabilities": [
            {"file": "index.html", "issue": "Falta sanitización en comentarios"},
            {"file": "app.js", "issue": "Sin escape de datos en renderizado"}
        ]
    }
