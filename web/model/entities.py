from sqlalchemy import Column, Integer, String, Sequence, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import connector

class USUARIO(connector.Manager.Base):
    __tablename__ = 'USUARIO'
    usuario_id= Column(Integer, Sequence('usuario_id_seq'), primary_key=True)
    codigo = Column(String(50))
    nombre = Column(String(120))
    apellido = Column(String(120))
    contrasena =Column(String(120))