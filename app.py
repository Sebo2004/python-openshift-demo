from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Hola desde OpenShift</h1>"
    
@app.route("/api")
def api():
    return {"status": "ok"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
