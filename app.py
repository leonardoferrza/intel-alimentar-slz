from flask import Flask, render_template_string
import io
import sys
import os

app = Flask(__name__)

@app.route('/')
def home():
    # Redireciona o stdout para capturar tudo o que o main.py imprime ao rodar
    buffer = io.StringIO()
    sys.stdout = buffer
    
    try:
        # Importa e executa o main.py do seu projeto em tempo real
        import main
        # Se o seu main tiver uma função principal (ex: main.run() ou main.executar()),
        # você pode chamá-la aqui se necessário.
    except Exception as e:
        print(f"Erro ao executar o projeto: {e}")
    finally:
        # Restaura a saída padrão do terminal
        sys.stdout = sys.__stdout__
    
    # Obtém o texto gerado pela execução do projeto
    saida_projeto = buffer.getvalue()
    
    html_content = f"""
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Intel Alimentar SLZ - Execução</title>
        <style>
            body {{ font-family: 'Courier New', Courier, monospace; background-color: #0d1117; color: #c9d1d9; margin: 0; padding: 20px; }}
            .container {{ max-width: 1000px; margin: 0 auto; }}
            h1 {{ font-family: Arial, sans-serif; color: #58a6ff; font-size: 22px; border-bottom: 1px solid #30363d; padding-bottom: 10px; }}
            .terminal {{ background-color: #161b22; border: 1px solid #30363d; border-radius: 6px; padding: 20px; overflow-x: auto; white-space: pre-wrap; font-size: 14px; line-height: 1.5; color: #7ee787; }}
            .status {{ font-family: Arial, sans-serif; font-size: 12px; color: #8b949e; margin-bottom: 15px; }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🌾 Intel Alimentar SLZ - Processamento de Dados</h1>
            <div class="status">⚡ Executado em tempo real via Serverless</div>
            <div class="terminal">{saida_projeto if saida_projeto.strip() else "O projeto foi executado, mas não gerou nenhuma saída de texto."}</div>
        </div>
    </body>
    </html>
    """
    return render_template_string(html_content)

if __name__ == '__main__':
    app.run(debug=True)