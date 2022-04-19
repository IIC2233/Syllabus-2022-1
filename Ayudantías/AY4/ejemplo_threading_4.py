from threading import Thread, Lock

class Contador:
    def __init__(self):
        self.valor = 0


def sumador(contador, lock):
    for _ in range(1000000):
        lock.acquire()
        contador.valor += 1
        lock.release()

contador = Contador()
lock_global = Lock()

thread_contador_1 = Thread(target=sumador, args=(contador, lock_global))
thread_contador_2 = Thread(target=sumador, args=(contador, lock_global))

thread_contador_1.start()
thread_contador_2.start()

thread_contador_1.join()
thread_contador_2.join()

print("Valor del contador:", contador.valor)