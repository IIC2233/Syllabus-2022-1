from typing import List
from math import log10


def menu_opciones(titulo: str = "", descripcion: str = "",
                  opciones: List[str] = [], cancelar: str = "Cancelar"):
    print(f'\n\n\n  {titulo}:\n')

    if descripcion != "":
        print(f'{descripcion}\n')

    n_digitos = 1
    if len(opciones) > 0:
        n_digitos += int(log10(len(opciones)))

    plantilla = "\t[{:{}}] {}"
    for i in opciones:
        print(plantilla.format(opciones.index(i) + 1, n_digitos, i))
    print(plantilla.format(0, n_digitos, cancelar))
    pregunta = f'\n  Ingresa un número entre 0 y {len(opciones)}: '

    while not (opcion := input(pregunta).strip()).isdigit()\
            or (opcion := int(opcion)) > len(opciones):
        input(f'  La opción [{opcion}] no es válida.'
              f'Presione Enter para continuar.')
        return -1
    return opcion


def pedir_texto(titulo="Texto Fantasma", largo_min=0, largo_max=144,
                prohibido=set()):
    while True:
        print(f'  Ingresa {titulo}')
        texto = input()
        if len(texto) < largo_min or largo_max < len(texto):
            print(f'  "{texto}" no es válido.'
                  f' {titulo} debe tener entre'
                  f' {largo_min} y {largo_max} caracteres')
            input("Aprieta enter para continuar.")
        elif 1 in [caracter in texto for caracter in prohibido]:
            print(f'  "{texto}" no es válido.'
                  f' {titulo} no debe contener:{prohibido}')
            input("Aprieta enter para continuar.")
        else:
            return texto
