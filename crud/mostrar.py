import os
from utilidades.recorridos import recorrer_recursivo

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