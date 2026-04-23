from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.usuario_model import Usuario
from app.schemas.usuario_schema import UsuarioCriar, UsuarioResposta

router = APIRouter(prefix="/usuarios", tags=["Usuários"])

@router.post("/", response_model=UsuarioResposta, status_code=status.HTTP_201_CREATED)
def criar_usuario(usuario: UsuarioCriar, db: Session = Depends(get_db)):
    existente = db.query(Usuario).filter(
        Usuario.telegram_id == usuario.telegram_id
    ).first()

    if existente:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Telegram ID já cadastrado.",
        )

    novo_usuario = Usuario(**usuario.model_dump())  
    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)
    return novo_usuario