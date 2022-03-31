from random import choice
from construcciones import Barracas, Muro, Catapulta, MuroCatapulta
from parametros import COSTO_UNIDADES


class Reino:
    # representara a un departamento de Ingenieria

    def __init__(self, nombre, dinero_inicial, construcciones, ganancias):
        # No modificar
        self.nombre = nombre
        self.dinero = dinero_inicial
        self.costos = construcciones
        self.ganancias = ganancias
        self.edad = "Media"
        self.bolsa = dinero_inicial
        self.__hp = 10000
        self._ataque = 0
        self.construcciones = {
            "Barracas": [Barracas(self.edad)],
            "Muro": [],
            "Catapulta": [],
            "MuroCatapulta": []
        }
        self.unidades = {
            "Guerrero": [],
            "Mago": [],
            "MagoGuerrero": []
        }
        self.para_construir = ["Barracas", "Muro", "Catapulta"]

    @property
    def hp(self):
        # No modificar
        return self.__hp

    @hp.setter
    def hp(self, valor):
        # No modificar
        if valor < 0:
            self.__hp = 0
        elif valor < 100:
            self.__hp = valor
            print(f"Al reino {self.nombre} le queda poca vida :o")
        else:
            self.__hp = valor

    @property
    def ataque(self):
        # No modificar
        daño = 0
        if self.construcciones["Catapulta"]:
            for catapulta in self.construcciones["Catapulta"]:
                daño += catapulta.accion()
        if self.construcciones["MuroCatapulta"]:
            for muro_catapulta in self.construcciones["MuroCatapulta"]:
                daño += muro_catapulta.accion()[1]
        if self.unidades["Guerrero"]:
            for guerrero in self.unidades["Guerrero"]:
                daño += guerrero.accion()
        if self.unidades["MagoGuerrero"]:
            for mago_guerrero in self.unidades["MagoGuerrero"]:
                daño += mago_guerrero.accion()[1]
        return daño

    def reconstruir(self):
        # No modificar
        reparacion = 0
        if self.construcciones["Muro"]:
            for catapulta in self.construcciones["Muro"]:
                reparacion += catapulta.accion()
        if self.construcciones["MuroCatapulta"]:
            for muro_catapulta in self.construcciones["MuroCatapulta"]:
                reparacion += muro_catapulta.accion()[0]
        if self.unidades["Mago"]:
            for guerrero in self.unidades["Mago"]:
                reparacion += guerrero.accion()
        if self.unidades["MagoGuerrero"]:
            for mago_guerrero in self.unidades["MagoGuerrero"]:
                reparacion += mago_guerrero.accion()[1]
        self.hp += reparacion
        print(f"{self.nombre}: ha reparado su reino en {reparacion} pts")

    def minar_datos(self):
        # No modificar
        resultados = ["baja", "baja", "baja", "baja", "media", "media",
                      "media", "alta", "alta", "super_alta"]
        produccion = choice(resultados)
        self.dinero += self.ganancias[produccion]
        self.bolsa += self.ganancias[produccion]
        print(f"{self.nombre}: la producción ha sido {produccion} y la ganancia"
              + f" es de ${self.ganancias[produccion]}")
        if self.edad == "Moderna":
            return
        elif self.bolsa >= 5000:
            self.avanzar_edad()

    def construir_estructura(self):
        # No modificar
        planos = choice(self.para_construir)
        if self.dinero >= self.costos[planos]:
            if planos == "Barracas":
                estructura = Barracas(self.edad)
                self.hp += estructura.hp
                self.construcciones[planos].append(estructura)
                print(f"{self.nombre}: ha construido Barracas")
            elif planos == "Muro":
                estructura = Muro(self.edad)
                self.hp += estructura.hp
                self.construcciones[planos].append(estructura)
                print(f"{self.nombre}: ha construido un Muro")
            elif planos == "Catapulta":
                estructura = Catapulta(self.edad)
                self.hp += estructura.hp
                self.construcciones[planos].append(estructura)
                print(f"{self.nombre}: ha construido una Catapulta")
            elif planos == "MuroCatapulta":
                estructura = MuroCatapulta(self.edad)
                self.hp += estructura.hp
                self.construcciones[planos].append(estructura)
                print(f"{self.nombre}: ha construido un MuroCatapulta")
            self.dinero -= self.costos[planos]
        else:
            print(f"{self.nombre}: no tiene el dinero suficiente para "
                  + f"construir {planos}")

    def crear_unidades(self):
        # No modificar
        if self.construcciones["Barracas"]:
            for barraca in self.construcciones["Barracas"]:
                if self.dinero >= COSTO_UNIDADES:
                    self.dinero -= COSTO_UNIDADES
                    tipo, unidad = barraca.accion()
                    print(f"{self.nombre}: ha creado un {unidad}")
                    self.unidades[tipo].append(unidad)
                else:
                    break

    def avanzar_edad(self):
        # Completar
        pass
