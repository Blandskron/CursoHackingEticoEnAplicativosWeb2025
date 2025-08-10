import json, logging, os, socket

class UDPJSONLogstashHandler(logging.Handler):
    def __init__(self, host=None, port=None):
        super().__init__()
        self.addr = (host or os.getenv("LOGSTASH_HOST","logstash"),
                     int(port or os.getenv("LOGSTASH_PORT","5044")))
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def emit(self, record):
        try:
            payload = record.msg if isinstance(record.msg, dict) else {"message": str(record.msg)}
            self.sock.sendto(json.dumps(payload).encode("utf-8"), self.addr)
        except Exception:
            self.handleError(record)

def build_logger():
    logger = logging.getLogger("api")
    logger.setLevel(logging.INFO)
    if not logger.handlers:
        logger.addHandler(UDPJSONLogstashHandler())
    return logger
