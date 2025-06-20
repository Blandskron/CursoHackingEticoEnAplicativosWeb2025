from locust import HttpUser, task, between
from random import choice
import json

# Lista de usuarios para pruebas de carga
user_credentials = [
    {"username": "user1@example.com", "password": "pass123"},
    {"username": "user2@example.com", "password": "pass456"},
    {"username": "user3@example.com", "password": "pass789"},
    {"username": "user4@example.com", "password": "pass000"},
]

class LoginUser(HttpUser):
    wait_time = between(1, 2)  # tiempo entre peticiones

    @task(5)
    def login(self):
        user = choice(user_credentials)
        self.client.post(
            "/login",
            headers={"Content-Type": "application/json"},
            data=json.dumps(user)
        )

# locust -f locustfile.py --host http://localhost:8000  # reemplaza con tu dominio real
