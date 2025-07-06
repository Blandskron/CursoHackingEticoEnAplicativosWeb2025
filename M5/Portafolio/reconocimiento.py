import requests
from bs4 import BeautifulSoup
import json

COMMON_PATHS = ["/admin", "/login", "/config", "/dashboard"]

url_base = "http://testphp.vulnweb.com"
result = {
    "url_base": url_base,
    "rutas_detectadas": [],
    "formularios": [],
    "cabeceras": {}
}

for path in COMMON_PATHS:
    url = url_base + path
    res = requests.get(url)
    if res.status_code == 200:
        result["rutas_detectadas"].append(path)

    soup = BeautifulSoup(res.text, "html.parser")
    for form in soup.find_all("form"):
        campos = [input_tag.get("name") for input_tag in form.find_all("input") if input_tag.get("name")]
        result["formularios"].append({
            "action": form.get("action"),
            "método": form.get("method"),
            "campos": campos
        })

result["cabeceras"] = dict(res.headers)

with open("reconocimiento.json", "w") as f:
    json.dump(result, f, indent=4)

print("[+] Reconocimiento completado. Resultados guardados en reconocimiento.json")