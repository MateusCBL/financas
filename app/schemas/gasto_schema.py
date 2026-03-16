from pydantic import BaseModel

class GastoBase(BaseModel):
    descricao: str
    valor: float
    usuario_id: int

class GastoCreate(GastoBase):
    pass

class GastoResponse(GastoBase):
    id: int
    class Config:
        from_attributes = True