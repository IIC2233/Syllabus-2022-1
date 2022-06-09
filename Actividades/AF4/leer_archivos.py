from ayudantes import Ayudante, Plato
from supermercado import Pasillo, ListaPasillos


def cargar_platos(path):
    with open(path, 'r') as file:
        platos_raw = file.readlines()[1:]

    platos = []
    for plato in platos_raw:
        p = plato.strip()
        p = p.split(',')
        platos.append(p)

    platos_dict = {}

    for plato in platos:
        nombre = plato[0]
        ing = plato[1:]
        ingredientes = []
        for i in ing:
            l = i.split(';')
            l[1] = int(l[1])
            l = tuple(l)
            ingredientes.append(l)

        platos_dict[nombre] = ingredientes

    platos_instances = {}

    for k, v in platos_dict.items():
        platos_instances[k] = Plato(nombre=k, ingredientes=v)

    return platos_instances


def cargar_ayudantes(path, platos_instances):
    with open(path, 'r') as file:
        ayudante_raw = file.readlines()[1:]

    ayudantes = []
    for cocinero in ayudante_raw:
        l = cocinero.strip()
        l = l.split(',')
        ayudantes.append(l)

    ayudante_instances = []
    for c in ayudantes:
        nombre = c[0]
        platos = c[1:-1]
        dinero = int(c[-1])
        instances = []
        for p in platos:
            instances.append(platos_instances[p])

        cocinero = Ayudante(nombre, instances, dinero)
        ayudante_instances.append(cocinero)

    return ayudante_instances


def cargar_pasillos(path, productos):  # lista ligada de pasillos (primer elemento)
    with open(path, 'r') as file:
        pasillos_raw = file.readlines()[1:]

    pasillos = []
    for pasillo in pasillos_raw:
        p = pasillo.strip()
        p = p.split(',')
        pasillos.append(p)

    pasillos_instances = []

    for pasillo in pasillos:
        id = int(pasillo[0])
        nombre = pasillo[1]
        pasillo_inst = Pasillo(id, nombre)
        pasillo_inst.productos = []
        for producto in productos:
            if productos[producto][0] == pasillo_inst.id:
                pasillo_inst.productos.append(producto)
        pasillos_instances.append(pasillo_inst)

    for i in range(len(pasillos_instances)):
        if i < len(pasillos_instances) - 1:
            pasillos_instances[i].siguiente = pasillos_instances[i + 1]

    return ListaPasillos(pasillos_instances[0])


def cargar_productos(path):
    with open(path, 'r') as file:
        productos_raw = file.readlines()[1:]

    productos = []
    for producto_raw in productos_raw:
        i = producto_raw.strip()
        i = i.split(',')
        productos.append(i)

    productos_dict = {}

    for producto in productos:
        pasillo = int(producto[0])
        nombre = producto[1]
        precio = int(producto[2])
        productos_dict[nombre] = (pasillo, precio)

    return productos_dict


if __name__ == "__main__":
    productos = cargar_productos('pasillos_productos.csv')
    pasillos = cargar_pasillos('pasillos.csv', productos)
    print(pasillos)
    print(productos)
    # platos_instances = cargar_platos("platos.csv")
    # cocineros_instances = cargar_cocineros("ayudantes.csv", platos_instances)
    # print(cocineros_instances[0].platos[0].ingredientes)

    # platos = cargar_platos("platos.csv")
    # print(platos["Meatballs with sauce"])
