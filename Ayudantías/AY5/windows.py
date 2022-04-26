import sys
import os
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel,
                             QHBoxLayout, QVBoxLayout, QPlainTextEdit,
                             QLineEdit)
from PyQt5.QtCore import QCoreApplication, pyqtSignal, Qt
from PyQt5.QtGui import QPixmap


class MailWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.init_gui()

    def init_gui(self):
        pass
