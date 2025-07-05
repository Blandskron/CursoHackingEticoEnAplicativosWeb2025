import requests
from auth_tools import obtener_token_csrf, intento_login
from scan_tools import obtener_headers, detectar_tecnologias
from xss_tester import probar_xss, generar_payload
from utils import mostrar_banner

# Solicitar URL base al usuario
base_url = input("Ingresa la URL base del objetivo (ej: http://192.168.1.10:8000): ").strip()
login_url = f"{base_url}/login"
xss_url = f"{base_url}/search?q="

session = requests.Session()

def probar_conexion(url):
    try:
        requests.get(url, timeout=5)
        return True
    except requests.exceptions.RequestException as e:
        print(f"Error de conexión con {url}: {e}")
        return False

# Paso 1: Reconocimiento de cabeceras
mostrar_banner("Reconocimiento de cabeceras")

if probar_conexion(base_url):
    try:
        cabeceras = obtener_headers(base_url)
        tecnologias = detectar_tecnologias(cabeceras)
        for clave, valor in tecnologias.items():
            print(f"{clave}: {valor}")
    except Exception as e:
        print("No se pudo analizar cabeceras:", e)
else:
    print("No se pudo conectar al objetivo.")
    exit()

# Paso 2: Login automatizado
mostrar_banner("Login automatizado")

if probar_conexion(login_url):
    try:
        csrf = obtener_token_csrf(session, login_url)
        response = intento_login(session, login_url, "admin", "admin1234", csrf)
        if response.status_code in [302, 303]:
            print("Login exitoso")
        else:
            print("Login fallido")
    except Exception as e:
        print("Error durante login:", e)
else:
    print("El formulario de login no está disponible.")

# Paso 3: Test de XSS
mostrar_banner("Prueba de XSS")

if probar_conexion(xss_url):
    payload = generar_payload("XSS")
    if probar_xss(xss_url, payload):
        print("Vulnerabilidad XSS detectada")
    else:
        print("No vulnerable con este payload")
else:
    print("No se pudo acceder al endpoint de prueba XSS.")
