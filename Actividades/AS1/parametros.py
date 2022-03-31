from os.path import join

DINERO_INICIAL_DCC = 3500
DINERO_INICIAL_ICS = 3000

RUTA_CONSTRUCCIONES = join("datos", "construcciones.csv")
RUTA_GANANCIAS = join("datos", "ganancias.csv")

# parametros para unidades.py
PROB_REVIVIR = 0.5
PROB_CRITICO_GUERRERO = 0.5
PROB_CRITICO_MAGO = 0.6
PROB_CRITICO_MAGO_GUERRERO = 0.7

# parametros para construcciones.py

PROB_CRITICO_MURO = 0.4
PROB_CRITICO_CATAPULTA = 0.5
PROB_CRITICO_MURO_CATAPULTA = 0.6
HP_BARRACAS = 50
HP_MURO = 400
HP_CATAPULTA = 100
HP_MUROCATAPULTA = 600

# parametros para reino.py
COSTO_UNIDADES = 100

# parametros para main.py
SEMANAS_SIMULACION = 100

COSTOS_CONSTRUCCIONES = {
    "Barracas": 500,
    "Muro": 400,
    "Catapulta": 300,
    "MuroCatapulta": 500
}

PRODUCCION_GANANCIAS = {
    "baja": 100,
    "media": 300,
    "alta": 500,
    "super_alta": 1000
}
