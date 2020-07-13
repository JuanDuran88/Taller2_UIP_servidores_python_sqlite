from db import *

from cliente import Cliente
from mascota import Mascota
from veterinaria import Veterinaria

class DML():
    """ Clase manejo de consulta de datos """ 
    def getCliente(self):
        query =  session.query(Cliente)
        print('____IMPRESION DE DATOS DE CLIENTES____')
        # el objeto __dict__ permite imprimir las claves valor de la consulta
        # De igual forma uno puede especificar un campo especifico que desee
        for data in query.all():
            print(data.__dict__)
        print('\n_____________________________________\n')

    def getMascotas(self):
        query = session.query(Mascota)
        print('____IMPRESION DE DATOS DE LAS MASCOTAS____')
        for data in query.all():
            print(data.__dict__)
        print('\n_________________________________\n')

    def getVisitasVeterinaria(self):
        # Consultando las tablas relacionadas y realizamos un join
        query = session.query(Veterinaria, Cliente, Mascota)\
            .join(Cliente, Cliente.codigo == Veterinaria.cliente_id)\
            .join(Mascota, Mascota.codigo == Veterinaria.mascota_id)\
            .all()
        print('_____IMPRESION DE HISTORIA_____')
        for data in query:
            for item in data:
                print(item.__dict__)
            print()

        print('\n_______________________________\n')

    def getUniversal(self, Modelo):
        query = session.query(Modelo)
        print('\n_____IMPRESION DE UNIVERSAL {0}_____'.format(Modelo))
        for data in query.all():
            print(data.__dict__)
        print('\n___________FIN__________\n')
