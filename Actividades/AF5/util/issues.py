from util.archivo_csv import ArchivoCSV
from parametros import ISSUES_FILE_PATH


class Issues(ArchivoCSV):
    def __init__(self):
        ArchivoCSV.__init__(self, ISSUES_FILE_PATH, ["numero"])
        ArchivoCSV.cargar(self)

    def lista_a_elemento(self, e: list):
        self.append(int(e[0]))

    def elemento_a_lista(self, e: int):
        return [str(e)]
