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
        self._valida = value
        if not self.valida:
            self.senal_desaparecer_agua.emit(self.id)
        else:
            self.senal_aparecer_agua.emit(self.id, self.x, self.y,
                                          self.alto, self.ancho)

    def run(self):
        self.valida = True
        sleep(8)
        self.valida = False


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
        self.senal_vida.emit(self.tiempo_vida)

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value
        self.senal_posicion.emit(self.x, self.y)

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value
        self.senal_posicion.emit(self.x, self.y)


class LogInBackend:

    def __init__(self, recibir_login, responder_login):
        self.senal_responder_login = responder_login
        recibir_login.connect(self.login)

    def login(self, nombre):
        self.senal_responder_login.emit(
            {"permiso": random.random() >= 0.1, "nombre": nombre}
        )


class Juego(QObject):
    id_botella = 0

    def __init__(self, tecla_apretada, mover_personaje, actualizar_vida,
                 nombre_jugador, senal_aparecer_agua, senal_desaparecer_agua,
                 confirmar_inicio, senal_iniciar_juego):
        super().__init__()
        self.jugador = Jugador(30, 30, nombre_jugador, 90,
                               mover_personaje, actualizar_vida, 60, 120)
        tecla_apretada.connect(self.mover_jugador)
        self.timer_calor = QTimer()
        self.timer_calor.setInterval(1000)
        self.timer_calor.timeout.connect(self.sufrir_calor)
        self.timer_calor.start()
        self.senal_aparecer_agua = senal_aparecer_agua
        self.senal_desaparecer_agua = senal_desaparecer_agua
        self.x_max = 1000
        self.y_max = 700
        self.velocidad = 10
        self.senal_iniciar_juego = senal_iniciar_juego
        self.botellas = []
        confirmar_inicio.connect(self.iniciar_juego)
        self.aljibe = QTimer(self)
        self.aljibe.setInterval(5000)
        self.aljibe.timeout.connect(self.dar_agua)

    def jugando(self):
        return self.jugador.tiempo_vida >= 0

    def dar_agua(self):
        if self.jugando:
            x = random.randint(0, self.x_max)
            y = random.randint(0, self.y_max)
            botella = Botella(
                x,
                y,
                self.senal_aparecer_agua,
                self.senal_desaparecer_agua
            )
            self.botellas.append(botella)
            botella.start()

    def iniciar_juego(self):
        self.senal_iniciar_juego.emit(self.x_max, self.y_max, self.jugador.x,
                                      self.jugador.y, self.jugador.alto,
                                      self.jugador.ancho)
        self.aljibe.start()

    def sufrir_calor(self):
        self.jugador.tiempo_vida -= 1

    def chequear_colision(self, botella):
        if self.jugador.x >= botella.x + botella.ancho:
            return False
        if self.jugador.x + self.jugador.ancho <= botella.x:
            return False
        if self.jugador.y >= botella.y + botella.alto:
            return False
        if self.jugador.y + self.jugador.alto <= botella.y:
            return False
        return True

    def chequear_colisiones(self):
        for botella in self.botellas:
            if botella.valida:
                if self.chequear_colision(botella):
                    self.jugador.tiempo_vida += random.randint(4, 6)
                    botella.valida = False

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
