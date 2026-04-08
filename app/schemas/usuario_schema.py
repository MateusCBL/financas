from pydantic import BaseModel, Field

class UsuarioBase(BaseModel):
    nome:        str = Field(..., min_length=2, max_length=100)
    telegram_id: str = Field(..., min_length=5, max_length=50)

class UsuarioCriar(UsuarioBase):
    pass

class UsuarioResposta(UsuarioBase):
    id: int

    model_config = {"from_attributes": True}