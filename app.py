from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>🚀 My Azure Web App</title>
        <style>
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(to right, #0078D7, #00B4DB);
                color: white;
                text-align: center;
                padding: 80px;
            }
            h1 {
                font-size: 48px;
                margin-bottom: 20px;
            }
            p {
                font-size: 22px;
            }
            .card {
                background: rgba(255, 255, 255, 0.1);
                border-radius: 15px;
                padding: 30px;
                max-width: 600px;
                margin: 0 auto;
                box-shadow: 0 10px 25px rgba(0, 0, 0, 0.2);
            }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>✅ Deployed to Azure!</h1>
            <p>This Flask app is running on <strong>Azure App Service</strong> with GitHub Actions CI/CD.</p>
            <p>Edit <code>app.py</code> and push updates to GitHub or from VS Code.</p>
        </div>
    </body>
    </html>
    """
