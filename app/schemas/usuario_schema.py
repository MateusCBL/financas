from pydantic import BaseModel

class UsuarioBase(BaseModel):
    nome: str
    telegram_id: str

class UsuarioCreate(UsuarioBase):
    pass

class UsuarioResponse(UsuarioBase):
    id: int
    class Config:
        from_attributes = True