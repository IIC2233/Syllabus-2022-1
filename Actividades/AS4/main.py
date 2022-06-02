from Parte2.campus import CreadorCampus
from Parte1.pizzeria import CreadorPizzeria
from Parte2.recorrido_campus import bfs_iterativo, bfs_iterativo_largo, \
    dfs_iterativo, bfs_iterativo_camino, dfs_iterativo_camino, dfs_iterativo_largo, imprimir_camino
from parametros import ARCHIVO_AYUDANTES, ARCHIVO_EVENTOS, ARCHIVO_NODOS, ARCHIVO_NODOS_VECINOS


def gestor_de_inputs(opciones, numero=3):
    eleccion = input("Seleccione su opción: ")
    while eleccion not in map(lambda x: str(x), range(1, numero+1)):
        print("Elección invalida, seleccione de nuevo")
        print(opciones)
        eleccion = input("Seleccione su opción")
    return eleccion


def menu_de_actividad():
    print("""\
    ██████╗  ██████╗ ██████╗██╗  ██╗██╗███████╗███╗   ███╗ ██████╗ ███████╗ ██████╗ ███████╗
    ██╔══██╗██╔════╝██╔════╝██║  ██║██║██╔════╝████╗ ████║██╔═══██╗██╔════╝██╔═══██╗██╔════╝
    ██║  ██║██║     ██║     ███████║██║███████╗██╔████╔██║██║   ██║███████╗██║   ██║███████╗
    ██║  ██║██║     ██║     ██╔══██║██║╚════██║██║╚██╔╝██║██║   ██║╚════██║██║   ██║╚════██║
    ██████╔╝╚██████╗╚██████╗██║  ██║██║███████║██║ ╚═╝ ██║╚██████╔╝███████║╚██████╔╝███████║
    ╚═════╝  ╚═════╝ ╚═════╝╚═╝  ╚═╝╚═╝╚══════╝╚═╝     ╚═╝ ╚═════╝ ╚══════╝ ╚═════╝ ╚══════╝
          """)

    print("""⠀
                   ⣠⣤⣶⣶⣦⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣷⣤⠀⠈⠙⢿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⠆⠰⠶⠀⠘⢿⣿⣿⣿⣿⣿⣆⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⣿⣿⠏⠀⢀⣠⣤⣤⣀⠙⣿⣿⣿⣿⣿⣷⡀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⢠⠋⢈⣉⠉⣡⣤⢰⣿⣿⣿⣿⣿⣷⡈⢿⣿⣿⣿⣿⣷⡀
    ⠀⠀⠀⠀⠀⠀⠀⡴⢡⣾⣿⣿⣷⠋⠁⣿⣿⣿⣿⣿⣿⣿⠃⠀⡻⣿⣿⣿⣿⡇
    ⠀⠀⠀⠀⠀⢀⠜⠁⠸⣿⣿⣿⠟⠀⠀⠘⠿⣿⣿⣿⡿⠋⠰⠖⠱⣽⠟⠋⠉⡇
    ⠀⠀⠀⠀⡰⠉⠖⣀⠀⠀⢁⣀⠀⣴⣶⣦⠀⢴⡆⠀⠀⢀⣀⣀⣉⡽⠷⠶⠋⠀
    ⠀⠀⠀⡰⢡⣾⣿⣿⣿⡄⠛⠋⠘⣿⣿⡿⠀⠀⣐⣲⣤⣯⠞⠉⠁⠀⠀⠀⠀⠀
    ⠀⢀⠔⠁⣿⣿⣿⣿⣿⡟⠀⠀⠀⢀⣄⣀⡞⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⡜⠀⠀⠻⣿⣿⠿⣻⣥⣀⡀⢠⡟⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⢰⠁⠀⡤⠖⠺⢶⡾⠃⠀⠈⠙⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠈⠓⠾⠇
    """)

    salir = False
    print("Iniciando simulación: \n")
    while not salir:
        opciones = "¿Que deseas hacer? \n" \
                   "[1] Realizar fila para comprar pizza \n" \
                   "[2] Recorrer el campus \n" \
                   "[3] Salir \n"
        print(opciones)
        eleccion = gestor_de_inputs(opciones)

        if eleccion == "1":
            creador = CreadorPizzeria(ARCHIVO_EVENTOS)
            pizzeria = creador.crear_pizzeria()

            print("Mientras Ruz está en la fila, observa los siguientes eventos \n")
            while pizzeria.tiene_siguiente_evento:
                pizzeria.procesar_siguiente_evento()

            print()

        elif eleccion == "2":
            print("\n---- Evitando Chismosos ------\n")

            creador_campus = CreadorCampus(ARCHIVO_NODOS, ARCHIVO_NODOS_VECINOS,
                                           ARCHIVO_AYUDANTES, "San Joaquin")
            campus = creador_campus.crear_campus()

            opciones = "¿Como debería Ruz buscar su camino?\n" \
                       "[1] Debería investigar si hay un camino (DFS) \n" \
                       "[2] Debería investigar si hay un camino (BFS) \n" \
                       "[3] Debería encontrar el largo del camino (DFS) \n" \
                       "[4] Debería encontrar el largo del camino (BFS) \n" \
                       "[5] [Bonus] Debería realizar una búsqueda de profundidad (DFS) " \
                       "para encontrar el camino \n" \
                       "[6] [Bonus] Debería realizar una búsqueda en anchura (BFS) " \
                       "para encontrar el camino\n" \
                       "[7] Ruz debería volver al menú anterior"
            print(opciones)
            eleccion_busqueda = gestor_de_inputs(opciones, 7)
            existencia = None
            camino = None
            largo = None
            volver = False
            if eleccion_busqueda == "1":
                print("RUTA DFS SIN CHISMOSOS:\n")
                existencia = dfs_iterativo(campus[1], campus[9])
            elif eleccion_busqueda == "2":
                print("RUTA BFS SIN CHISMOSOS:\n")
                existencia = bfs_iterativo(campus[1], campus[9])
            elif eleccion_busqueda == "3":
                print("RUTA DFS SIN CHISMOSOS:\n")
                largo = dfs_iterativo_largo(campus[1], campus[9])
            elif eleccion_busqueda == "4":
                print("RUTA BFS SIN CHISMOSOS:\n")
                largo = bfs_iterativo_largo(campus[1], campus[9])
            elif eleccion_busqueda == "5":
                print("RUTA DFS SIN CHISMOSOS:\n")
                camino = dfs_iterativo_camino(campus[1], campus[9])
            elif eleccion_busqueda == "6":
                print("RUTA BFS SIN CHISMOSOS:\n")
                camino = bfs_iterativo_camino(campus[1], campus[9])
            elif eleccion_busqueda == "7":
                print(" \nRuz está volviendo al menú anterior \n")
                volver = True

            if volver:
                pass
            elif camino is None and largo is None and existencia is None:
                print("Búsqueda de camino no implementada")
            elif camino:
                imprimir_camino(camino)
            elif largo:
                print(f"El largo del camino es {largo}")
            elif existencia:
                print("Existe un camino" if existencia else "No existe un camino")

        elif eleccion == "3":
            print("Al parecer no hay más pizza por hoy D:")
            salir = True



if __name__ == "__main__":
    menu_de_actividad()
