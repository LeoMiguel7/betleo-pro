
import requests
import time
from config import TELEGRAM_TOKEN, TELEGRAM_CHAT_ID

def enviar_mensagem(mensagem):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": mensagem,
        "parse_mode": "HTML"
    }
    try:
        requests.post(url, data=payload)
    except Exception as e:
        print("Erro ao enviar mensagem:", e)

def rodar_bot():
    while True:
        try:
            mensagem = "⚽ Bot BET LÉO está rodando e pronto para enviar sinais!"
            enviar_mensagem(mensagem)
            time.sleep(3600)
        except Exception as erro:
            print("Erro no loop principal:", erro)
            time.sleep(60)

if __name__ == "__main__":
    rodar_bot()
