from reino import Reino
from simulacion import Simulacion
import parametros as p


if __name__ == "__main__":
    # No modificar
    dcc = Reino("DCC", p.DINERO_INICIAL_DCC,
                p.COSTOS_CONSTRUCCIONES, p.PRODUCCION_GANANCIAS)
    ics = Reino("ICS", p.DINERO_INICIAL_ICS,
                p.COSTOS_CONSTRUCCIONES, p.PRODUCCION_GANANCIAS)
    guerra = Simulacion(dcc, ics, p.SEMANAS_SIMULACION)
    guerra.run()
