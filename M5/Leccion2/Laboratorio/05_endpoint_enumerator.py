import requests

base = input("Dominio base (ej: http://192.168.1.10:8080): ")
rutas = ["admin", "login", "dashboard", "config", "robots.txt", ".git"]

for ruta in rutas:
    url = f"{base}/{ruta}"
    r = requests.get(url)
    if r.status_code == 200:
        print(f"Ruta encontrada: {url}")
    elif r.status_code == 403:
        print(f"Ruta protegida: {url}")
    else:
        print(f"{ruta} no disponible")
    