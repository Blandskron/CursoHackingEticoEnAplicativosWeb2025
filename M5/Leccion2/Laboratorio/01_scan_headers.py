import requests

url = input("Ingresa la URL objetivo (ej: http://192.168.1.10:8080): ")
try:
    response = requests.get(url, timeout=5)
    print("\n=== Cabeceras HTTP ===")
    for k, v in response.headers.items():
        print(f"{k}: {v}")

    if "X-Powered-By" in response.headers:
        print("\nTecnología expuesta:", response.headers["X-Powered-By"])
    if "Server" in response.headers:
        print("Servidor detectado:", response.headers["Server"])
except Exception as e:
    print("Error al conectar:", e)
