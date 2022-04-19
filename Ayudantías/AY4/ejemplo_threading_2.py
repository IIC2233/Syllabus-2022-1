from time import sleep
import threading

def calculo_muy_complejo():
    for i in range(10):
        print(i)
        sleep(0.3)

def pasar_lista(velocidad):
    estudiantes = ["Juan", "Rebeca", "Pedro", "Angélica"]
    for estudiante in estudiantes:
        print(estudiante, "Presente!")
        sleep(velocidad)


hilo_calculo = threading.Thread(target=calculo_muy_complejo)
hilo_lista = threading.Thread(target=pasar_lista, args=[0.3])

hilo_calculo.start()

hilo_calculo.join()

hilo_lista.start()