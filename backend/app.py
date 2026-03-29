from flask import Flask
import os
import time
import socket
import logging
app = Flask(__name__)

# pega variáveis do docker-compose
INSTANCE_ID = os.getenv("INSTANCE_ID", socket.gethostname())
DELAY = int(os.getenv("DELAY", 0))

# configura logs
logging.basicConfig(level=logging.INFO)

# endpoint principal
@app.route("/api/")
def api():
    time.sleep(DELAY)  # simula carga

    logging.info(f"Requisição atendida por {INSTANCE_ID}")

    return {
        "instance": INSTANCE_ID,
        "delay": DELAY
    }

# health check (usado pelo nginx/failover)
@app.route("/health")
def health():
    return {"status": "ok"}, 200

# métricas simples (requisito)
@app.route("/api/status")
def status():
    return {
        "instance": INSTANCE_ID,
        "status": "running",
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)