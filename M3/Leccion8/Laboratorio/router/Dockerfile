FROM debian:stable-slim

RUN apt update && apt install -y iproute2 iputils-ping net-tools vlan

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
