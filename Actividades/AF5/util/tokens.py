from util.archivo_csv import ArchivoCSV
from parametros import TOKENS_FILE_PATH


class Tokens(ArchivoCSV):
    def __init__(self):
        ArchivoCSV.__init__(self, TOKENS_FILE_PATH, ["token"])
        ArchivoCSV.cargar(self)

    def lista_a_elemento(self, e: list):
        self.append(e[0])

    def elemento_a_lista(self, e: str):
        return [e]
