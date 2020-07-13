from db import *
from cliente import *
from mascota import *
from veterinaria import *
from dml import DML
import random

#if __name__ == '__main__':
 #   Base.metadata.create_all(engine)

  #  def __init__(self, codigo, direccion, telefono, cuentaBanco, mascota):
   #     self.codigo = codigo
    #    self.direccion = direccion
     #   self.telefono = telefono
      #  self.cuentaBanco = cuentaBanco
       # self.mascota = mascota

# jose = Cliente(dirccion="Panama", telefono="9999", cuentaBanco="123456", mascota="Firulai")

# user = Cliente(1,"Bella vista, Panama","222-5566","55566699","Bono Duran")
# session.add(user)
# session.commit()

def gen (lista):
    ''' Generador de item ''' 
    return random.choice(lista)

def cargaInformacion():
    # info temp
    _lnombres = ['Jose', 'Maria', 'Pedro', 'Karin', 'Camila']
    _lapellidos = ['Asprilla', 'Aguila', 'Zuñiga', 'Chef', 'Python', 'Rodriguez', 'Balboa']
    _lmascotas = ['Firulai', 'Zorro', 'Covid', 'Juanita', 'Jilio', 'Rambo', 'Consentido', 'Github', 'Jupyter']

    # Creamos Personas
    persona1 = Persona(nombre=gen(_lnombres), apellido=gen(_lapellidos))
    persona2 = Persona(nombre=gen(_lnombres), apellido=gen(_lapellidos))
    persona3 = Persona(nombre=gen(_lnombres), apellido=gen(_lapellidos))
    persona4 = Persona(nombre=gen(_lnombres), apellido=gen(_lapellidos))

    # Creamos clientes
    cliente1 = Cliente(persona=persona1, direccion='Panama City', telefono='1234555', cuentaBanco='8-10-232')
    cliente2 = Cliente(persona=persona2, direccion='Chiriqui', telefono='1234555', cuentaBanco='6-10-252')
    cliente3 = Cliente(persona=persona3, direccion='Los santos', telefono='1234555', cuentaBanco='4-10-222')
    cliente4 = Cliente(persona=persona4, direccion='Colon', telefono='1234555', cuentaBanco='2-10-202')

    # Agregamos los insert a la sesion
    session.add_all([persona1, persona2, persona3, persona4])
    # Ejecutamos la consulta
    session.commit()

    session.add_all([cliente1, cliente2, cliente3, cliente4])
    session.commit()

    # Creamos las mascotas
    mascota1 = Mascota(alias=gen(_lmascotas), especies='Doberman', raza='Original', colorPelo='Negro', peso=80, historial='Se porta bien')
    mascota2 = Mascota(alias=gen(_lmascotas), especies='Coker', raza='Original', colorPelo='Negro con blanco', peso=50, historial='Se porta muy mal')
    mascota3 = Mascota(alias=gen(_lmascotas))
    mascota4 = Mascota(alias=gen(_lmascotas))

    # Agregamos los insert de las mascotas
    session.add_all([mascota1, mascota2, mascota3, mascota4])
    session.commit()

    # Creamos el historial

    historia1 = Veterinaria(descripcion='Visita #1 con exito ', cliente=cliente1, mascota=mascota4)
    historia2 = Veterinaria(descripcion='Visita #1 se aplico las vacunas ', cliente=cliente2, mascota=mascota3)
    historia3 = Veterinaria(descripcion='Visita #1 se cortaron las uñas ', cliente=cliente3, mascota=mascota2)
    historia4 = Veterinaria(descripcion='Visita #1 se opero ', cliente=cliente4, mascota=mascota1)
    historia5 = Veterinaria(descripcion='Visita #2 se le realizo limpienza ', cliente=cliente1, mascota=mascota2)
    historia6 = Veterinaria(descripcion='Visita #3 se alimento ', cliente=cliente3, mascota=mascota2)
    historia7 = Veterinaria(descripcion='Visita #4 se murio ', cliente=cliente4, mascota=mascota3)

    # Creamos informacion
    session.add_all([historia1, historia2, historia3, historia4, historia5, historia6, historia7])
    session.commit()

if __name__ == '__main__':
    # Creamos nuestras clases en tablas
    Base.metadata.create_all(engine)

    # Carga inicial de informacion
    cargaInformacion()

    # Consultando la información con un DML
    dml = DML()

    # impresion de todo los clientes
    #dml.getCliente()

    # impresion de todas las mascotas
    #dml.getMascotas()

    # impresion de historia con join
    dml.getVisitasVeterinaria()

    # Consultas universales
    # dml.getUniversal(Persona)
    # dml.getUniversal(Mascota)
    # dml.getUniversal(Veterinaria)
