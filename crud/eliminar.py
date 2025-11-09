import os
import csv
from utilidades.archivos import leer_csv
from utilidades.recorridos import recorrer_recursivo

def eliminar_item():
    lista = recorrer_recursivo("datos")
    nombre = input("nombre del producto a eliminar: ").strip()
    encontrado = next((i for i in lista if i["nombre"].lower() == nombre.lower()), None)

    if not encontrado:
        print("no encontrado")
        return

    ruta = os.path.join("datos", encontrado["categoria"], encontrado["marca"], encontrado["modelo"], "productos.csv")
    todos = [i for i in leer_csv(ruta) if i["nombre"].lower() != nombre.lower()]

    with open(ruta, "w", newline="", encoding="utf-8") as f:
        escritor = csv.DictWriter(f, fieldnames=["nombre", "precio", "stock"])
        escritor.writeheader()
        escritor.writerows(todos)

    print("producto eliminado")