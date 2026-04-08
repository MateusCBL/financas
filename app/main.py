from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.database import engine, Base
from app.routes import usuarios_rotas, gastos_rotas


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine) 
    yield


app = FastAPI(
    title="Sistema de Alerta Financeiro",
    description="API para registro de gastos com notificações via Telegram.",
    version="1.0.0",
    lifespan=lifespan, 
)

app.include_router(
    usuarios_rotas.router,
    prefix="/usuarios",
    tags=["Usuários"],
)

app.include_router(
    gastos_rotas.router,
    prefix="/gastos",
    tags=["Gastos"],
)