from pydantic import BaseModel, Field
from datetime import datetime

class GastoBase(BaseModel):
    descricao:  str   = Field(..., min_length=1, max_length=200)
    valor:      float = Field(..., gt=0) 
    usuario_id: int

class GastoCriar(GastoBase):   
    pass

class GastoResposta(GastoBase):
    id:        int
    criado_em: datetime       

    model_config = {"from_attributes": True}