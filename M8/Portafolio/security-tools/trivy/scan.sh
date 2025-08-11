#!/usr/bin/env bash
set -euo pipefail
# Construir imagen local del backend
docker build -t pfm8/backend:local ../../backend
# Escanear imagen con Trivy
docker run --rm -v /var/run/docker.sock:/var/run/docker.sock aquasec/trivy:latest image pfm8/backend:local
