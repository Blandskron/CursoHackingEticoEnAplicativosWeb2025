import requests

def analizar_encabezados():
    print("=== Exploración de Encabezados HTTP ===\n")
    url = input("Ingresa la URL del sitio (ej. https://www.python.org): ").strip()

    try:
        respuesta = requests.get(url, timeout=5)
        print("respuesta " + respuesta.text)
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] No se pudo conectar a {url}: {e}")
        return

    print("\n📦 Encabezados de respuesta HTTP:")
    print("----------------------------------")
    for clave, valor in respuesta.headers.items():
        print(f"{clave}: {valor}")

    # Reflexión técnica automatizada (opcional para estudiantes avanzados)
    print("\n🔍 Posibles cabeceras útiles en reconocimiento:")
    cabeceras_clave = ["Server", "X-Powered-By", "Strict-Transport-Security", "X-Frame-Options", "Content-Type"]
    for cabecera in cabeceras_clave:
        if cabecera in respuesta.headers:
            print(f"✔ {cabecera}: {respuesta.headers[cabecera]}")
        else:
            print(f"✘ {cabecera}: No encontrada")

if __name__ == "__main__":
    analizar_encabezados()
