import nmap
import json

scanner = nmap.PortScanner()
host = "127.0.0.1"
scanner.scan(hosts=host, arguments="-p 1-1024 -sV")

resultado = {"host": host, "puertos_abiertos": []}

for proto in scanner[host].all_protocols():
    ports = scanner[host][proto].keys()
    for port in ports:
        servicio = scanner[host][proto][port]["name"]
        version = scanner[host][proto][port].get("version", "")
        resultado["puertos_abiertos"].append({"puerto": port, "servicio": servicio, "version": version})

with open("scanner.json", "w") as f:
    json.dump(resultado, f, indent=4)

print("[+] Escaneo de puertos completado. Resultados guardados en scanner.json")