import os
import csv
from utilidades.archivos import leer_csv
from utilidades.recorridos import recorrer_recursivo

def modificar_item():
    lista = recorrer_recursivo("datos")
    nombre = input("nombre del producto a modificar: ").strip()
    encontrado = next((i for i in lista if i["nombre"].lower() == nombre.lower()), None)

    if not encontrado:
        print("no encontrado")
        return

    nuevo_precio = input("nuevo precio: ").strip()
    nuevo_stock = input("nuevo stock: ").strip()

    try:
        nuevo_precio = float(nuevo_precio)
        nuevo_stock = int(nuevo_stock)
    except:
        print("datos invalidos")
        return

    ruta = os.path.join("datos", encontrado["categoria"], encontrado["marca"], encontrado["modelo"], "productos.csv")
    todos = [i for i in leer_csv(ruta) if i["nombre"].lower() != nombre.lower()]
    todos.append({"nombre": encontrado["nombre"], "precio": nuevo_precio, "stock": nuevo_stock})

    with open(ruta, "w", newline="", encoding="utf-8") as f:
        escritor = csv.DictWriter(f, fieldnames=["nombre", "precio", "stock"])
        escritor.writeheader()
        escritor.writerows(todos)

    print("producto modificado")