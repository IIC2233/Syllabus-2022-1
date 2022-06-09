import random
from parametros import PATH_PASILLOS, PATH_PRODUCTOS, PATH_AYUDANTES, PATH_PLATOS
from leer_archivos import cargar_ayudantes, cargar_productos, cargar_pasillos, cargar_platos
from supermercado import Supermercado

def imprimir_ingredientes_de_platos(ingredientes_para_platos, ayudante):

  if ingredientes_para_platos is not None:
    print("    Los ingredientes para cada plato:")
    for plato, ingredientes in zip(ayudante.platos, ingredientes_para_platos):
      print(f"        * {plato.nombre}: {', '.join(map(lambda x: x[0], ingredientes))}")
        #print(f"{ayudante.nombre} tiene que comprar {ingrediente[1]} de {ingrediente[0]}")

  else:
    print("    TODOS LOS INGREDIENTES NO IMPLEMENTADO")
  print("")
  return ingredientes_para_platos

def imprimir_lista_compras(cantidad_productos):
  
  if cantidad_productos is not None:
    print("    La lista de compras:")
    for ingrediente, cantidad in cantidad_productos:
      print(f"        * {cantidad} de {ingrediente}")
  else:
    print("    CANTIDAD DE INGREDIENTES NO IMPLEMENTADO")
  print("")

def imprimir_pasillos_a_recorrer(pasillos_a_recorrer):
  if pasillos_a_recorrer is not None:
    print("   Recorriendo los pasillos:")
    for pasillo in pasillos_a_recorrer:
      print(f"        * {pasillo.nombre}")

  else:
    print("    PASILLOS A RECORRER NO IMPLEMENTADOS")
  print("")

def imprimir_final_compra(total, ayudante):

  if total is not None:

    if total > ayudante.dinero:
      print(f"    Oh no! Al ayudante le faltan ${total - ayudante.dinero} para pagar la cuenta")
    else:
      ayudante.dinero -= total
      print(f"    El ayudante compró los productos y le sobró ${ayudante.dinero}")
  else:
    print("    TOTAL NO IMPLEMENTADO")

def imprimir_estadisticas(ayudante, ingredientes_para_platos, cantidad_productos, a_recorrer, total):
  print("-" * 50)
  print(f"Es el turno de {ayudante.nombre} de ir a comprar\n")

  imprimir_ingredientes_de_platos(ingredientes_para_platos, ayudante)

  imprimir_lista_compras(cantidad_productos)

  imprimir_pasillos_a_recorrer(a_recorrer)

  print(f"    Yendo a la caja...\n")

  imprimir_final_compra(total, ayudante)

  print("-" * 50 + "\n")

if __name__ == "__main__":
  productos = cargar_productos(PATH_PRODUCTOS)
  pasillos = cargar_pasillos(PATH_PASILLOS, productos)
  supermercado = Supermercado(pasillos, productos)
  platos = cargar_platos(PATH_PLATOS)
  ayudantes = cargar_ayudantes(PATH_AYUDANTES, platos)

  print("Comenzó la competencia! Los ayudantes van a comprar los productos para sus platos.\nEn 3...\n   2...\n   1...\n   Partieron!")
  for ayudante in ayudantes:

    ingredientes_para_platos = ayudante.obtener_ingredientes_platos()

    cantidad_productos = ayudante.cantidad_ingredientes(ingredientes_para_platos)

    pasillos_a_recorrer = supermercado.pasillos_a_recorrer(ingredientes_para_platos)

    total = ayudante.total_compra(ingredientes_para_platos, supermercado)

    imprimir_estadisticas(ayudante, ingredientes_para_platos, cantidad_productos, pasillos_a_recorrer, total)

  ganador = random.choice(ayudantes)
  print(f"{ganador.nombre} ganó la competencia de MasterDCChef")