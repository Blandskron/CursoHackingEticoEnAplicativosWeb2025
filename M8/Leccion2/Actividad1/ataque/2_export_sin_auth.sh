#!/bin/bash
# Exportar datos sin autenticación (caso 2)

curl -X GET http://localhost:8000/admin/users/export
