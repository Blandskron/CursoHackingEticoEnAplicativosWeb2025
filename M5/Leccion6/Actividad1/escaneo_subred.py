import nmap
import argparse
import ipaddress
from datetime import datetime
from tqdm import tqdm
import json
import threading

def escanear_host(scanner, host, argumentos, resultados):
    """Escanea un host específico y guarda los datos encontrados."""
    try:
        argumentos_str = " ".join(argumentos) if isinstance(argumentos, list) else argumentos
        scanner.scan(hosts=host, arguments=argumentos_str)
        if host in scanner.all_hosts():
            datos = {
                "host": host,
                "estado": scanner[host].state(),
                "puertos": []
            }
            for proto in scanner[host].all_protocols():
                lport = scanner[host][proto].keys()
                for port in sorted(lport):
                    datos["puertos"].append({
                        "puerto": port,
                        "estado": scanner[host][proto][port]['state'],
                        "servicio": scanner[host][proto][port].get('name', ''),
                        "version": scanner[host][proto][port].get('version', '')
                    })
            resultados.append(datos)
    except Exception as e:
        print(f"[!] Error escaneando {host}: {e}")

def escanear_subred(subred, argumentos):
    """Realiza escaneo de una subred completa detectando hosts activos y escaneando puertos."""
    try:
        red = ipaddress.IPv4Network(subred, strict=False)
    except ValueError:
        print("[ERROR] La subred ingresada no es válida.")
        return []

    print(f"[+] Detectando hosts activos en {subred}...")
    scanner = nmap.PortScanner()
    scanner.scan(hosts=subred, arguments="-sn")
    activos = [host for host in scanner.all_hosts() if scanner[host].state() == 'up']

    print(f"[+] {len(activos)} hosts activos detectados.")
    print(f"[+] Iniciando escaneo detallado con argumentos '{' '.join(argumentos)}'...")

    resultados = []
    threads = []
    for host in tqdm(activos):
        t = threading.Thread(target=escanear_host, args=(scanner, host, argumentos, resultados))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    return resultados

def guardar_resultados(resultados, archivo):
    """Guarda los resultados del escaneo en formato JSON."""
    with open(archivo, 'w') as f:
        json.dump(resultados, f, indent=2)
    print(f"[✔] Resultados guardados en {archivo}")

def main():
    parser = argparse.ArgumentParser(description="Escáner avanzado de subred con Nmap")
    parser.add_argument("-s", "--subred", required=True, help="Subred a escanear (ej: 192.168.1.0/24)")
    parser.add_argument("-a", "--argumentos", nargs=argparse.REMAINDER, default=["-T4", "-F"],
                        help="Argumentos adicionales para Nmap (ej: -sS -sV -O)")
    parser.add_argument("-o", "--output", default="resultados_escaneo.json", help="Archivo de salida en JSON")
    args = parser.parse_args()

    resultados = escanear_subred(args.subred, args.argumentos)
    if resultados:
        guardar_resultados(resultados, args.output)

if __name__ == "__main__":
    main()
