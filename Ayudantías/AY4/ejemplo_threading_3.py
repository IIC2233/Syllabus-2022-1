from time import sleep
from threading import Thread

class Sala(Thread):
    def __init__(self, lista_estudiantes, profe, nombre_hilo):
        super().__init__(name=nombre_hilo)
        self.lista_estudiantes = lista_estudiantes
        self.profe = profe

    def run(self):
        print("Profe", self.profe, "está pasando lista")
        for estudiante in self.lista_estudiantes:
            print(estudiante, "Presente!")
            sleep(0.3)


estudiantes = ["Juan", "Rebeca", "Pedro", "Angélica"]
profe = "Diego"

sala = Sala(estudiantes, profe, "Sala de clases")
sala.start()