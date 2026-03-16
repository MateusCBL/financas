from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.gasto_model import Gasto
from app.models.usuario_model import Usuario
from app.schemas.gasto_schema import GastoCreate, GastoResponse
from app.services.notificacao_service import NotificacaoService

router = APIRouter(prefix="/gastos", tags=["Gastos"])
TOKEN_TELEGRAM = "SEU_TOKEN_AQUI" # Configure aqui

@router.post("/", response_model=GastoResponse)
def registrar_gasto(gasto: GastoCreate, db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.id == gasto.usuario_id).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    
    novo_gasto = Gasto(**gasto.dict())
    db.add(novo_gasto)
    db.commit()
    db.refresh(novo_gasto)
    
    msg = f"🔔 *Alerta Financeiro*\n\nNovo gasto de *R$ {novo_gasto.valor:.2f}* registrado: {novo_gasto.descricao}"
    NotificacaoService.enviar_telegram(TOKEN_TELEGRAM, usuario.telegram_id, msg)
    
    return novo_gasto