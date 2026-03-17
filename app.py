import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# Chave direta para teste definitivo
API_KEY = "AIzaSyBtXynF3yCcP1poBvD35KRFdOxnnQRllqM"
URL_GEMINI = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={API_KEY}"

@app.route('/api/ia', methods=['POST'])
def processar_ia():
    dados = request.json
    pergunta = dados.get('mensagem', '')
    
    payload = {"contents": [{"parts": [{"text": pergunta}]}]}
    
    try:
        # Faz a chamada real para o Google
        response = requests.post(URL_GEMINI, json=payload)
        res_json = response.json()
        
        # Mostra o que o Google respondeu no terminal do servidor
        print("\n--- RESPOSTA DO GOOGLE ---")
        print(res_json)
        print("--------------------------\n")

        if 'candidates' in res_json:
            texto_ia = res_json['candidates'][0]['content']['parts'][0]['text']
            return jsonify({"status": "sucesso", "resposta": texto_ia})
        else:
            return jsonify({"status": "erro", "detalhes": res_json})
            
    except Exception as e:
        return jsonify({"status": "erro", "detalhes": str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
