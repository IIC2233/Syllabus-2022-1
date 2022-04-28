from PyQt5.QtWidgets import QApplication
from frontend import VentanaInicio
import sys


app = QApplication([])
login = VentanaInicio()
sys.exit(app.exec_())
