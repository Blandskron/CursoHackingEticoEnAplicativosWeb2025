import requests

url = input("Ingresa la URL objetivo (ej: http://192.168.1.10:8080): ")

response = requests.get(url, timeout=5)
print(response.headers)
