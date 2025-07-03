import socket

def scan_ports(host, start_port=20, end_port=1024):
    print(f"\nEscaneando puertos del host: {host} (de {start_port} a {end_port})\n")

    try:
        for port in range(start_port, end_port + 1):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)
            result = s.connect_ex((host, port))
            if result == 0:
                print(f"Puerto {port}: ABIERTO")
            s.close()
    except socket.gaierror:
        print("Error: El host no fue encontrado.")
    except socket.error:
        print("Error: No se pudo establecer conexión.")
    
    print("\nEscaneo finalizado.")

if __name__ == "__main__":
    print("Escáner de Puertos Básico con Python")
    target_host = input("Ingresa la dirección IP o dominio a escanear: ")
    scan_ports(target_host)
