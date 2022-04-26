import sys
from PyQt5.QtWidgets import QApplication
from windows import MailWindow
from systems import Mailer


def hook(type, value, traceback):
    print(type)
    print(traceback)
    sys.__excepthook__ = hook


app = QApplication([])

# Se instancian las clases necesarias.

ventana_mail = MailWindow()
procesamiento_mail = Mailer()

# Se conectan las señales entre el front y el back.

ventana_mail.show()
sys.exit(app.exec_())
