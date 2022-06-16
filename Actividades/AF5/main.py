from util.cli import menu_opciones, pedir_texto
from api import get_pokemon, post_issue, put_lock_issue, delete_lock_issue
from util.tokens import Tokens
from util.issues import Issues

tokens = Tokens()
issues = Issues()


def menu_inicial():
    if tokens:
        opciones = ["Borrar Github Token", "Probar APIs"]
    else:
        opciones = ["Ingresar Github Token"]
    opcion = -1
    while opcion != 0:
        if opcion == 1:
            if tokens:
                tokens.clear()
                return True
            else:
                tokens.append(pedir_texto("Github Token"))
                tokens.guardar()
                return True
        if opcion == 2:
            menu_partes()
        opcion = menu_opciones(titulo="Menú inicial", opciones=opciones,
                               cancelar="Salir")
    return False


def menu_partes():
    opciones = ["Get Pokemon", "Post Issue",
                "Put Lock Issue", "Delete Lock Issue"]
    opcion = -1
    pokemon = [None, None, None, [None, None]]
    tipo = None
    status = None
    while opcion != 0:
        if opcion == 1:
            status, pokemon = get_pokemon()
            tipo = "Get"
        if opcion == 2:
            status, numero_issue = post_issue(tokens[-1], pokemon)
            if numero_issue > 0:
                issues.append(numero_issue)
                issues.guardar()
            tipo = "Post"
        if opcion == 3:
            if issues:
                status = put_lock_issue(tokens[-1], issues[-1])
                tipo = "Put"
        if opcion == 4:
            if issues:
                status = delete_lock_issue(tokens[-1], issues[-1])
                tipo = "Delete"

        descripcion = f"\tPokemón: {pokemon}\n"
        descripcion += f"\tIssue: {str(issues[-1] if issues else None)}\n"
        descripcion += f"\tResult: {tipo} -> {str(status)}"
        opcion = menu_opciones(titulo="Probar APIs", descripcion=descripcion,
                               opciones=opciones, cancelar="Regresar")


if __name__ == '__main__':
    while menu_inicial():
        pass
