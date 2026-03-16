from fastapi import FastAPI
from app.database import engine, Base
from app.routes import usuarios_rotas, gastos_rotas

Base.metadata.create_all(bind=engine)
app = FastAPI(title="Sistema de Alerta Financeiro")

app.include_router(usuarios_rotas.router)
app.include_router(gastos_rotas.router)