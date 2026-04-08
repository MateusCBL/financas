from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.sql import func
from app.database import Base

class Gasto(Base):
    __tablename__ = "gastos"

    id          = Column(Integer, primary_key=True, index=True)
    descricao   = Column(String(200), nullable=False)           
    valor       = Column(Float, nullable=False)                 
    usuario_id  = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    criado_em   = Column(DateTime, server_default=func.now())   