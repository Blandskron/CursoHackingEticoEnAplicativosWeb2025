import requests
from bs4 import BeautifulSoup

def detectar_formularios(url):
    try:
        # Solicitud HTTP
        respuesta = requests.get(url, timeout=5)
        respuesta.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] No se pudo conectar a {url}: {e}")
        return

    # Procesar contenido con BeautifulSoup
    soup = BeautifulSoup(respuesta.text, 'html.parser')
    formularios = soup.find_all('form')

    if not formularios:
        print("No se detectaron formularios en la página.")
        return

    print(f"\n🔍 Formularios detectados en: {url}\n")

    for i, form in enumerate(formularios, 1):
        metodo = form.get('method', 'GET').upper()
        accion = form.get('action', '[sin acción definida]')
        print(f"📝 Formulario #{i}:")
        print(f"   - Método: {metodo}")
        print(f"   - Acción: {accion}")
        print(f"   - Campos encontrados:")

        # Buscar campos input, textarea, select
        campos = form.find_all(['input', 'textarea', 'select'])

        for campo in campos:
            tipo = campo.get('type', 'text') if campo.name == 'input' else campo.name
            nombre = campo.get('name', '[sin nombre]')
            print(f"     * name: {nombre} | type: {tipo}")
        
        print()

if __name__ == "__main__":
    print("=== Detección de Formularios HTML y Campos de Entrada ===\n")
    url = input("Ingresa la URL (ej: https://httpbin.org/forms/post): ").strip()
    detectar_formularios(url)
