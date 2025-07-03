import requests

def analyze_headers(url):
    if not url.startswith("http://") and not url.startswith("https://"):
        url = "http://" + url

    print(f"\nAnalizando cabeceras de: {url}\n")

    try:
        response = requests.get(url)
    except requests.exceptions.RequestException as e:
        print(f"Error al realizar la solicitud: {e}")
        return

    if response.status_code != 200:
        print(f"Advertencia: el servidor respondió con código {response.status_code}\n")

    headers = response.headers

    print("Cabeceras encontradas:\n")
    for key, value in headers.items():
        print(f"  {key}: {value}")

    print("\nAnálisis específico:\n")

    if "Server" in headers:
        print(f"Server: {headers['Server']}")
    else:
        print("Server: No especificado")

    if "X-Powered-By" in headers:
        print(f"X-Powered-By: {headers['X-Powered-By']}")
    else:
        print("X-Powered-By: No especificado")

    if "Content-Type" in headers:
        print(f"Content-Type: {headers['Content-Type']}")
    else:
        print("Content-Type: No especificado")

    if "Set-Cookie" in headers:
        print(f"Set-Cookie: {headers['Set-Cookie']}")
    else:
        print("Set-Cookie: No especificado")

    if "Strict-Transport-Security" in headers:
        print(f"Strict-Transport-Security: {headers['Strict-Transport-Security']}")
    else:
        print("Strict-Transport-Security: No especificado")

if __name__ == "__main__":
    print("Herramienta de Análisis de Cabeceras HTTP")
    target_url = input("Ingresa la URL del sitio a analizar: ")
    analyze_headers(target_url)
