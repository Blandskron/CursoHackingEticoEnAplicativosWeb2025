#!/bin/bash

echo "🧼 Limpiando entorno anterior..."
docker compose down -v
docker rm -f $(docker ps -aq) 2>/dev/null
docker network prune -f

echo "🚀 Levantando infraestructura con Docker Compose..."
docker compose up -d --build

echo "⏳ Esperando que los contenedores arranquen..."
sleep 5

echo "🔗 Conectando el router a las demás redes REALES..."
docker network connect laboratorio_finance_net router
docker network connect laboratorio_hr_net router
docker network connect laboratorio_prod_net router

sleep 2

echo "🏷️ Asignando IPs adicionales al router..."
docker exec router ip addr add 192.168.100.62/27 dev eth1
docker exec router ip addr add 192.168.100.94/27 dev eth2
docker exec router ip addr add 192.168.100.126/27 dev eth3

echo "✅ Router conectado a todas las subredes"

echo "🔍 Verificando conectividad desde el router a cada PC..."
docker exec router ping -c 2 192.168.100.10   # admin_pc
docker exec router ping -c 2 192.168.100.34   # finance_pc
docker exec router ping -c 2 192.168.100.66   # hr_pc
docker exec router ping -c 2 192.168.100.98   # prod_pc

echo "✅ Todos los pings desde el router fueron ejecutados."
