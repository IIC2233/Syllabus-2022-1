from time import sleep
import threading

def calculo_muy_complejo():
    for i in range(10):
        print(i)
        sleep(0.3)

hilo_calculo = threading.Thread(target=calculo_muy_complejo)
hilo_calculo.start()