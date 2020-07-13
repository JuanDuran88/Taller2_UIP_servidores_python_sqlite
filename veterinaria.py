from db import *
from sqlalchemy import Column, Integer, String, ForeignKey, Float, Date
from sqlalchemy.orm import relationship

class Veterinaria(Base):
    __tablename__ = "veterinarias"
    codigo = Column(Integer, primary_key=True)
    descripcion = Column(String(200), nullable=False)

    # Relacion con cliente y mascota
    cliente_id = Column(Integer, ForeignKey('clientes.codigo'), nullable=False)
    mascota_id = Column(Integer, ForeignKey('mascotas.codigo'), nullable=False)

    # Indicamos las referencias a los modelos
    cliente = relationship('Cliente')
    mascota = relationship('Mascota')