from fastapi import APIRouter, Depends, BackgroundTasks
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.gasto_schema import GastoCriar
from app.services.notificacao_service import enviar_alerta_gasto
from app import models

router = APIRouter()

@router.post("/gastos/")
async def criar_gasto(
    gasto: GastoCriar,
    background_tasks: BackgroundTasks,  
    db: Session = Depends(get_db)
):

    usuario = db.query(models.Usuario).filter(
        models.Usuario.id == gasto.usuario_id
    ).first()

    db_gasto = models.Gasto(**gasto.dict())
    db.add(db_gasto)
    db.commit()
    db.refresh(db_gasto)

    background_tasks.add_task(
        enviar_alerta_gasto,
        usuario.telegram_id,
        gasto.descricao,
        gasto.valor
    )

    return {"mensagem": "Gasto registrado com sucesso!", "id": db_gasto.id}