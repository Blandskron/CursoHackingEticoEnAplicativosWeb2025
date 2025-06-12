### Archivo: `docker-compose.yml`

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
        ipv4_address: 192.168.10.1
      vlan20:
        ipv4_address: 192.168.20.1
      vlan30:
        ipv4_address: 192.168.30.1
      vlan40:
        ipv4_address: 192.168.40.1

  # ======================
  # CLIENTES VLAN 10 (ADMINISTRACIÓN)
  # ======================
  admin_pc:
    image: alpine
    container_name: admin_pc
    command: ["sh", "-c", "apk add iputils && sleep infinity"]
    networks:
      vlan10:
        ipv4_address: 192.168.10.10

  # ======================
  # CLIENTES VLAN 20 (DESARROLLO)
  # ======================
  dev_pc:
    image: alpine
    container_name: dev_pc
    command: ["sh", "-c", "apk add iputils && sleep infinity"]
    networks:
      vlan20:
        ipv4_address: 192.168.20.10

  # ======================
  # CLIENTES VLAN 30 (SOPORTE TÉCNICO)
  # ======================
  support_pc:
    image: alpine
    container_name: support_pc
    command: ["sh", "-c", "apk add iputils && sleep infinity"]
    networks:
      vlan30:
        ipv4_address: 192.168.30.10

  # ======================
  # SERVIDOR INTERNO VLAN 40
  # ======================
  server:
    image: alpine
    container_name: internal_server
    command: ["sh", "-c", "apk add iputils && sleep infinity"]
    networks:
      vlan40:
        ipv4_address: 192.168.40.10

# ======================
# DEFINICIÓN DE VLANs (Redes bridge de Docker)
# ======================
networks:

  vlan10:
    driver: bridge
    ipam:
      config:
        - subnet: 192.168.10.0/24

  vlan20:
    driver: bridge
    ipam:
      config:
        - subnet: 192.168.20.0/24

  vlan30:
    driver: bridge
    ipam:
      config:
        - subnet: 192.168.30.0/24

  vlan40:
    driver: bridge
    ipam:
      config:
        - subnet: 192.168.40.0/24
```

---

### 🔧 Comandos para aplicar políticas de red desde el contenedor `router`

1. Ingresa al contenedor:

```bash
docker exec -it router sh
```

2. Establece las reglas de `iptables` para segmentar tráfico:

```sh
# Política por defecto: bloquea el tráfico inter-VLAN
iptables -P FORWARD DROP

# Permitir tráfico de administración a todas las VLANs
iptables -A FORWARD -s 192.168.10.0/24 -j ACCEPT

# Bloquear tráfico entre Desarrollo y Soporte Técnico
iptables -A FORWARD -s 192.168.20.0/24 -d 192.168.30.0/24 -j DROP
iptables -A FORWARD -s 192.168.30.0/24 -d 192.168.20.0/24 -j DROP

# Permitir acceso a Servidores desde cualquier VLAN
iptables -A FORWARD -d 192.168.40.0/24 -j ACCEPT
```

3. (Opcional) Guardar reglas en un archivo:

```sh
iptables-save > /etc/iptables.rules
```

---

### Cómo levantar el laboratorio

```bash
docker compose up -d
```

Una vez levantado, puedes:

* Hacer `ping` entre contenedores.
* Probar rutas, simular tráfico y aplicar nuevas políticas.
* Añadir herramientas como `tcpdump`, `nmap`, `curl`, etc.
