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

        # Creamos los layouts que usaremos para ajustar los labels
        # en las ventanas y le agregamos los labels correspondientes.
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
        # Si el permiso es True, entonces ocultar esta ventana y mostrar una
        # nueva ventana de juego
        pass

class VentanaJuego(QMainWindow):

    # Definir la señal actualizar_vida, que recibe un int.
    # Definir la señal senal_confirmar_inicio que no recibe nada.
    # Definir la señal mover_personaje, que recibe dos enteros con la
    # posición x e y del jugador
    tecla_apretada = pyqtSignal(int)
    #                         (id,   x,   y, alto, ancho)
    aparecer_agua = pyqtSignal(int, int, int, int, int)
    #                             id
    desaparecer_agua = pyqtSignal(int)
    #         (x_max, y_max, x_jugador, y_jugador, alto_jugador, ancho_jugador)
    senal_iniciar_juego = pyqtSignal(int, int, int, int, int, int)

    def __init__(self, parent, nombre_jugador):
        super().__init__(parent)
        # Conectar la senal_iniciar_juego con el método para iniciar,
        # instanciar el backend entregándole los parámetros necesarios,
        # conectar las señales de aparecer agua y desaparecer agua.
        # Conectar señales actualizar_vida y mover_personaje
        # Setear el atributo background a un QLabel que tenga
        # el pixmap del desierto.
        # Setear el atributo label_jugador a un QLabel con el pixmap
        # del vaquero.
        # Conectar las señales mover_personaje y actualizar_vida
        self.label_vida = QLabel(self)
        self.label_vida.setFont(QFont('Arial', 17))
        self.label_vida.setGeometry(90, 10, 280, 50)
        self.labels_agua = {}  # id: label
        self.pixmap_agua = QPixmap('./sprites/water.png')
        self.show()

    def iniciar(self, x_max, y_max,
                x_jugador, y_jugador, alto_jugador, ancho_jugador):
        # Setear tamaño del juego, posicionar el jugador donde corresponde y
        # setear el porte del background para que ande bien
        pass

    def keyPressEvent(self, event):
        self.tecla_apretada.emit(event.key())

    def actualizar_label_personaje(self, x, y):
        # Mover el label del jugador según las coordenadas entregadas
        pass

    def actualizar_label_vida(self, vida):
        self.label_vida.setText(f'Tienes {vida} de vida')

    def agregar_label_agua(self, id, x, y, alto, ancho):
        # Agregar un label para el agua que apareció
        pass

    def remover_label_agua(self, id):
        # Esconder el label del agua
        pass
