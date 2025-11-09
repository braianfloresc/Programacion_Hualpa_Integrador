import os
from utilidades.archivos import leer_csv

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
