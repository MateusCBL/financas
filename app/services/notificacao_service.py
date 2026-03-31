import httpx
from app.config import settings
import logging

logger = logging.getLogger(__name__)

async def enviar_alerta_gasto(telegram_id: str, descricao: str, valor: float):
    url = f"https://api.telegram.org/bot{settings.TELEGRAM_TOKEN}/sendMessage"
    mensagem = (
        f" *Novo Gasto Registrado!*\n\n"
        f" Descrição: {descricao}\n"
        f" Valor: R$ {valor:.2f}"
    )
    
    try:
        async with httpx.AsyncClient(timeout=5.0) as client:
            response = await client.post(url, json={
                "chat_id": telegram_id,
                "text": mensagem,
                "parse_mode": "Markdown"
            })
            response.raise_for_status()
    except httpx.TimeoutException:
        logger.warning(f"Timeout ao notificar usuário {telegram_id}")
    except httpx.HTTPStatusError as e:
        logger.error(f"Erro HTTP do Telegram: {e.response.status_code}")
    except Exception as e:
        logger.error(f"Erro inesperado ao enviar notificação: {e}")