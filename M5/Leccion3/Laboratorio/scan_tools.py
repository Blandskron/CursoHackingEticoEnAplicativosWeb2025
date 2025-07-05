import requests

def obtener_headers(url):
    res = requests.get(url)
    return res.headers

def detectar_tecnologias(headers):
    return {
        "server": headers.get("Server", "Desconocido"),
        "powered_by": headers.get("X-Powered-By", "Desconocido")
    }
