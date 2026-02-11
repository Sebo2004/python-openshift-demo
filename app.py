import os
from flask import Flask, jsonify, render_template_string

app = Flask(__name__)

# =========================
# Configuración desde entorno
# =========================

APP_NAME = os.getenv("APP_NAME", "OpenShift Demo App")
APP_ENV = os.getenv("APP_ENV", "Producción" if os.getenv("APP_ENV") == "prod" else "Desarrollo")
APP_VERSION = os.getenv("APP_VERSION", "1.0.0")
API_KEY = os.getenv("API_KEY", None)
DATA_PATH = os.getenv("DATA_PATH", "/tmp/data")
DATA_FILE = f"{DATA_PATH}/visits.txt"

# =========================
# Estilos CSS Reutilizables
# =========================

BASE_STYLE = """
<style>
    :root {
        --primary: #4a90e2;
        --secondary: #f39c12;
        --success: #2ecc71;
        --danger: #e74c3c;
        --dark: #2c3e50;
        --light: #ecf0f1;
    }
    body {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        background: #f0f2f5;
        color: var(--dark);
        margin: 0;
        display: flex;
        flex-direction: column;
        align-items: center;
        min-height: 100vh;
    }
    nav {
        background: var(--dark);
        width: 100%;
        padding: 1rem 0;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 2px 5px rgba(0,0,0,0.2);
    }
    nav a {
        color: white;
        text-decoration: none;
        margin: 0 15px;
        font-weight: bold;
        transition: 0.3s;
    }
    nav a:hover { color: var(--secondary); }
    .container {
        background: white;
        padding: 2rem;
        border-radius: 12px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.1);
        width: 90%;
        max-width: 500px;
        text-align: center;
    }
    .badge {
        padding: 5px 12px;
        border-radius: 20px;
        font-size: 0.8rem;
        color: white;
        font-weight: bold;
    }
    .bg-env { background: var(--primary); }
    .bg-ver { background: var(--secondary); }
    .bg-status { background: var(--success); }
    .card {
        background: #f8f9fa;
        border-left: 5px solid var(--primary);
        margin: 1rem 0;
        padding: 1rem;
        text-align: left;
    }
    .btn {
        display: inline-block;
        padding: 10px 20px;
        background: var(--primary);
        color: white;
        text-decoration: none;
        border-radius: 5px;
        margin-top: 10px;
        transition: 0.3s;
    }
    .btn:hover { opacity: 0.8; }
</style>
"""

LAYOUT = f"""
<!DOCTYPE html>
<html>
<head>
    <title>{APP_NAME}</title>
    {BASE_STYLE}
</head>
<body>
    <nav>
        <a href="/">Inicio</a>
        <a href="/api">API Data</a>
        <a href="/info">Info</a>
        <a href="/health">Health</a>
    </nav>
    <div class="container">
        {{{{ content | safe }}}}
    </div>
</body>
</html>
"""

# =========================
# Utilidades
# =========================

def ensure_data_path():
    try:
        os.makedirs(DATA_PATH, exist_ok=True)
        if not os.path.exists(DATA_FILE):
            with open(DATA_FILE, "w") as f:
                f.write("0")
        return True
    except Exception:
        return False

def increment_visits():
    try:
        ensure_data_path()
        with open(DATA_FILE, "r+") as f:
            content = f.read().strip()
            count = int(content) if content else 0
            count += 1
            f.seek(0)
            f.write(str(count))
            f.truncate()
        return count
    except Exception:
        return None

# =========================
# Rutas con Interfaz
# =========================

@app.route("/")
def index():
    visits = increment_visits()
    content = f"""
        <h1>{APP_NAME}</h1>
        <p>Bienvenido al panel de control principal.</p>
        <div style="font-size: 3rem;"></div>
        <p>Visitas detectadas: <b style="color:var(--primary); font-size: 1.5rem;">{visits if visits is not None else "Error de PVC"}</b></p>
        <hr>
        <p><span class="badge bg-env">{APP_ENV}</span> <span class="badge bg-ver">v{APP_VERSION}</span></p>
    """
    return render_template_string(LAYOUT, content=content)

@app.route("/api")
def api_view():
    secret_status = "✅ Configurado" if API_KEY else "❌ No configurado"
    content = f"""
        <h2>Datos de la API</h2>
        <div class="card">
            <p><b>Nombre:</b> {APP_NAME}</p>
            <p><b>Entorno:</b> {APP_ENV}</p>
            <p><b>Secreto:</b> {secret_status}</p>
        </div>
        <a href="/api/raw" class="btn" target="_blank">Ver JSON Crudo</a>
    """
    return render_template_string(LAYOUT, content=content)

@app.route("/api/raw")
def api_raw():
    return jsonify({"app": APP_NAME, "env": APP_ENV, "version": APP_VERSION, "secret_configured": API_KEY is not None})

@app.route("/info")
def info():
    content = f"""
        <h2>Información del Sistema</h2>
        <div class="card" style="border-left-color: var(--secondary);">
            <p><b>Ruta de Datos:</b> <code>{DATA_PATH}</code></p>
            <p><b>Versión:</b> {APP_VERSION}</p>
            <p><b>Host:</b> 0.0.0.0:8080</p>
        </div>
        <p>Esta aplicación está diseñada para demostrar persistencia y configuración en OpenShift/K8s.</p>
    """
    return render_template_string(LAYOUT, content=content)

@app.route("/health")
def health():
    pvc_ok = ensure_data_path()
    status_color = "var(--success)" if pvc_ok else "var(--danger)"
    content = f"""
        <h2>Estado del Sistema</h2>
        <div style="font-size: 4rem; color: {status_color};">●</div>
        <p><b>Health Check:</b> UP</p>
        <p><b>Persistencia (PVC):</b> {"Conectado" if pvc_ok else "Error"}</p>
        <a href="/" class="btn">Reintentar</a>
    """
    return render_template_string(LAYOUT, content=content)

# =========================
# Main
# =========================

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)