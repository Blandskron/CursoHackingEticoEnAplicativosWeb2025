#!/bin/bash

echo "=============================="
echo "🔍 TEST DE CONECTIVIDAD"
echo "=============================="

echo ""
echo "📡 Desde router a cada PC:"
ping -c 2 10.100.10.10  # pc1
ping -c 2 10.100.20.10  # pc2
ping -c 2 10.100.30.10  # pc3
ping -c 2 10.100.40.10  # pc4

echo ""
echo "=============================="
echo "🔁 Test entre PCs (puede fallar sin rutas estáticas configuradas):"
echo "=============================="

echo ""
echo "pc1 -> pc2"
docker exec pc1 ping -c 2 10.100.20.10

echo ""
echo "pc2 -> pc3"
docker exec pc2 ping -c 2 10.100.30.10

echo ""
echo "pc3 -> pc4"
docker exec pc3 ping -c 2 10.100.40.10

echo ""
echo "pc4 -> pc1"
docker exec pc4 ping -c 2 10.100.10.10

echo ""
echo "✅ Pruebas finalizadas"
