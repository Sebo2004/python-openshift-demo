from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def index():
    return {
        "app": "python-openshift-demo",
        "status": "running",
        "pod": os.getenv("HOSTNAME", "unknown")
    }

@app.route("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
