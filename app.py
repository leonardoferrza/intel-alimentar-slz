from flask import Flask, render_template_string, send_from_directory
import os

app = Flask(__name__)

# Rota para servir as imagens salvas na pasta assets (mapas e gráficos)
@app.route('/assets/<path:filename>')
def serve_assets(filename):
    return send_from_directory('assets', filename)

@app.route('/')
def home():
    html_content = """
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Intel Alimentar SLZ</title>
        <style>
            body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #f4f6f8; margin: 0; padding: 20px; color: #333; }
            .container { max-width: 1000px; margin: 0 auto; background: white; padding: 30px; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.08); }
            h1 { color: #1e3c72; margin-bottom: 5px; }
            p.sub { color: #666; margin-top: 0; font-size: 1.05rem; }
            .grid { display: grid; grid-template-columns: 1fr; gap: 25px; margin-top: 30px; }
            @media (min-width: 768px) { .grid { grid-template-columns: 1fr 1fr; } }
            .card { background: #fff; border: 1px solid #e1e8ed; border-radius: 8px; padding: 15px; box-shadow: 0 2px 4px rgba(0,0,0,0.04); }
            .card h3 { margin-top: 0; color: #2c3e50; border-bottom: 2px solid #3498db; padding-bottom: 8px; }
            .card img { width: 100%; height: auto; border-radius: 6px; }
            .full-width { grid-column: 1 / -1; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🌾 Intel Alimentar SLZ</h1>
            <p class="sub">Plataforma de Inteligência e Análise de Vulnerabilidade Alimentar de São Luís</p>
            
            <div class="grid">
                <div class="card">
                    <h3>🗺️ Mapa de Calor de Vulnerabilidade</h3>
                    <img src="/assets/mapa-de-calor-de-vulnerabilidade.png" alt="Mapa de Calor">
                </div>
                
                <div class="card">
                    <h3>📊 Análise Estatística</h3>
                    <img src="/assets/analise-estatistica.png" alt="Análise Estatística">
                </div>
                
                <div class="card full-width">
                    <h3>📋 Plano de Ação Prioritário</h3>
                    <img src="/assets/plano-de-acao-prioritario.png" alt="Plano de Ação">
                </div>
            </div>
        </div>
    </body>
    </html>
    """
    return render_template_string(html_content)

if __name__ == '__main__':
    app.run(debug=True)