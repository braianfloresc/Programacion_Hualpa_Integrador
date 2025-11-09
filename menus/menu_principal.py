from crud.agregar import agregar_item
from crud.mostrar import mostrar_items
from crud.modificar import modificar_item
from crud.eliminar import eliminar_item
from crud.estadisticas_ordenar import estadisticas, ordenar_items

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