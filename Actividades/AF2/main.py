from dcconcierto import DCConcierto
from cargar_datos import cargar_artistas, cargar_suministros
from random import choice

from parametros import (ANIMO_MINIMO, PUBLICO_ACCION, PUBLICO_FIN_ARTISTA,
                        PUBLICO_HIT)


def menu_inicio():
    while True:
        print(" MENU DE INICIO ".center(80, "="))
        print("Selecciona una opción")
        print("[1] Ingresar")
        print("[0] Salir :c")

        opcion = input("Indique su opción: ")

        if opcion == "1":  # Ingresar
            dcconcierto = DCConcierto()
            todos_artistas = cargar_artistas('artistas.csv')
            dcconcierto.artistas = todos_artistas
            for artista in dcconcierto.artistas:
                print(artista.nombre)
            dcconcierto.asignar_lineup()
            lista_suministros = cargar_suministros('suministros.csv')
            dcconcierto.suministros = lista_suministros
            menu_concierto(dcconcierto)

        elif opcion == "0":  # Salir
            print("Vuelve pronto!")
            break

        else:
            print("La opción ingresada no es válida")


def menu_concierto(dcconcierto):
    while dcconcierto.funcionando:
        print(f" MENU DÍA {dcconcierto.dia} ".center(80, "="))
        print("Selecciona un artista")
        contador = 1
        for artista in dcconcierto.line_up:
            print(f"[{contador}] {artista.nombre} ")
            contador += 1
        print(f'[{contador}] Estado del Concierto')
        contador += 1
        print(f'[{contador}] Pasar Día')

        op = input("Seleccione la opción: ")

        if 0 < int(op) <= len(dcconcierto.line_up):
            artista = dcconcierto.line_up[int(op) - 1]
            dcconcierto.artista_actual = artista
            menu_artista(artista, dcconcierto)

        elif (
            len(dcconcierto.line_up) < int(op) <= len(dcconcierto.line_up) + 2
             ):
            if op == str(len(dcconcierto.line_up) + 1):
                dcconcierto.imprimir_estado()
            else:
                dcconcierto.nuevo_dia()
                dcconcierto.asignar_lineup()

        else:
            print("La opción ingresada no es válida")
    if not dcconcierto.exito_del_concierto:
        print("El concierto se ha quedado sin la cantidad de público "
              "mínima para funcionar, FIN DEL JUEGO :(")
    else:
        print(f"Felicitaciones! Lograste coordinar con éxito el "
              f"DCConcierto. Público final: {dcconcierto.cant_publico}")


def menu_artista(artista, dcconcierto):
    op = None
    while dcconcierto.funcionando and op != "-1":
        print(" MENU DEL ARTISTA ".center(80, "="))
        print(f"{artista}")
        print(f"¿Qué debe hacer con {artista.nombre}?")
        print("[1] Acción")
        print("[2] Cantar Hit")
        print("[p] Pedir suministro")
        print("[e] Estado del concierto")
        print("[-1] Terminar presentación del artista")
        print("\n")

        op = input("Indique su opción: ")

        if op == "-1":  # Volver atrás
            dcconcierto.line_up.remove(artista)
            dcconcierto.cant_publico -= PUBLICO_FIN_ARTISTA
            print(f"{artista.nombre} terminó su presentación. "
                  f"Se fueron sus fans del concierto...")

        elif op == "p":  # Pasar de día
            artista.recibir_suministros(choice(dcconcierto.suministros))

        elif op == "1" or op == "2":
            if artista.animo >= ANIMO_MINIMO:
                if op == "1":  # Accion
                    artista.accion_especial()
                    dcconcierto.cant_publico += PUBLICO_ACCION
                elif op == "2":  # Cantar hit
                    artista.cantar_hit()
                    dcconcierto.cant_publico += PUBLICO_HIT
                dcconcierto.ejecutar_evento()
            else:
                print("El artista no tiene el animo para realizar esas acciones")

        elif op == "e":
            dcconcierto.imprimir_estado()

        else:
            print("La opción ingresada no es válida")


if __name__ == '__main__':
    menu_inicio()
