from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>🔷 Azure App Service Demo</title>
        <style>
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(to right, #2C7BE5, #1E90FF);
                color: white;
                margin: 0;
                padding: 0;
                height: 100vh;
                display: flex;
                align-items: center;
                justify-content: center;
            }
            .card {
                background: rgba(255, 255, 255, 0.1);
                padding: 40px;
                border-radius: 20px;
                text-align: center;
                box-shadow: 0 8px 30px rgba(0,0,0,0.3);
                max-width: 600px;
            }
            h1 {
                font-size: 40px;
                margin-bottom: 20px;
                color: #ffffff;
            }
            p {
                font-size: 20px;
                line-height: 1.6;
                color: #e0e0e0;
            }
            .footer {
                margin-top: 30px;
                font-size: 16px;
                color: #dddddd;
                border-top: 1px solid rgba(255,255,255,0.2);
                padding-top: 15px;
            }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>✅ Azure Deployment Success</h1>
            <p>This Flask app is live on <strong>Azure App Service</strong>.</p>
            <p>Deployed using <strong>GitHub Actions</strong> CI/CD pipeline.</p>
            <div class="footer">
                👤 Venkatesh<br>
                📞 +91-9876543210
            </div>
        </div>
    </body>
    </html>
    """

