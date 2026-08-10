import os
from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)

# Usar PORT do ambiente (importante para deploy)
port = int(os.getenv('PORT', 5000))

@app.route('/health', methods=['GET'])
def health():
    return jsonify({
        "status": "ok",
        "timestamp": datetime.now().isoformat()
    })

@app.route('/generate-strategy', methods=['POST'])
def generate_strategy():
    data = request.get_json()
    
    tipo = data.get('tipo', 'email')
    objetivo = data.get('objetivo', 'aumentar conversoes')
    publico_alvo = data.get('publico_alvo', 'e-commerce')
    
    return jsonify({
        "criado_em": datetime.now().isoformat(),
        "estrategia": f"Estratégia de {tipo.upper()} para {objetivo}",
        "objetivo": objetivo,
        "orcamento_estimado": "$100-500",
        "passos": [
            f"Segmente sua lista de {publico_alvo}",
            "Crie subject lines persuasivas",
            "Personalize conteúdo por segmento",
            "Teste A/B diferentes versões",
            "Analise taxa de abertura e clique"
        ],
        "publico_alvo": publico_alvo,
        "sucesso": True,
        "timeline": "2-3 semanas",
        "tipo": tipo
    })

if __name__ == '__main__':
    # Muito importante: host='0.0.0.0' permite deploy
    app.run(host='0.0.0.0', port=port, debug=False)
