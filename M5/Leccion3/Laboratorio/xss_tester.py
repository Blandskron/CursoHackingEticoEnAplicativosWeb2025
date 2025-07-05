import requests

def probar_xss(url, payload):
    r = requests.get(url + payload)
    return payload in r.text

generar_payload = lambda texto: f"<script>alert('{texto}')</script>"
