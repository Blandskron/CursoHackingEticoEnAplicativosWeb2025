#!/usr/bin/env bash
set -euo pipefail
mkdir -p reports
docker run --rm -v "$(pwd)/../../:/src" -v "$(pwd)/reports:/reports" owasp/dependency-check:latest \
  --scan /src/backend \
  --format "HTML" \
  --out /reports \
  --project "PFM8-Backend"
echo "Reporte SCA en security-tools/dependency-check/reports"
