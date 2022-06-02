def leer_archivo_nodos(ruta_archivo_nodos: str):
    # NO MODIFICAR
    with open(ruta_archivo_nodos, "r", encoding="utf-8") as archivo:
        lineas = archivo.readlines()
        lineas = lineas[1:]
        return [
            (linea[0].strip(), int(linea[1].strip()))
                for linea in [l.strip().split(',') for l in lineas]
        ]

def leer_archivo_conexiones(ruta_archivo_vecinos: str):
    # NO MODIFICAR
    with open(ruta_archivo_vecinos, "r", encoding="utf-8") as archivo:
        lineas = archivo.readlines()
        lineas = lineas[1:]
        return [(int(linea[0].strip()), int(linea[1].strip()))
                for linea in [l.strip().split(',') for l in lineas]]

def leer_archivo_eventos(ruta_archivo_eventos: str):
    # NO MODIFICAR
    with open(ruta_archivo_eventos, "r", encoding="utf-8") as archivo:
        lineas = archivo.readlines()
        lineas = lineas[1:]
        return [(
            int(linea[0].strip()),
            linea[1].strip(),
            [l.strip() for l in linea[2].strip().split(";")])
                for linea in [l.strip().split(',') for l in lineas]]

def leer_archivo_ayudantes(ruta_archivo_ayudantes):
    # NO MODIFICAR
    with open(ruta_archivo_ayudantes, "r", encoding="utf-8") as file:
        lineas = file.readlines()
        lineas = lineas[1:]
        return [(linea[0].strip(), linea[1].strip(), int(linea[2].strip()))
                for linea in [l.strip().split(',') for l in lineas]]

if __name__ == "__main__":
    print("\nNO DEBES EJECUTAR AQUÍ EL PROGRAMA!!!!")
    print("Ejecuta el main.py\n")
    raise(ModuleNotFoundError)