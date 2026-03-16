# Sistema de Alerta Financeiro
API Python com FastAPI que notifica gastos via Telegram.

## Como rodar:
1. Instale as dependências: `pip install -r requirements.txt`
2. Configure seu Token do Bot no arquivo `app/routes/gastos_rotas.py`.
3. Rode o servidor: `uvicorn app.main:app --reload`
4. Acesse `http://127.0.0.1:8000/docs` para testar.