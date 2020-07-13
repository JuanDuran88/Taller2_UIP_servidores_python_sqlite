from db import *
from sqlalchemy import Column, String, ForeignKey, Float, Date
from sqlalchemy.orm import relationship

from veterinaria import Veterinaria

class Mascota(Base):
    __tablename__ = "mascotas"
    codigo = Column(Integer, primary_key=True)
    alias = Column(String(30))
    especies = Column(String(30))
    raza = Column(String(30))
    colorPelo = Column(String(30))
    fechaNacimiento = Column(Date())
    peso = Column(Float)
    historial = Column(String(50))
    calendario = Column(Date())

    # Relación con veterinaria
    veterinaria = relationship(Veterinaria, backref='veterinarias')