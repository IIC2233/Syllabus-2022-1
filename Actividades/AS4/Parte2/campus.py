from Parte2.lectura_archivos_parte2 import leer_archivo_ayudantes, leer_archivo_conexiones, \
                             leer_archivo_nodos
from parametros import ARCHIVO_NODOS, ARCHIVO_NODOS_VECINOS, ARCHIVO_AYUDANTES
from Parte2.ayudantes import Ayudante

class Lugar:
    # NO MODIFICAR
    def __init__(self, nombre, id):
        self.nombre = nombre
        self.id = id
        self.vecinos = []
        self.ayudantes = []

    def agregar_vecino(self, vecino):
        # NO MODIFICAR
        self.vecinos.append(vecino)

    def agregar_ayudante(self, ayudante):
        # NO MODIFICAR
        self.ayudantes.append(ayudante)

    def __repr__(self):
        # NO MODIFICAR
        return self.nombre


class Campus():
    # NO MODIFICAR
    def __init__(self, nombre):
        # NO MODIFICAR
        self.lugares = dict()
        self.raiz: Lugar = None
        self.nombre = nombre

    def agregar_lugar(self, nombre, id):
        # NO MODIFICAR
        self.lugares[id] = Lugar(nombre, id)
        if self.raiz is None:
            self.raiz = self.lugares[id]
  
    def crear_conexion(self, lugar_1: int, lugar_2: int):
        # NO MODIFICAR
        self.lugares[lugar_1].agregar_vecino(self.lugares[lugar_2])
        self.lugares[lugar_2].agregar_vecino(self.lugares[lugar_1])
    
    def agregar_ayudante(self, nombre: str, frase: str, id_lugar: int):
        # NO MODIFICAR
        lugar = self.lugares[id_lugar]
        lugar.agregar_ayudante(Ayudante(nombre, frase))

    def __getitem__(self, item):
        # NO MODIFICAR
        return self.lugares[item]

    def __str__(self):
        # NO MODIFICAR
        text = self.nombre + "\n"
        for lugar in self.lugares.values():
            text += str(lugar) + "\n"
        return text


class CreadorCampus:
# NO MODIFICAR
# es una factoria :D
    def __init__(self, ruta_archivo_nodos, ruta_archivo_vecinos,
                 ruta_archivo_ayudantes, nombre_campus):
        # NO MODIFICAR
        self.ruta_archivo_nodos = ruta_archivo_nodos
        self.ruta_archivo_vecinos = ruta_archivo_vecinos
        self.nombre_campus = nombre_campus
        self.ruta_archivo_ayudantes = ruta_archivo_ayudantes

    def crear_campus(self):
        # NO MODIFICAR
        mapa = Campus(self.nombre_campus)
        lineas_nodos = leer_archivo_nodos(self.ruta_archivo_nodos)
        self.instanciar_nodos(mapa, lineas_nodos)
        lineas_conexiones = leer_archivo_conexiones(self.ruta_archivo_vecinos)
        self.crear_conexiones(mapa, lineas_conexiones)
        lineas_ayudantes = leer_archivo_ayudantes(self.ruta_archivo_ayudantes)
        self.cargar_ayudantes(mapa, lineas_ayudantes)
        return mapa

    def instanciar_nodos(self, mapa, info_nodos):
        # NO MODIFICAR
        for nombre_nodo, id_nodo in info_nodos:
            mapa.agregar_lugar(nombre_nodo, id_nodo)

    def crear_conexiones(self, mapa, info_conexiones):
        # NO MODIFICAR
        for nodo_1, nodo_2 in info_conexiones:
            mapa.crear_conexion(nodo_1, nodo_2)

    def cargar_ayudantes(self, mapa, info_ayudantes):
        # NO MODIFICAR
        for nombre, frase, nodo_id in info_ayudantes:
            mapa.agregar_ayudante(nombre, frase, nodo_id)


if __name__ == "__main__":
    print("\nNO DEBES EJECUTAR AQUÍ EL PROGRAMA!!!!")
    print("Ejecuta el main.py\n")
    raise(ModuleNotFoundError)
