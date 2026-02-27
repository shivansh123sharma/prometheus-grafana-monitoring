from flask import Flask
from prometheus_client import Counter, Histogram, generate_latest
import time
import random

app = Flask(__name__)

REQUEST_COUNT = Counter(
    'app_request_count', 
    'Total HTTP Requests'
)

REQUEST_LATENCY = Histogram(
    'app_request_latency_seconds',
    'Request latency'
)

@app.route("/")
def home():
    REQUEST_COUNT.inc()
    start_time = time.time()
    
    time.sleep(random.uniform(0.1, 0.5))
    
    REQUEST_LATENCY.observe(time.time() - start_time)
    return "Flask App is Running!"

@app.route("/metrics")
def metrics():
    return generate_latest()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
