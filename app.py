from flask import Flask,jsonify

app=Flask(__name__)

@app.route("/")
def index():
    return"""
    <html>
    <head>
        <title>OpenShift Demo</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background: #eef2f7;
                text-align: center;
                margin-top: 60px;
            }
            .box {
                background: white;
                padding: 30px;
                border-radius: 8px;
                width: 420px;
                margin: auto;
                box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            }
            button {
                padding: 12px 18px;
                margin: 10px;
                font-size: 15px;
                cursor: pointer;
                border: none;
                border-radius: 5px;
                background: #0066cc;
                color: white;
            }
            button:hover {
                background: #004c99;
            }
            #result {
                margin-top: 20px;
                font-weight: bold;
                color: green;
            }
        </style>
    </head>
    <body>
        <div class="box">
            <h1>Ruta /</h1>
            <p>Interfaz principal</p>

            <button onclick="callApi()">Llamar /api</button>
            <br>
            <a href="/api"><button>Ir a /api</button></a>

            <div id="result"></div>
        </div>

        <script>
            function callApi() {
                fetch('/api/data')
                    .then(res => res.json())
                    .then(data => {
                        document.getElementById('result').innerText =
                            'Respuesta: ' + JSON.stringify(data);
                    });
            }
        </script>
    </body>
    </html>
    """

@app.route("/api")
def api():
    return"""
    <html>
    <head>
        <title>API Demo</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background: #f7f7f7;
                text-align: center;
                margin-top: 60px;
            }
            .box {
                background: white;
                padding: 30px;
                border-radius: 8px;
                width: 420px;
                margin: auto;
                box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            }
            button {
                padding: 12px 18px;
                margin: 10px;
                font-size: 15px;
                cursor: pointer;
                border: none;
                border-radius: 5px;
                background: #28a745;
                color: white;
            }
            button:hover {
                background: #1e7e34;
            }
            #result {
                margin-top: 20px;
                font-weight: bold;
                color: #333;
            }
        </style>
    </head>
    <body>
        <div class="box">
            <h1>Ruta /api</h1>
            <p>Interfaz secundaria</p>

            <button onclick="callRoot()">Llamar /</button>
            <br>
            <a href="/"><button>Volver a /</button></a>

            <div id="result"></div>
        </div>

        <script>
            function callRoot() {
                fetch('/')
                    .then(() => {
                        document.getElementById('result').innerText =
                            'Ruta / respondió correctamente';
                    });
            }
        </script>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)