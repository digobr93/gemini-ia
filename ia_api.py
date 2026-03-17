import requests
import json

def comunicar_gemini(mensagem):
    api_key = "SUA_CHAVE_AQUI"
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"
    
    headers = {'Content-Type': 'application/json'}
    payload = {
        "contents": [{
            "parts": [{"text": mensagem}]
        }]
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))
    
    if response.status_code == 200:
        return response.json()['candidates'][0]['content']['parts'][0]['text']
    else:
        return f"Erro: {response.status_code} - {response.text}"

if __name__ == "__main__":
    texto = input("Digite a mensagem: ")
    print(comunicar_gemini(texto))
