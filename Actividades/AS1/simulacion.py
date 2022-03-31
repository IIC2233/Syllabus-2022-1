from random import randint


class Simulacion:

    def __init__(self, reino_1, reino_2, semanas_maximas):
        # No modificar
        self.reino_1 = reino_1
        self.reino_2 = reino_2
        self.semanas_maximas = semanas_maximas
        self.semana_actual = 0

    def run(self):
        # No modificar
        print("#" * 60)
        print(" HA INICIADO LA GUERRA ENTRE REINOS ".center(60, "#"))
        print("#" * 60)
        while (self.semanas_maximas > self.semana_actual) \
                and (self.reino_1.hp > 0 and self.reino_2.hp > 0):
            print("\n" + f" Semana: {self.semana_actual} ".center(60, "-")
                  + "\n")
            atacante = randint(1, 2)
            if atacante == 1:
                daño = self.preparacion_reinos(self.reino_1)
                self.ataque_entre_reinos(self.reino_1, self.reino_2, daño)
                daño = self.preparacion_reinos(self.reino_2)
                self.ataque_entre_reinos(self.reino_2, self.reino_1, daño)
            else:
                daño = self.preparacion_reinos(self.reino_2)
                self.ataque_entre_reinos(self.reino_2, self.reino_1, daño)
                daño = self.preparacion_reinos(self.reino_1)
                self.ataque_entre_reinos(self.reino_1, self.reino_2, daño)
            self.semana_actual += 1
        print("\n" + "#" * 60)
        print(" DATOS FINALES DE LA GUERRA ".center(60, "#"))
        print("#" * 60 + "\n")
        self.datos_finales(self.reino_1)
        self.datos_finales(self.reino_2)
        print("*" * 60)
        if self.reino_1.hp > self.reino_2.hp:
            win = self.reino_1.nombre
            print(f" {win} HA GANADO LA GUERRA DE REINOS ".center(60, "*"))
        elif self.reino_2.hp > self.reino_1.hp:
            win = self.reino_2.nombre
            print(f" {win} HA GANADO LA GUERRA DE REINOS ".center(60, "*"))
        print("*" * 60 + "\n")

    def preparacion_reinos(self, reino):
        # No modificar
        reino.minar_datos()
        reino.construir_estructura()
        reino.crear_unidades()
        reino.reconstruir()
        daños = reino.ataque
        return daños

    def ataque_entre_reinos(self, atacante, defensor, daño_atacante):
        # No modificar
        if daño_atacante > 0:
            defensor.hp -= daño_atacante
            print(f"{atacante.nombre}: Ha dañado en {daño_atacante} pts "
                  + "el castillo del {defensor.nombre}\n")

    def datos_finales(self, reino):
        # No modificar
        print(f"{reino.nombre}: en la edad {reino.edad}")
        print(f"{reino.nombre}: termino con {reino.dinero} de oro")
        print(f"{reino.nombre}: acumulo {reino.bolsa}")
        print(f"{reino.nombre}: El castillo quedo con {reino.hp} pts\n")
