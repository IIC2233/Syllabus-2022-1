import os
from abc import ABC, abstractmethod
from collections import deque


class ArchivoCSV(deque, ABC):
    def __init__(self, archivo: str, cabeceras: list):
        super().__init__()
        self.archivo: str = archivo
        self.cabeceras: list = cabeceras
        self.cargado = False

    @abstractmethod
    def lista_a_elemento(self, data: list):
        self.append(data)

    @abstractmethod
    def elemento_a_lista(self, e: list):
        return e

    def cargar(self):
        self.clear()
        if not self.cargado and not os.path.isfile(self.archivo):
            self.cargado = True
            self.guardar()
        try:
            with open(self.archivo, 'r+', encoding="utf-8") as f:
                if f.readline().replace("\n", "") == ",".join(self.cabeceras):
                    while linea := f.readline():
                        self.lista_a_elemento(linea.replace("\n", "").split(",", len(self.cabeceras)))
                    self.cargado = True
                else:
                    raise Exception(0, "Format Error")
        except Exception as e:
            print(f'Error Grave: {self.archivo} - {e.args[1]}')
            exit(1)

    def guardar(self):
        if not self.cargado:
            return False
        try:
            with open(self.archivo, 'w+', encoding="utf-8") as f:
                f.write(",".join(self.cabeceras))
                for e in self:
                    f.write(f'\n{",".join(self.elemento_a_lista(e))}')
                return True
        except Exception as e:
            print(f'Error Grave: {self.archivo} - {e.args[1]}')
            exit(1)
