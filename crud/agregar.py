import os
import csv
from utilidades.archivos import crear_directorio, crear_csv_si_no_existe

def agregar_item():
    categoria = input("categoria: ").strip()
    marca = input("marca: ").strip()
    modelo = input("modelo: ").strip()
    nombre = input("nombre del producto: ").strip()
    precio = input("precio: ").strip()
    stock = input("stock: ").strip()

    if not categoria or not marca or not modelo or not nombre or not precio or not stock:
        print("datos invalidos")
        return

    try:
        precio = float(precio)
        stock = int(stock)
        if precio <= 0 or stock < 0:
            print("valores invalidos")
            return
    except:
        print("tipo de dato incorrecto")
        return

    ruta = os.path.join("datos", categoria, marca, modelo)
    crear_directorio(ruta)
    archivo = os.path.join(ruta, "productos.csv")
    crear_csv_si_no_existe(archivo)

    with open(archivo, "a", newline="", encoding="utf-8") as f:
        escritor = csv.DictWriter(f, fieldnames=["nombre", "precio", "stock"])
        escritor.writerow({"nombre": nombre, "precio": precio, "stock": stock})
    print("producto agregado")