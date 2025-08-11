README.md
md
Copiar
Editar
# Proyecto Final de Módulo 8 – Laboratorio completo

## Levantar
```bash
docker compose up -d
API: http://localhost:8000/docs

Prometheus: http://localhost:9090

Grafana: http://localhost:3000 (admin/admin)

SonarQube: http://localhost:9000 (crear token y usarlo en CI)

Flujo sugerido
Diagnóstico inicial: Sonar (SAST), Dependency-Check (SCA), Trivy (contenedor), ZAP (DAST).

Pipeline CI/CD (GitHub Actions) con gates y reportes.

Métricas: Prometheus + Grafana (latencias, 5xx, RPS).

Mitigación: endurecer CORS, auth, validaciones, manejo de errores.

Pentest posterior: comparar hallazgos.

KPI de ejemplo
Rate de 5xx = 5xx_total / requests_total (Prometheus).

MTTR vulns = tiempo cierre - tiempo apertura (gestión issues).

Vulns abiertas por severidad (SAST/SCA).

% builds fallados por seguridad (CI).

Endpoints rápidos
GET /health (para pipelines / monitoreo)

POST /auth/login (inseguro por diseño)

CRUD /clients (vulnerabilidades controladas para práctica)

GET /search?q= (reflected XSS para práctica)

Advertencia: no expongas este entorno vulnerable a Internet real.