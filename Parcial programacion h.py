import os
import csv

def crear_directorio(ruta):
    if not os.path.exists(ruta):
        os.makedirs(ruta)

def crear_csv_si_no_existe(archivo):
    if not os.path.exists(archivo):
        with open(archivo, "w", newline="", encoding="utf-8") as f:
            escritor = csv.DictWriter(f, fieldnames=["nombre", "precio", "stock"])
            escritor.writeheader()

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

def leer_csv(archivo):
    items = []
    with open(archivo, newline="", encoding="utf-8") as f:
        lector = csv.DictReader(f)
        for fila in lector:
            fila["precio"] = float(fila["precio"])
            fila["stock"] = int(fila["stock"])
            items.append(fila)
    return items

def recorrer_recursivo(ruta_base):
    lista = []
    for elemento in os.listdir(ruta_base):
        ruta = os.path.join(ruta_base, elemento)
        if os.path.isdir(ruta):
            lista += recorrer_recursivo(ruta)
        elif ruta.endswith(".csv"):
            partes = ruta.split(os.sep)
            if len(partes) >= 4:
                categoria = partes[-4]
                marca = partes[-3]
                modelo = partes[-2]
                items = leer_csv(ruta)
                for i in items:
                    i["categoria"] = categoria
                    i["marca"] = marca
                    i["modelo"] = modelo
                    lista.append(i)
    return lista

def mostrar_items():
    if not os.path.exists("datos"):
        print("sin datos")
        return
    lista = recorrer_recursivo("datos")
    if not lista:
        print("sin productos")
        return
    for i in lista:
        print(f'{i["categoria"]} | {i["marca"]} | {i["modelo"]} | {i["nombre"]} | ${i["precio"]} | stock: {i["stock"]}')
    filtrar = input("filtrar por categoria? (s/n): ").lower()
    if filtrar == "s":
        cat = input("categoria: ").strip().lower()
        filtrados = [i for i in lista if i["categoria"].lower() == cat]
        for i in filtrados:
            print(f'{i["categoria"]} | {i["marca"]} | {i["modelo"]} | {i["nombre"]} | ${i["precio"]} | stock: {i["stock"]}')

def modificar_item():
    lista = recorrer_recursivo("datos")
    nombre = input("nombre del producto a modificar: ").strip()
    encontrado = None
    for i in lista:
        if i["nombre"].lower() == nombre.lower():
            encontrado = i
            break
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
    encontrado["precio"] = nuevo_precio
    encontrado["stock"] = nuevo_stock
    ruta = os.path.join("datos", encontrado["categoria"], encontrado["marca"], encontrado["modelo"], "productos.csv")
    todos = [i for i in leer_csv(ruta) if i["nombre"].lower() != nombre.lower()]
    todos.append({"nombre": encontrado["nombre"], "precio": nuevo_precio, "stock": nuevo_stock})
    with open(ruta, "w", newline="", encoding="utf-8") as f:
        escritor = csv.DictWriter(f, fieldnames=["nombre", "precio", "stock"])
        escritor.writeheader()
        escritor.writerows(todos)
    print("producto modificado")

def eliminar_item():
    lista = recorrer_recursivo("datos")
    nombre = input("nombre del producto a eliminar: ").strip()
    encontrado = None
    for i in lista:
        if i["nombre"].lower() == nombre.lower():
            encontrado = i
            break
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

def estadisticas():
    if not os.path.exists("datos"):
        print("sin datos")
        return
    lista = recorrer_recursivo("datos")
    if not lista:
        print("sin productos")
        return
    total = len(lista)
    promedio = sum(i["precio"] for i in lista) / total
    print(f"total de productos: {total}")
    print(f"precio promedio: {promedio:.2f}")
    categorias = {}
    for i in lista:
        cat = i["categoria"]
        categorias[cat] = categorias.get(cat, 0) + 1
    for c, n in categorias.items():
        print(f"{c}: {n} productos")

def ordenar_items():
    lista = recorrer_recursivo("datos")
    if not lista:
        print("sin productos")
        return
    criterio = input("ordenar por (nombre/precio): ").strip().lower()
    if criterio not in ["nombre", "precio"]:
        print("criterio invalido")
        return
    lista_ordenada = sorted(lista, key=lambda x: x[criterio])
    for i in lista_ordenada:
        print(f'{i["nombre"]} | {i["precio"]} | {i["stock"]}')

def menu():
    while True:
        print("\n1. agregar producto")
        print("2. mostrar productos")
        print("3. modificar producto")
        print("4. eliminar producto")
        print("5. estadisticas")
        print("6. ordenar")
        print("7. salir")
        op = input("opcion: ").strip()
        if op == "1":
            agregar_item()
        elif op == "2":
            mostrar_items()
        elif op == "3":
            modificar_item()
        elif op == "4":
            eliminar_item()
        elif op == "5":
            estadisticas()
        elif op == "6":
            ordenar_items()
        elif op == "7":
            break
        else:
            print("opcion invalida")

menu()
