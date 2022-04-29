from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import (
    QHBoxLayout, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget
)
from PyQt5.QtGui import QFont, QPixmap
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QLabel, QMainWindow)
from backend import Juego, LogInBackend


class VentanaInicio(QWidget):

    senal_enviar_login = pyqtSignal(str)
    senal_recibir_login = pyqtSignal(dict)

    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 400, 150)
        self.setWindowTitle("Log In")

        # Creamos los labels que vamos a necesitar en nuestra ventana de LogIn
        username_label = QLabel('Ingrese su nombre:', self)
        self.input_usuario = QLineEdit('', self)
        self.boton_ingresar = QPushButton("Ingresar", self)

        # Creamos los layouts que usaremos para ajustar los labels en
        # las ventanas y le agregamos los labels correspondientes.
        layout_principal = QVBoxLayout()
        layout_formulario = QHBoxLayout()
        layout_boton = QHBoxLayout()
        layout_formulario.addWidget(username_label)

        layout_boton.addWidget(self.boton_ingresar)

        layout_formulario.addWidget(self.input_usuario)
        layout_principal.addLayout(layout_formulario)
        layout_principal.addLayout(layout_boton)
        self.setLayout(layout_principal)

        # Finalmente, dejamos las señales conectadas para que todo ande bien,
        # y le asignamos un backend a la ventana
        self.boton_ingresar.clicked.connect(self.enviar_login)
        self.senal_recibir_login.connect(self.entrar_juego)
        self.backend = LogInBackend(self.senal_enviar_login,
                                    self.senal_recibir_login)
        self.show()

    def enviar_login(self):
        # Le avisamos al backend que nos estamos conectando mediante la señal.
        self.senal_enviar_login.emit(self.input_usuario.text())

    def entrar_juego(self, diccionario):
        if diccionario["permiso"]:
            VentanaJuego(self, diccionario["nombre"])
            self.hide()


class VentanaJuego(QMainWindow):

    tecla_apretada = pyqtSignal(int)
    mover_personaje = pyqtSignal(int, int)
    actualizar_vida = pyqtSignal(int)
    #                         (id,   x,   y, alto, ancho)
    aparecer_agua = pyqtSignal(int, int, int, int, int)
    #                             id
    desaparecer_agua = pyqtSignal(int)
    #         (x_max, y_max, x_jugador, y_jugador, alto_jugador, ancho_jugador)
    senal_iniciar_juego = pyqtSignal(int, int, int, int, int, int)
    senal_confirmar_inicio = pyqtSignal()

    def __init__(self, parent, nombre_jugador):
        super().__init__(parent)
        self.senal_iniciar_juego.connect(self.iniciar)
        self.background = QLabel(self)
        background = QPixmap('./sprites/desierto.jpg')
        self.background.setPixmap(background)
        self.label_jugador = QLabel(self)
        self.label_vida = QLabel(self)
        self.label_vida.setFont(QFont('Arial', 17))
        self.label_vida.setGeometry(90, 10, 280, 50)
        pixmap = QPixmap('./sprites/cowboy.png')
        self.label_jugador.setPixmap(pixmap)
        self.label_jugador.setScaledContents(True)
        self.labels_agua = {}  # id: label
        self.aparecer_agua.connect(self.agregar_label_agua)
        self.desaparecer_agua.connect(self.remover_label_agua)
        self.pixmap_agua = QPixmap('./sprites/water.png')
        self.show()
        self.mover_personaje.connect(self.actualizar_label_personaje)
        self.actualizar_vida.connect(self.actualizar_label_vida)
        self.backend = Juego(
            self.tecla_apretada,
            self.mover_personaje,
            self.actualizar_vida,
            nombre_jugador,
            self.aparecer_agua,
            self.desaparecer_agua,
            self.senal_confirmar_inicio,
            self.senal_iniciar_juego
        )
        self.backend.iniciar_juego()

    def iniciar(self, x_max, y_max,
                x_jugador, y_jugador, alto_jugador, ancho_jugador):
        self.setGeometry(100, 100, x_max, y_max)
        self.background.setGeometry(0, 0, x_max, y_max)
        self.label_jugador.setGeometry(x_jugador, y_jugador,
                                       ancho_jugador, alto_jugador)
        self.label_jugador.setScaledContents(True)

    def keyPressEvent(self, event):
        self.tecla_apretada.emit(event.key())

    def actualizar_label_personaje(self, x, y):
        self.label_jugador.move(x, y)

    def actualizar_label_vida(self, vida):
        self.label_vida.setText(f'Tienes {vida} de vida')

    def agregar_label_agua(self, id, x, y, alto, ancho):
        label = QLabel(self)
        label.setPixmap(self.pixmap_agua)
        label.setScaledContents(True)
        label.setGeometry(x, y, ancho, alto)
        self.labels_agua[id] = label
        label.show()

    def remover_label_agua(self, id):
        self.labels_agua[id].hide()
