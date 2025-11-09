import os
from utilidades.recorridos import recorrer_recursivo

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