from flask import Flask, render_template_string
import os

app = Flask(__name__)

@app.route('/')
def home():
    html_content = """
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <title>Intel Alimentar SLZ</title>
        <style>
            body { font-family: Arial, sans-serif; background-color: #f4f6f8; margin: 0; padding: 40px; color: #333; }
            .container { max-width: 800px; margin: 0 auto; background: white; padding: 30px; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); }
            h1 { color: #2c3e50; }
            p { font-size: 16px; line-height: 1.6; }
            .badge { background: #27ae60; color: white; padding: 5px 10px; border-radius: 4px; font-weight: bold; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🌾 Intel Alimentar SLZ</h1>
            <p>Status do Sistema: <span class="badge">ONLINE</span></p>
            <p>Plataforma de Inteligência e Análise de Vulnerabilidade Alimentar de São Luís rodando via Serverless na Vercel.</p>
        </div>
    </body>
    </html>
    """
    return render_template_string(html_content)

if __name__ == '__main__':
    app.run(debug=True)

app = app.wsgi_app