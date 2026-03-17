import requests

def enviar_mensagem(texto):
    url = "http://localhost:5000/api/ia"
    dados = {"mensagem": texto}
    
    try:
        response = requests.post(url, json=dados)
        if response.status_code == 200:
            print(f"Resposta da IA: {response.json()['resposta']}")
        else:
            print("Erro na comunicação.")
    except Exception as e:
        print(f"Falha ao conectar: {e}")

if __name__ == "__main__":
    msg = input("Digite sua mensagem para a IA: ")
    enviar_mensagem(msg)
