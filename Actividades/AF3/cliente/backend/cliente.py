"""
Modulo contiene implementación principal del cliente
"""
import socket
import json
from threading import Thread
from backend.interfaz import Interfaz


class Cliente:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.conectado = False
        self.interfaz = Interfaz(self)
        self.iniciar_cliente()

    def iniciar_cliente(self):
        """
        Se encarga de iniciar el cliente y conectar el socket
        """

        # TODO: Completado por estudiante
        pass

    def comenzar_a_escuchar(self):
        """
        Instancia el Thread que escucha los mensajes del servidor
        """
        # TODO: Completado por estudiante
        pass

    def escuchar_servidor(self):
        """
        Recibe mensajes constantes desde el servidor y responde.
        """
        # TODO: Completado por estudiante
        pass

    def recibir(self):
        """
        Se encarga de recibir lis mensajes del servidor.
        """
        # TODO: Completado por estudiante
        pass

    def enviar(self, mensaje):
        """
        Envía un mensaje a un cliente.
        """
        # TODO: Completado por estudiante
        pass

    def codificar_mensaje(self, mensaje):
        """
        Codifica el mensaje a enviar
        """
        try:
            # TODO: Completado por estudiante
            pass
        except json.JSONDecodeError:
            print("ERROR: No se pudo codificar el mensaje")
            return b""

    def decodificar_mensaje(self, mensaje_bytes):
        """
        Decodifica el mensaje del servidor
        """
        try:
            # TODO: Completado por estudiante
            pass
        except json.JSONDecodeError:
            print("ERROR: No se pudo decodificar el mensaje")
            return {}
