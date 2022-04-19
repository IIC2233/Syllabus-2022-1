from time import sleep
from threading import Thread, Event

evento_global = Event()

def carrete(evento):
    sleep(0.5)
    print("Esperando algún carrete...")
    sleep(2)
    print("Aún no hay carrete...")
    evento.wait()
    print("CARRETEEEEE")

hilo_carrete = Thread(target=carrete, args=[evento_global])

hilo_carrete.start()

sleep(5)

evento_global.set()