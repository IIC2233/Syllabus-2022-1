import os
import time
import csv
from PyQt5.QtCore import (QObject, pyqtSignal)


class Mailer():
    def __init__(self):

        # Se carga la base de datos de mails.
        path_mails = os.path.join("Data", "mails.csv")
        with open(path_mails, encoding="utf-8") as archivo:
            self.mails = list(map(lambda x: x.strip(), archivo))

    def send_mail(self, sender, receiver, subject, content):
        
        # Se verifica que el remitente haya sido ingresado y sea válido.
        if sender == "":
            return (400, "¡Debe ingresar un remitente!")

        elif sender not in self.mails:
            return (404, "El remitente no es válido.")

        # Se verifica que el destinatario se haya ingresado y sea válido.
        elif receiver == "":
            return (400, "¡Debe ingresar un destinatario!")

        elif receiver not in self.mails:
            return (404, f"El destinatario ingresado \"{self.destinatario}\" no es válido.")

        else:
            # Si no se agrega un asunto se permite el envío, pero se notifica.
            if subject != "":
                notificacion = "Su mensaje fue enviado correctamente."
            else:
                notificacion = "¡Su mensaje fue enviado sin asunto!"
            
            with open(os.path.join("Data", "actions.csv"),
                      "a", encoding="utf-8") as file:
                date = time.strftime("%d/%m/%Y %H:%M:%S", time.localtime())
                writer = csv.DictWriter(file, fieldnames =["Sender", "Receiver", "Subject", "Content", "Date"])
                writer.writerow({
                    "Sender": sender,
                    "Receiver": receiver, "Subject": subject, "Content": content, "Date": date})
            
            return (200, notificacion)
