from sqlalchemy import Column, Integer, String, Float, ForeignKey
from app.database import Base

class Gasto(Base):
    __tablename__ = "gastos"
    id = Column(Integer, primary_key=True, index=True)
    descricao = Column(String)
    valor = Column(Float)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))