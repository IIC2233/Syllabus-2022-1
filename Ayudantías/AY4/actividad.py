import threading
import os
import random
import time


class MiCelular(threading.Thread):

    def __init__(self, chats):
        super().__init__()
        self.chats = chats
        print(self.chats)

    def run(self):

        for _ in range(10):
            time.sleep(1)
            self.enviar_whatsapp()

    def enviar_whatsapp(self):
        chat = random.choice(self.chats)
        if isinstance(chat, OtroCelular):
            chat.senal_whatsapp.set()
        else:
            for persona in chat:
                persona.senal_whatsapp.set()


class OtroCelular(threading.Thread):

    lock = threading.Lock()

    def __init__(self, archivo):
        super().__init__()
        self.senal_whatsapp = threading.Event()
        self.archivo = archivo
        self.notificaciones = 0

    def run(self):
        while True:
            self.senal_whatsapp.wait()
            self.senal_whatsapp.clear()
            self.recibir_whatsapp()

    def recibir_whatsapp(self):
        print(f"¡{self.name} recibió un whatsapp!")
        self.notificaciones += 1
        with self.lock:
            print(self.name)
            self.archivo.write(f"[{self.name}]: Tienes " 
                f"{self.notificaciones} notificaciones de Wahtsapp sin leer.\n")


with open(os.path.join("notificaciones.txt"), "w") as archivo:

    contactos = [OtroCelular(archivo) for _ in range(5)]
    grupo = [random.choices(contactos, k=2)]
    chats = contactos + grupo
    mi_celular = MiCelular(chats)

    mi_celular.start()
    for thread in contactos:
        thread.start()

    for thread in contactos:
        thread.join()
