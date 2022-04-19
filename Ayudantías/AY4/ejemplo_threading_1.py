from time import sleep
import threading

def calculo_muy_complejo():
    for i in range(10):
        print(i)
        sleep(0.3)

def pasar_lista():
    estudiantes = ["Juan", "Rebeca", "Pedro", "Angélica"]
    for estudiante in estudiantes:
        print(estudiante, "Presente!")
        sleep(0.5)


hilo_calculo = threading.Thread(target=calculo_muy_complejo)
hilo_lista = threading.Thread(target=pasar_lista)

hilo_calculo.start()
hilo_lista.start()