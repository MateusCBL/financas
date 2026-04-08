from fastapi import APIRouter, Depends, BackgroundTasks, HTTPException, status
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
    db: Session = Depends(get_db),
):
    # 1. Verifica se o usuário existe
    usuario = db.query(models.Usuario).filter(
        models.Usuario.id == gasto.usuario_id
    ).first()

    if not usuario:                          # ← NOVO: evita crash
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuário não encontrado.",
        )

    # 2. Salva o gasto
    db_gasto = models.Gasto(**gasto.model_dump())  # ← corrigido: model_dump()
    db.add(db_gasto)
    db.commit()
    db.refresh(db_gasto)

    # 3. Notifica em background só se tiver telegram_id
    if usuario.telegram_id:                  # ← NOVO: evita erro se campo vazio
        background_tasks.add_task(
            enviar_alerta_gasto,
            usuario.telegram_id,
            gasto.descricao,
            gasto.valor,
        )

    return {"mensagem": "Gasto registrado com sucesso!", "id": db_gasto.id}