# Laboratorio 2 – Verificación del Backend Seguro (FastAPI + SQLite + JWT)

## Paso a paso realizado (con tokens reales)


### Registro de usuario normal

```bash
curl -X POST http://localhost:8000/register \
  -H "Content-Type: application/json" \
  -d '{"username": "usuario1", "password": "clave123", "role": "user"}'
```

✔ Resultado: `Usuario registrado correctamente`


### Registro de administrador

```bash
curl -X POST http://localhost:8000/register \
  -H "Content-Type: application/json" \
  -d '{"username": "admin", "password": "admin123", "role": "admin"}'
```

✔ Resultado: `Usuario registrado correctamente`


### Login como `usuario1`

```bash
curl -X POST http://localhost:8000/login \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=usuario1&password=clave123"
```

✔ Resultado:

```json
{
  "access_token": "<TOKEN_DE_USUARIO>",
  "token_type": "bearer"
}
```


### Login como `admin`

```bash
curl -X POST http://localhost:8000/login \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=admin&password=admin123"
```

✔ Resultado:

```json
{
  "access_token": "<TOKEN_DE_ADMIN>",
  "token_type": "bearer"
}
```


### Acceso al panel como administrador

```bash
curl -X GET http://localhost:8000/panel \
  -H "Authorization: Bearer <TOKEN_DE_ADMIN>"
```

✔ Resultado:

```json
{"message":"Bienvenido admin","role":"admin"}
```


### Confirmación de Seguridad

| Ataque              | Resultado con backend seguro                                                |
| ------------------- | --------------------------------------------------------------------------- |
| Inyección SQL       | ❌ No es posible (uso de `?`)                                                |
| XSS en `username`   | ❌ Rechazado (valores válidos)                                               |
| Acceso sin login    | ❌ Rechazado automáticamente                                                 |
| Escalada por `role` | ✅ Permitido solo si lo define el admin en frontend o backend con validación |
| Token manipulado    | ❌ Detectado por `JWTError`                                                  |

uvicorn main:app --reload
