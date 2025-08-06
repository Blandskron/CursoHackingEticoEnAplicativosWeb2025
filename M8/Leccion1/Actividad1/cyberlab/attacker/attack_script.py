import requests
import time

BACKEND_URL = "http://waf:8001"


def brute_force(rounds=100):
    print("🔥 Iniciando ataque de fuerza bruta...")
    for i in range(rounds):
        payload = {
            "username": "admin",
            "password": f"wrongpass{i}"
        }
        r = requests.post(f"{BACKEND_URL}/login", json=payload)
        print(f"[{i+1}] Login {payload['password']} -> {r.status_code}")
        time.sleep(0.2)  # Simula tráfico real (ajustable)

def xss_payloads():
    print("💣 Iniciando ataque XSS...")
    payloads = [
        "<script>alert('x')</script>",
        "<img src=x onerror=alert('xss')>",
        "<svg/onload=alert(1)>",
        "<body onload=alert('xss')>",
        "<a href='javascript:alert(1)'>link</a>",
        "<script>String.fromCharCode(88,83,83)</script>",
        "<iframe src='javascript:alert(1)'>"
    ]
    for i, payload in enumerate(payloads):
        r = requests.post(f"{BACKEND_URL}/comment", json={"comment": payload})
        print(f"[{i+1}] XSS payload enviado -> {r.status_code}")
        time.sleep(0.5)

def header_injection():
    print("🧠 Inyección en headers...")
    headers = {
        "User-Agent": "<script>alert('x')</script>",
        "Referer": "javascript:alert('ref')",
        "X-Custom": "eval(alert(1))"
    }
    r = requests.post(f"{BACKEND_URL}/login", headers=headers, json={
        "username": "admin",
        "password": "headerattack"
    })
    print(f"Header injection -> {r.status_code}")

def query_injection():
    print("🧪 Inyección en query string...")
    url = f"{BACKEND_URL}/login?param=<script>alert(1)</script>"
    r = requests.get(url)
    print(f"Query injection -> {r.status_code}")

if __name__ == "__main__":
    brute_force(rounds=50)
    xss_payloads()
    header_injection()
    query_injection()
