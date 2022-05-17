import json
import socket
import threading


class Servidor:

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket_servidor.bind((self.host, self.port))
        self.socket_servidor.listen()
        self.clientes = {}
        print(f'Servidor escuchando en {self.host}:{self.port}')

        thread = threading.Thread(target=self.aceptar_clientes)
        thread.start()

    def aceptar_clientes(self):
        while True:
            socket_cliente, address = self.socket_servidor.accept()
            self.clientes[str(socket_cliente)] = socket_cliente
            print(f'Cliente con dirección {address} se ha conectado al servidor')
            thread_cliente = threading.Thread(target=self.escuchar_cliente, args=(socket_cliente,), daemon=True)
            thread_cliente.start()

    def escuchar_cliente(self, socket_cliente):
        try:
            while True:
                frase_secreta = "Al abordaje muchachos!"
                mensaje = self.recibir(socket_cliente)
                respuesta = self.manejar_mensaje_recibido(mensaje)
                print(f'Enviando respuesta: {respuesta}')
                if frase_secreta in mensaje:
                    self.enviar_todos(self.al_ataque())
                else:
                    self.enviar(respuesta, socket_cliente)
        except ConnectionResetError:
            print('Error de conexión con el cliente')

    def recibir(self, socket_cliente):
        largo_bytes_mensaje = socket_cliente.recv(4)
        largo_mensaje = int.from_bytes(largo_bytes_mensaje, byteorder='big')
        bytes_mensaje = bytearray()
        while len(bytes_mensaje) < largo_mensaje:
            bytes_mensaje += socket_cliente.recv(60)
        bytes_mensaje_limpios = bytes_mensaje.strip(b'\x00')
        if 5 < len(bytes_mensaje_limpios) < 60:
            mensaje = self.decodificar_mensaje(bytes_mensaje_limpios)
            return mensaje
        else:
            return ""

    def enviar(self, mensaje, socket_cliente):
        bytes_mensaje = self.codificar_mensaje(mensaje)
        while len(bytes_mensaje) % 60 != 0:
            bytes_mensaje += b'\x00'
        largo_bytes_mensaje = len(bytes_mensaje).to_bytes(4, byteorder='big')
        socket_cliente.sendall(largo_bytes_mensaje + bytes_mensaje)

    def enviar_todos(self, mensaje):
        for socket_cliente in self.clientes.values():
            bytes_mensaje = self.codificar_mensaje(mensaje)
            while len(bytes_mensaje) % 60 != 0:
                bytes_mensaje += b'\x00'
            largo_bytes_mensaje = len(bytes_mensaje).to_bytes(4, byteorder='big')
            socket_cliente.sendall(largo_bytes_mensaje + bytes_mensaje)

    def codificar_mensaje(self, mensaje):
        try:
            mensaje_json = json.dumps(mensaje)
            bytes_mensaje = mensaje_json.encode('utf-8')
            return bytes_mensaje
        except json.JSONDecodeError:
            print('No se pudo codificar el mensaje')
            return b''

    def decodificar_mensaje(self, bytes_mensaje):
        try:
            mensaje = json.loads(bytes_mensaje)
            return mensaje
        except json.JSONDecodeError:
            print('No se pudo decodificar el mensaje')
            return ''

    def manejar_mensaje_recibido(self, mensaje):
        return f'ECO: Respuesta asociada al mensaje: {mensaje}'

    def al_ataque(self):
        return f"Al ATAQUE!"


if __name__ == "__main__":
    host = "localhost"
    port = 5000
    servidor = Servidor(host, port)
