# Laboratorio “API observada y escaneada”

Este laboratorio levanta una API de ejemplo con **observabilidad completa** (métricas, logs y trazas) y un **escaneo automatizado** con ZAP. La idea es mostrar cómo se conectan las piezas y dónde ver cada resultado.

---

## Arquitectura (visión rápida)

```
[Cliente] ──HTTP──> [FastAPI]
                     │
                     ├─ /metrics ───> [Prometheus] ──> [Grafana (dashboard)]
                     │
                     ├─ Logs UDP(JSON) ──> [Logstash] ──> [Elasticsearch] ──> [Kibana]
                     │
                     └─ OpenTelemetry ──> [Jaeger]
                     
[ZAP] ──autorun(plan)──> Escanea la API y guarda reportes (HTML/XML) en ./zap-reports
```

---

## Servicios y qué hace cada uno

### 1) API (FastAPI)

* Endpoints de ejemplo:

  * `GET /` → responde 200 (salud básica del servicio).
  * `GET /public/health` → health público.
  * `GET /private/data` → requiere `Authorization: Bearer <token>` (demo).
  * `GET /private/admin` → fuerza un 403 (sin permiso).
* Seguridad (demo):

  * **JWT guard** muy básico (firma deshabilitada a propósito para laboratorio).
  * **Headers de seguridad** y **no-cache** aplicados por middleware.
  * `X-Correlation-Id` agregado a la respuesta para correlación.
* Observabilidad:

  * **Métricas Prometheus** con `prometheus_fastapi_instrumentator` en `GET /metrics`.
  * **Logs** en JSON por **UDP** a Logstash (latencia, ruta, método, status, cid).
  * **Trazas** OpenTelemetry exportadas a **Jaeger**.

### 2) Prometheus

* “Scrapea” la API en `/metrics`.
* Expone su UI en `http://localhost:9090` para explorar series y consultas.

### 3) Grafana

* Provisionado automáticamente con:

  * **Datasource** Prometheus.
  * **Dashboard**: `Secure API – KPIs y Observabilidad` (latencia p95, 5xx, 401 vs 403, RPS, etc.).
* UI: `http://localhost:3000` (credenciales por defecto de Grafana si no se cambiaron).

### 4) Logstash + Elasticsearch + Kibana (ELK)

* **Logstash** recibe logs **UDP JSON** de la API (puerto 5044/udp).
* **Elasticsearch** indexa esos eventos.
* **Kibana** permite explorarlos visualmente en `http://localhost:5601`.

### 5) Jaeger (tracing distribuido)

* Recibe las trazas exportadas por la API.
* UI en `http://localhost:16686` para ver spans, latencias y relaciones.

### 6) ZAP (automatizado)

* Contenedor que ejecuta **ZAP Automation Framework** con un **plan** predefinido.
* Hace un **spider** sobre la API, espera el análisis pasivo y **genera reportes**:

  * `./zap-reports/report.html`
  * `./zap-reports/report.xml`

---

## Estructura de carpetas

```
lab-sec-api/
├─ api/
│  ├─ main.py                 # API FastAPI (métricas, headers, auth demo)
│  ├─ logstash_logger.py      # Logger UDP JSON a Logstash
│  ├─ entrypoint.sh           # Arranque (opcional según tu imagen)
│  ├─ requirements.txt
│  ├─ .env / .env.example     # Variables (JWT_PUBLIC, LOGSTASH_HOST/PORT, JAEGER_*…)
│  └─ Dockerfile
├─ grafana/provisioning/
│  ├─ dashboards/dashboard.json
│  ├─ dashboards/provider.yml
│  └─ datasources/datasource.yml
├─ logstash/pipeline/
│  └─ logstash.conf           # Input UDP JSON → ES (y stdout)
├─ prometheus/
│  └─ prometheus.yml          # Scrape a la API (/metrics)
├─ zap-reports/
│  └─ plan.yml o plan.yaml    # Plan de ZAP (autorun) + reportes generados
└─ docker-compose.yml
```

> Nota: Asegúrate de que el nombre del plan de ZAP coincida con el usado en `docker-compose.yml` (por ejemplo, `plan.yaml`). Los reportes se escriben en esta misma carpeta.

---

## Puertos y rutas

| Servicio      | URL local / Puerto          | Comentario                                    |
| ------------- | --------------------------- | --------------------------------------------- |
| API           | `http://localhost:8000/`    | `/public/health`, `/private/data`, `/metrics` |
| Prometheus    | `http://localhost:9090`     | Explorar métricas                             |
| Grafana       | `http://localhost:3000`     | Dashboard provisionado                        |
| Elasticsearch | `http://localhost:9200`     | API de ES (sin seguridad en este lab)         |
| Kibana        | `http://localhost:5601`     | Explorar logs                                 |
| Jaeger        | `http://localhost:16686`    | Trazas/spans                                  |
| ZAP Reports   | `./zap-reports/report.html` | HTML generado en el host                      |

---

## Variables de entorno (API)

* `JWT_PUBLIC`: clave (demo) para decodificar JWT.
* `JAEGER_AGENT_HOST` / `JAEGER_AGENT_PORT`: destino de exportación de trazas.
* `LOGSTASH_HOST` / `LOGSTASH_PORT`: a dónde enviar logs UDP JSON (5044/udp por defecto).

*(Se cargan desde `api/.env` vía `env_file` en `docker-compose`).*

---

## Cómo levantar todo

```bash
# Desde la raíz (donde está docker-compose.yml)
docker compose up -d --build

# Verifica:
curl -s http://localhost:8000/public/health
# -> {"ok": true}

# (Opcional) Ver el plan de ZAP corriendo y crear reportes
docker compose logs -f zap-af
# Al finalizar: "Automation plan succeeded!"
# Reportes: ./zap-reports/report.html y report.xml
```

---

## Dónde ver “resultados”

* **Métricas & KPIs**: Grafana → dashboard “Secure API – KPIs y Observabilidad”.
  (Latencia p95 por endpoint, tasa de 5xx, 401 vs 403, RPS, etc.)
* **Logs**: Kibana → descubre índices de ES y filtra por `service: "secure-api-demo"` (si se agregó en Logstash).
* **Trazas**: Jaeger → busca servicio “Secure API Demo”, inspecciona spans y latencias.
* **Reportes de seguridad (pasivo)**: `zap-reports/report.html` (y XML).

---

## Comportamientos útiles para pruebas

* **401**: Llama `GET /private/data` sin `Authorization` → 401 (autenticación faltante).
* **403**: Llama `GET /private/admin` con o sin token → 403 (sin permiso).
* **Headers de seguridad**: Respuesta incluye `X-Content-Type-Options: nosniff`, `Cross-Origin-Opener-Policy: same-origin`, etc.
* **No cache**: Respuestas incluyen `Cache-Control: no-cache, no-store, must-revalidate`, etc.
* **/metrics**: Exporta contadores/histogramas para Prometheus.

---

## Consideraciones

* El guard JWT es **didáctico** (firma no verificada en modo demo).
* Los headers de seguridad y “no-store” se aplican en middleware global para que sean visibles en todo el flujo.
* Logstash usa **UDP** por simplicidad en el lab (cero backpressure); en producción podrías elegir TCP/HTTP.

---

## Problemas comunes

* **ZAP no genera reportes**: revisa que el plan montado en el volumen tenga el **mismo nombre** que el especificado en `command` (`plan.yaml` vs `plan.yml`), y que el directorio `./zap-reports/` exista en el host.
* **Grafana sin dashboard**: confirma la ruta de provisioning (`grafana/provisioning/…`) y que `datasource.yml` apunte a `http://prometheus:9090`.
* **Kibana vacío**: espera a que lleguen logs (haz algunas requests a la API). Crea el index pattern si hace falta.
