### 🟥 1. **XSS con variantes evasivas**

El objetivo es burlar la regex actual del WAF.

```bash
curl -X POST http://localhost:8001/comment -H "Content-Type: application/json" \
  -d '{"comment":"<sCript >alert(String.fromCharCode(88,83,83))</sCript>"}'
```

```bash
curl -X POST http://localhost:8001/comment -H "Content-Type: application/json" \
  -d '{"comment":"<IMG SRC=\"javascript:alert(\'XSS\')\">"}'
```

---

### 🟨 2. **SQL Injection encubierta**

Para evaluar si el WAF detecta variantes:

```bash
curl -X POST http://localhost:8001/login -H "Content-Type: application/json" \
  -d '{"username":"admin\'/**/OR/**/1=1--", "password":"x"}'
```

---

### 🟧 3. **Command Injection**

Si decides simular endpoints que ejecuten comandos (por ejemplo, usando `subprocess.run()`), prueba esto:

```bash
curl -X POST http://localhost:8001/execute -H "Content-Type: application/json" \
  -d '{"command":"; whoami"}'
```

---

### 🟪 4. **Inyección en headers**

Haz que el WAF analice headers como `User-Agent`, `Referer`, etc.

```bash
curl -X POST http://localhost:8001/login \
  -H "User-Agent: eval(alert(1))" \
  -H "Content-Type: application/json" \
  -d '{"username":"admin", "password":"pass"}'
```

---

### 🟫 5. **Tasa de requests para simular DoS/fuerza bruta extrema**

Puedes hacer un simple bucle bash:

```bash
for i in {1..100}; do
  curl -s -X POST http://localhost:8001/login \
    -H "Content-Type: application/json" \
    -d '{"username":"admin", "password":"'"$i"'"}' > /dev/null
done
```
