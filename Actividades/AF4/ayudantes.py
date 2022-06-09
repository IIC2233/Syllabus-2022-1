from collections import namedtuple, defaultdict
from functools import reduce

Plato = namedtuple('nombre', 'nombre ingredientes')

class Ayudante:
    def __init__(self, nombre, platos, dinero):
        self.nombre = nombre
        self.platos = platos # lista con namedtuples de platos
        self.dinero = dinero

    def obtener_ingredientes_platos(self):
        # Completar
        pass

    def cantidad_ingredientes(self, lista_ingredientes_platos):
        # Completar
        pass
    
    def total_compra(self, ingredientes_platos, supermercado):
        # Completar
        pass
