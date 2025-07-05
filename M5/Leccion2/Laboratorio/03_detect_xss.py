import requests

url = input("URL con parámetro vulnerable (ej: http://192.168.1.10:8080/search?q=): ")

payload = "<script>alert('xss')</script>"
test_url = url + payload

response = requests.get(test_url)

if payload in response.text:
    print("Vulnerabilidad XSS detectada")
else:
    print("No vulnerable con este payload")
