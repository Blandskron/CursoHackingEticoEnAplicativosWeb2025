import nmap
import argparse
import logging
from datetime import datetime
import socket
import sys

# Configurar logs
logging.basicConfig(
    filename='port_scan.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def validar_ip(ip):
    try:
        socket.inet_aton(ip)
        return True
    except socket.error:
        return False

def escaneo_puertos(ip_objetivo: str, puerto_inicio: int = 1, puerto_fin: int = 1024):
    logging.info(f"Iniciando escaneo para {ip_objetivo} en el rango {puerto_inicio}-{puerto_fin}")
    print(f"\n🔍 Escaneando el host: {ip_objetivo} (puertos {puerto_inicio}-{puerto_fin})...\n")
    
    scanner = nmap.PortScanner()
    try:
        scanner.scan(ip_objetivo, f"{puerto_inicio}-{puerto_fin}")
    except Exception as e:
        logging.error(f"Error al ejecutar el escaneo: {e}")
        print(f"❌ Error al ejecutar el escaneo: {e}")
        sys.exit(1)

    if not scanner.all_hosts():
        print("❌ No se detectó ningún host activo.")
        return

    for host in scanner.all_hosts():
        print(f"📌 Resultados para {host}:")
        for protocolo in scanner[host].all_protocols():
            puertos = scanner[host][protocolo].keys()
            for puerto in sorted(puertos):
                estado = scanner[host][protocolo][puerto]['state']
                servicio = scanner[host][protocolo][puerto].get('name', '')
                version = scanner[host][protocolo][puerto].get('version', '')
                print(f" - Puerto {puerto}: {estado} | Servicio: {servicio} | Versión: {version}")

    print("\n✅ Escaneo completado.")
    logging.info(f"Escaneo completado para {ip_objetivo}")

def main():
    parser = argparse.ArgumentParser(description="Escáner avanzado de puertos con python-nmap")
    parser.add_argument("-t", "--target", required=True, help="Dirección IP a escanear (ej: 127.0.0.1)")
    parser.add_argument("--start-port", type=int, default=1, help="Puerto inicial (por defecto: 1)")
    parser.add_argument("--end-port", type=int, default=1024, help="Puerto final (por defecto: 1024)")

    args = parser.parse_args()

    if not validar_ip(args.target):
        print("❌ IP no válida. Usa un formato como 127.0.0.1")
        sys.exit(1)

    escaneo_puertos(args.target, args.start_port, args.end_port)

if __name__ == "__main__":
    main()
