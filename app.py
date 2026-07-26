import matplotlib
matplotlib.use('Agg')  # Configura Matplotlib para rodar em servidores Headless (sem tela)

from flask import Flask, render_template_string, send_file
import io
import sys
import matplotlib.pyplot as plt
import pandas as pd

# Importa as estruturas e lógicas do seu projeto
try:
    from src.logic import *
    from src.sorting import *
    from src.structures import *
except ImportError:
    pass

app = Flask(__name__)

@app.route('/')
def index():
    # 1. Executa a lógica de captura do terminal para exibir o relatório impresso pelo seu código
    buffer = io.StringIO()
    sys.stdout = buffer
    
    try:
        import main
    except Exception as e:
        print(f"Execução do pipeline: {e}")
    finally:
        sys.stdout = sys.__stdout__
    
    log_saida = buffer.getvalue()

    # 2. Renderiza a página WEB completa com os relatórios e os gráficos gerados ao vivo
    html = f"""
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Intel Alimentar SLZ - Sistema Web</title>
        <style>
            body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; background: #0f172a; color: #f8fafc; margin: 0; padding: 24px; }}
            .max-width {{ max-width: 1100px; margin: 0 auto; }}
            h1 {{ color: #38bdf8; border-bottom: 2px solid #1e293b; padding-bottom: 12px; margin-top: 0; }}
            .card {{ background: #1e293b; border-radius: 8px; border: 1px solid #334155; padding: 20px; margin-bottom: 24px; }}
            .card h2 {{ color: #cbd5e1; margin-top: 0; font-size: 1.2rem; }}
            .terminal {{ background: #020617; color: #38edf8; font-family: 'Courier New', monospace; padding: 16px; border-radius: 6px; overflow-x: auto; white-space: pre-wrap; font-size: 13px; line-height: 1.6; border: 1px solid #0f172a; }}
            .grid {{ display: grid; grid-template-columns: 1fr; gap: 20px; }}
            @media (min-width: 768px) {{ .grid {{ grid-template-columns: 1fr 1fr; }} }}
            .chart-img {{ width: 100%; height: auto; border-radius: 6px; background: #fff; }}
        </style>
    </head>
    <body>
        <div class="max-width">
            <h1>🌾 Intel Alimentar SLZ</h1>
            <p style="color: #94a3b8;">Sistema de Inteligência e Análise de Vulnerabilidade Alimentar rodando em ambiente Serverless.</p>
            
            <div class="card">
                <h2>🖥️ Saída do Processamento de Algoritmos (main.py)</h2>
                <div class="terminal">{log_saida if log_saida.strip() else "Processamento concluído com sucesso."}</div>
            </div>

            <div class="grid">
                <div class="card">
                    <h2>📊 Análise de Vulnerabilidade Dinâmica</h2>
                    <img src="/grafico/vulnerabilidade" class="chart-img" alt="Gráfico de Vulnerabilidade">
                </div>
                <div class="card">
                    <h2>🌧️ Distribuição e Impacto Climatológico</h2>
                    <img src="/grafico/clima" class="chart-img" alt="Gráfico Clima">
                </div>
            </div>
        </div>
    </body>
    </html>
    """
    return render_template_string(html)

# Rota para gerar gráficos do Matplotlib em memória RAM (sem salvar em disco)
@app.route('/grafico/vulnerabilidade')
def gerar_grafico_vulnerabilidade():
    plt.figure(figsize=(6, 4))
    # Exemplo de geração dinâmica com matplotlib
    plt.bar(['Zona 1', 'Zona 2', 'Zona 3', 'Zona 4'], [85, 62, 40, 95], color=['#ef4444', '#f97316', '#eab308', '#dc2626'])
    plt.title('Índice de Vulnerabilidade por Zona (SLZ)')
    plt.ylabel('Score de Risco')
    plt.tight_layout()
    
    img = io.BytesIO()
    plt.savefig(img, format='png', dpi=100)
    img.seek(0)
    plt.close()
    return send_file(img, mimetype='image/png')

@app.route('/grafico/clima')
def gerar_grafico_clima():
    plt.figure(figsize=(6, 4))
    plt.plot(['Jan', 'Fev', 'Mar', 'Abr', 'Mai'], [220, 310, 450, 380, 200], marker='o', color='#0284c7', linewidth=2)
    plt.title('Precipitação Sazonal (mm)')
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    
    img = io.BytesIO()
    plt.savefig(img, format='png', dpi=100)
    img.seek(0)
    plt.close()
    return send_file(img, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)