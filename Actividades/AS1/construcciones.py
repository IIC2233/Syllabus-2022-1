from abc import ABC, abstractmethod
from random import choice, randint, random
from unidades import Guerrero, Mago, MagoGuerrero
from parametros import PROB_CRITICO_MURO, PROB_CRITICO_CATAPULTA, \
                       HP_MUROCATAPULTA, PROB_CRITICO_MURO_CATAPULTA, \
                       HP_BARRACAS, HP_MURO, HP_CATAPULTA


# Recuerda que es una clase abstracta
class Estructura:

    def __init__(self, edad, *args):
        # No modificar
        super().__init__(*args)
        self.edad = edad
        self.asignar_atributos_segun_edad()

    # ---------------
    # Completar los métodos abstractos aquí

    # ---------------


# Recuerda completar la herencia
class Barracas:

    def __init__(self, *args):
        # Completar
        pass

    # ---------------
    # Completar los métodos aquí

    # ---------------

    def accion(self):
        # No modificar
        elegido = choice(self.unidades)
        suerte = choice((True, False))
        experiencia = choice([1, 2, 3, 4, 5, 6])
        energia = choice([1, 2, 3, 4, 5, 6])
        if elegido == "Guerrero":
            return elegido, Guerrero(suerte, xp=experiencia, stamina=energia)
        elif elegido == "Mago":
            return elegido, Mago(suerte, xp=experiencia, stamina=energia)
        elif elegido == "MagoGuerrero":
            atributos = {"bendito": suerte, "armado": suerte, "xp": experiencia,
                         "stamina": energia}
            return elegido, MagoGuerrero(**atributos)


# Recuerda completar la herencia
class Muro:

    def __init__(self, *args):
        # Completar
        pass

    # ---------------
    # Completar los métodos aquí

    # ---------------


# Recuerda completar la herencia
class Catapulta:

    def __init__(self, *args):
        # Completar
        pass

    # ---------------
    # Completar los métodos aquí

    # ---------------


# Recuerda completar la herencia
class MuroCatapulta(Muro, Catapulta):

    def __init__(self, *args):
        # Completar
        pass

    # ---------------
    # Completar los métodos aquí

    # ---------------


if __name__ == "__main__":
    # ---------------
    # En esta sección puedes probar tu codigo
    # ---------------
    pass
