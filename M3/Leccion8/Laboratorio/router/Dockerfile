FROM ubuntu:22.04

RUN apt-get update && \
    apt-get install -y iproute2 iputils-ping net-tools bash && \
    apt-get clean

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

CMD ["/entrypoint.sh"]
