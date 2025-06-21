#!/bin/bash

# Activar el reenvío de IP
echo 1 > /proc/sys/net/ipv4/ip_forward

# Agregar rutas (opcional)
ip route add 192.168.1.0/26 dev eth0
ip route add 192.168.1.64/26 dev eth1
ip route add 192.168.1.128/26 dev eth2
ip route add 192.168.1.192/26 dev eth3

# Mostrar interfaces
ip a

# Mantener el contenedor vivo
tail -f /dev/null
