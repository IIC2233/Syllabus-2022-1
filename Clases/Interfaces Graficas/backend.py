from PyQt5.QtCore import QObject, QThread, QTimer
from time import sleep
import random


class Botella(QThread):

    id = 0

    def __init__(self, x, y, senal_aparecer_agua, senal_desaparecer_agua):
        super().__init__()
        self.id += 1
        Botella.id += 1
        self.x = x
        self.y = y
        self.alto = 80
        self.ancho = 40
        self.senal_aparecer_agua = senal_aparecer_agua
        self.senal_desaparecer_agua = senal_desaparecer_agua

    @property
    def valida(self):
        return self._valida

    @valida.setter
    def valida(self, value):
        # Seteo al atributo. Si el nuevo valor es verdadero, emit la señal
        # para que aparezca la botella en el front en caso contrario,
        # emito la señal para que se esconda la botella.
        pass

    def run(self):
        # La botella debe ser válida por 8 segundos, y luego deja de ser valida
        pass


class Jugador:

    def __init__(self, x, y, nombre, vida,
                 senal_posicion, senal_vida, ancho, alto):
        self.senal_posicion = senal_posicion
        self.senal_vida = senal_vida
        self._x = x
        self._y = y
        self.nombre = nombre
        self.tiempo_vida = vida
        self.tiempo_vida_maximo = vida
        self.ancho = ancho
        self.alto = alto

    @property
    def tiempo_vida(self):
        return self._tiempo_vida

    @tiempo_vida.setter
    def tiempo_vida(self, value):
        self._tiempo_vida = value
        # Completar con la señal para actualizar la vida del jugador

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value
        # Completar con la señal para actualizar la posición del jugador

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value
        # Completar con la señal para actualizar la posición del jugador


class LogInBackend:

    def __init__(self, recibir_login, responder_login):
        self.senal_responder_login = responder_login
        # Conectar la senal para recibir el login desde el front

    def login(self, nombre):
        # Responderle al front, con un diccionario de la forma:
        # {"permiso": bool, "nombre": string}
        pass


class Juego(QObject):
    id_botella = 0

    def __init__(self, tecla_apretada, mover_personaje, actualizar_vida,
                 nombre_jugador, senal_aparecer_agua, senal_desaparecer_agua,
                 confirmar_inicio, senal_iniciar_juego):
        # Debemos agregar una instancia de jugador.
        # Este parte en la posición 30, 30 con 90 de vida y debe tener 60 de
        # ancho y 120 de alto. Ademas, debemos conectar la senal de tecla
        # apretada con el método encargado de mover al jugador, y hacer que
        # cada 1 segundo, se llame al método sufrir_calor para que el jugador
        # pierda 1 de vida. Además de esto, debemos instanciar el camion aljibe
        # para que empieze a distribuir agua cuando comienze el juego.
        # Para esto, se deberá ejecutar el método dar_agua cada 5 segundos
        super().__init__()
        self.x_max = 1000
        self.y_max = 700
        self.velocidad = 10
        self.senal_aparecer_agua = senal_aparecer_agua
        self.senal_desaparecer_agua = senal_desaparecer_agua
        self.senal_iniciar_juego = senal_iniciar_juego
        self.botellas = []
        confirmar_inicio.connect(self.iniciar_juego)

    @property
    def jugando(self):
        # Vemos si el jugador sigue vivo, y retornamos eso.
        pass

    def dar_agua(self):
        # Si el jugador está vivo, generamos una botella en cualquier lugar
        # aleatorio del mapa, echamos a andar el tiempo de la botella y
        # guardamos la botella junto con las otras botellas
        pass

    def iniciar_juego(self):
        # Avisar al front que comienza el juego, y hacer que el aljibe
        # comienze a repartir agua
        pass

    def sufrir_calor(self):
        self.jugador.tiempo_vida -= 1

    def chequear_colision(self, botella):
        # Completar con chequear colisión
        pass

    def chequear_colisiones(self):
        # Chequear si alguna botella que sea válida colisiona con el jugador y
        # se la consigue.
        # Si es así, le aumentamos la vida al jugador en un numero aleatorio
        # entre 4, 6 y seteamos la botella que se consiguió como no valida.
        pass

    def mover_jugador(self, tecla):
        if tecla == 65:  # Apreto la A
            self.jugador.x -= self.velocidad
        elif tecla == 87:  # Apreto la W
            self.jugador.y -= self.velocidad
        elif tecla == 68:  # Apreto la D
            self.jugador.x += self.velocidad
        elif tecla == 83:  # Apreto la S
            self.jugador.y += self.velocidad
        self.chequear_colisiones()
