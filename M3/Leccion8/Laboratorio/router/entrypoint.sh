#!/bin/bash
# Habilitar el reenvío de paquetes entre interfaces
sysctl -w net.ipv4.ip_forward=1

# Activar NAT (si se quiere salir hacia internet real más adelante)
# iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE

# Mantener contenedor activo
tail -f /dev/null
