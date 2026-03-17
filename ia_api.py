import requests

API_KEY = open("segredos/api_key.txt").read().strip()

MODEL = "gemini-1.5-flash"

URL = f"https://generativelanguage.googleapis.com/v1/models/{MODEL}:generateContent?key={API_KEY}"


def perguntar(msg):

    payload = {
        "contents":[
            {
                "parts":[
                    {"text":msg}
                ]
            }
        ]
    }

    try:

        r = requests.post(URL, json=payload, timeout=30)

        if r.status_code != 200:
            print("Erro API:")
            print(r.text)
            return

        data = r.json()

        resposta = data["candidates"][0]["content"]["parts"][0]["text"]

        print("\nIA:", resposta)

    except Exception as e:
        print("Erro:", e)


print("🤖 Gemini Terminal")
print("Digite sair para encerrar\n")

while True:

    pergunta = input("Você: ")

    if pergunta.lower() == "sair":
        break

    perguntar(pergunta)