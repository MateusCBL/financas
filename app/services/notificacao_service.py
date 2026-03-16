import requests

class NotificacaoService:
    @staticmethod
    def enviar_telegram(token_bot: str, chat_id: str, mensagem: str):
        url = f"https://api.telegram.org/bot{token_bot}/sendMessage"
        dados = {"chat_id": chat_id, "text": mensagem, "parse_mode": "Markdown"}
        try:
            requests.post(url, data=dados)
        except Exception as e:
            print(f"Erro ao enviar: {e}")