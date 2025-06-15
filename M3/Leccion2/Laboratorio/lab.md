### Archivo completo `docker-compose.yml` actualizado

```yaml
version: "3.9"

services:

  # ======================
  # ROUTER / FIREWALL
  # ======================
  router:
    image: alpine
    container_name: router
    command: ["sh", "-c", "apk add iptables iproute2 iputils && sleep infinity"]
    privileged: true  # Necesario para usar iptables dentro del contenedor
    networks:
      vlan10:
        ipv4_address: 192.168.110.254

  # ======================
  # CLIENTES VLAN 10 (ADMINISTRACIÓN)
  # ======================
  admin_pc:
    image: alpine
    container_name: admin_pc
    command: ["sh", "-c", "apk add iputils && sleep infinity"]
    networks:
      vlan10:
        ipv4_address: 192.168.110.10

  # ======================
  # CLIENTES VLAN 20 (DESARROLLO)
  # ======================
  dev_pc:
    image: alpine
    container_name: dev_pc
    command: ["sh", "-c", "apk add iputils && sleep infinity"]
    networks:
      vlan20:
        ipv4_address: 192.168.120.10

  # ======================
  # CLIENTES VLAN 30 (SOPORTE TÉCNICO)
  # ======================
  support_pc:
    image: alpine
    container_name: support_pc
    command: ["sh", "-c", "apk add iputils && sleep infinity"]
    networks:
      vlan30:
        ipv4_address: 192.168.130.10

  # ======================
  # SERVIDOR INTERNO VLAN 40
  # ======================
  server:
    image: alpine
    container_name: internal_server
    command: ["sh", "-c", "apk add iputils && sleep infinity"]
    networks:
      vlan40:
        ipv4_address: 192.168.140.10

# ======================
# DEFINICIÓN DE VLANs (Redes bridge de Docker)
# ======================
networks:

  vlan10:
    driver: bridge
    ipam:
      config:
        - subnet: 192.168.110.0/24

  vlan20:
    driver: bridge
    ipam:
      config:
        - subnet: 192.168.120.0/24

  vlan30:
    driver: bridge
    ipam:
      config:
        - subnet: 192.168.130.0/24

  vlan40:
    driver: bridge
    ipam:
      config:
        - subnet: 192.168.140.0/24
```

---

### Conecta el `router` a las demás redes

Después de levantar con:

```bash
docker compose up -d
```

Ejecuta:

```bash
docker network connect --ip 192.168.120.254 laboratorio_vlan20 router
docker network connect --ip 192.168.130.254 laboratorio_vlan30 router
docker network connect --ip 192.168.140.254 laboratorio_vlan40 router
```

---

### Configura reglas de `iptables` desde dentro del router

```bash
docker exec -it router sh
```

Y dentro:

```sh
# Política por defecto: bloquear tráfico entre contenedores
iptables -P FORWARD DROP

# Permitir administración a todas las VLANs
iptables -A FORWARD -s 192.168.110.0/24 -j ACCEPT

# Bloquear tráfico entre Desarrollo y Soporte Técnico
iptables -A FORWARD -s 192.168.120.0/24 -d 192.168.130.0/24 -j DROP
iptables -A FORWARD -s 192.168.130.0/24 -d 192.168.120.0/24 -j DROP

# Permitir acceso a servidor interno desde todas las VLANs
iptables -A FORWARD -d 192.168.140.0/24 -j ACCEPT
```

---

### (Opcional) Guardar las reglas:

```sh
iptables-save > /etc/iptables.rules
```

Excelente idea. Puedes agregar un **comando final de diagnóstico** para verificar fácilmente que tu laboratorio quedó bien configurado y que las reglas de `iptables` están aplicadas como esperas.

---

### Mostrar el estado general del router

Dentro del contenedor `router`, ejecuta estos comandos:

```sh
# Mostrar interfaces de red y sus IPs
ip a

# Mostrar tabla de rutas del router
ip route

# Mostrar reglas activas de iptables
iptables -L -v --line-numbers
```
