#!/bin/bash
# Detectar versión vulnerable de jQuery

echo "Verificando versión de jQuery cargada en frontend:"
curl -s http://localhost:5173 | grep jquery
