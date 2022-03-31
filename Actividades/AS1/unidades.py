from abc import ABC, abstractmethod
from parametros import PROB_REVIVIR, PROB_CRITICO_GUERRERO, \
                    PROB_CRITICO_MAGO, PROB_CRITICO_MAGO_GUERRERO
import math
import random


# Recuerda que es una clase abstracta
class Persona:

    def __init__(self, xp, stamina, **kwargs):
        # No modificar
        super().__init__(**kwargs)
        self.xp = xp
        self.stamina = stamina
        self.asignar_parametros()

    @property
    def stamina(self):
        # No modificar
        return self._stamina

    @stamina.setter
    def stamina(self, value):
        # No modificar
        if value <= 0:
            if not self.revivir():
                print("F")
        else:
            self._stamina = value

    def revivir(self):
        # No modificar
        if PROB_REVIVIR > random.random():
            self.stamina += 3
            return True
        else:
            return False

    # ---------------
    # Completar los métodos abstractos aquí

    # ---------------


# Recuerda completar la herencia
class Guerrero:

    def __init__(self, armado, **kwargs):
        # Completar
        pass

    # ---------------
    # Completar los métodos aquí

    # ---------------


# Recuerda completar la herencia
class Mago:

    def __init__(self, bendito, **kwargs):
        # Completar
        pass

    # ---------------
    # Completar los métodos aquí

    # ---------------


# Recuerda completar la herencia
class MagoGuerrero:

    def __init__(self, **kwargs):
        # Completar
        pass

    # ---------------
    # Completar los métodos aquí

    # ---------------

    def __str__(self):
        # No modificar
        if self.armado and self.bendito:
            return f"MagoGuerrero BENDITO y ARMADO con {self.curacion}" \
                   + f" pts de curación y {self.ataque} pts de ataque."
        else:
            return f"MagoGuerrero con {self.curacion} pts de curación" \
                + f" y {self.ataque} pts de ataque."


if __name__ == "__main__":
    # ---------------
    # En esta sección puedes probar tu codigo
    # ---------------
    pass
