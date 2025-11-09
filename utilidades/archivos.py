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

def leer_csv(archivo):
    items = []
    with open(archivo, newline="", encoding="utf-8") as f:
        lector = csv.DictReader(f)
        for fila in lector:
            fila["precio"] = float(fila["precio"])
            fila["stock"] = int(fila["stock"])
            items.append(fila)
    return items