#!/usr/bin/env bash
set -Eeuo pipefail

echo "===> PWD"
pwd
echo "===> Listado de /app"
ls -la

echo "===> Versiones:"
python - <<'PY'
import sys, importlib
print("Python", sys.version)
mods = ["fastapi", "uvicorn", "prometheus_fastapi_instrumentator",
        "prometheus_client", "jose", "opentelemetry", "opentelemetry.exporter.jaeger.thrift"]
for m in mods:
    try:
        importlib.import_module(m)
        print(m, "OK")
    except Exception as e:
        print(m, "FAIL:", e)
PY

echo "===> Test import main/app"
python - <<'PY'
import importlib
m = importlib.import_module("main")
app = getattr(m, "app", None)
print("main import OK:", m)
print("ASGI app present:", app is not None)
PY

echo "===> Lanzando Uvicorn"
exec uvicorn main:app --host 0.0.0.0 --port 8000 --log-level debug
