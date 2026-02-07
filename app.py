from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return """
    <html>
      <head>
        <title>OpenShift Demo</title>
        <style>
          body {
            font-family: Arial, sans-serif;
            background: #eef2f7;
            text-align: center;
            margin-top: 80px;
          }
          .box {
            background: white;
            padding: 30px;
            border-radius: 8px;
            width: 400px;
            margin: auto;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
          }
          button {
            padding: 12px 20px;
            margin-top: 20px;
            font-size: 16px;
            border: none;
            border-radius: 5px;
            background: #0066cc;
            color: white;
            cursor: pointer;
          }
          button:hover {
            background: #004c99;
          }
        </style>
      </head>
      <body>
        <div class="box">
          <h1>Ruta /</h1>
          <p>Página principal</p>
          <a href="/api"><button>Ir a /api</button></a>
        </div>
      </body>
    </html>
    """

@app.route("/api")
def api():
    return """
    <html>
      <head>
        <title>API</title>
        <style>
          body {
            font-family: Arial, sans-serif;
            background: #f7f7f7;
            text-align: center;
            margin-top: 80px;
          }
          .box {
            background: white;
            padding: 30px;
            border-radius: 8px;
            width: 400px;
            margin: auto;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
          }
          button {
            padding: 12px 20px;
            margin-top: 20px;
            font-size: 16px;
            border: none;
            border-radius: 5px;
            background: #28a745;
            color: white;
            cursor: pointer;
          }
          button:hover {
            background: #1e7e34;
          }
        </style>
      </head>
      <body>
        <div class="box">
          <h1>Ruta /api</h1>
          <p>Página secundaria</p>
          <a href="/"><button>Volver a /</button></a>
        </div>
      </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
