from collections import deque, namedtuple
from typing import Deque
from Parte1.fila_pizzas import Cliente, FilaPizza
from Parte1.lectura_archivos_parte1 import leer_archivo_eventos
from parametros import ARCHIVO_EVENTOS

Event = namedtuple("Event", "id tipo datos")

class CreadorPizzeria:
    # NO MODIFICAR
    def __init__(self, ruta_archivo_eventos: str):
        # NO MODIFICAR
        self.ruta_archivo_eventos = ruta_archivo_eventos
    
    def crear_pizzeria(self):
        # NO MODIFICAR
        eventos = leer_archivo_eventos(self.ruta_archivo_eventos)
        cola_eventos: Deque[Event] = deque()

        for id, tipo, datos in eventos:
            cola_eventos.append(Event(id=id, tipo=tipo, datos=datos))

        fila_pizza = FilaPizza()
        
        pizzeria = Pizzeria(fila_pizza, cola_eventos)
        return pizzeria

class Pizzeria:
    # NO MODIFICAR
    def __init__(self, fila: FilaPizza, cola_eventos: Deque[Event]):
        # NO MODIFICAR
        self.fila = fila
        self.cola_eventos = cola_eventos
        self.pizzas_compradas = 0

    @property
    def tiene_siguiente_evento(self):
        # NO MODIFICAR
        return bool(self.cola_eventos)

    def procesar_siguiente_evento(self):
        # NO MODIFICAR
        if self.tiene_siguiente_evento:
            next_event = self.cola_eventos.popleft()
            self.procesar_evento(next_event)

    def procesar_evento(self, evento: Event):
        # NO MODIFICAR
        if evento.tipo == "llega_cliente":
            nombre, = evento.datos
            cliente = Cliente(nombre)
            self.fila.llega_cliente(cliente)
            print(f"Llega {nombre} a la fila")

        elif evento.tipo == "se_cuela":
            nombre, posicion = evento.datos
            cliente = Cliente(nombre)
            self.fila.alguien_se_cuela(cliente, int(posicion))
            print(f"Se cuela {nombre} en la posición {posicion} de la fila")

        elif evento.tipo == "atendido":
            pizza, = evento.datos
            cliente = self.fila.cliente_atendido()
            print(f"El primer cliente de la fila ({cliente}) fue atendido y compró {pizza} pizzas")
            self.pizzas_compradas += int(pizza)
        print(self.fila)
        print()

if __name__ == "__main__":
    print("\nNO DEBES EJECUTAR AQUÍ EL PROGRAMA!!!!")
    print("Ejecuta el main.py\n")
    raise(ModuleNotFoundError)


