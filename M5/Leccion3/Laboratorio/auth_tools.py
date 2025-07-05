import requests
from bs4 import BeautifulSoup

def obtener_token_csrf(session, url_login):
    res = session.get(url_login)
    soup = BeautifulSoup(res.text, "html.parser")
    return soup.find("input", {"name": "csrfmiddlewaretoken"})["value"]

def intento_login(session, url, usuario, clave, csrf_token):
    datos = {
        "username": usuario,
        "password": clave,
        "csrfmiddlewaretoken": csrf_token
    }
    headers = {"Referer": url}
    return session.post(url, data=datos, headers=headers, allow_redirects=False)
