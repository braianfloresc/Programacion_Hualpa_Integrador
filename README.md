# 🛒 Tienda de Productos Electrónicos

## 📘 Descripción
Este proyecto implementa un **sistema de gestión para una tienda de productos electrónicos**, desarrollado en **Python**.  
Permite **agregar, mostrar, modificar, eliminar y ordenar productos**, además de calcular estadísticas básicas como el precio promedio o el total de productos registrados.

El sistema está basado en una **estructura jerárquica de carpetas y archivos CSV**, lo que permite mantener la **persistencia de datos** sin necesidad de usar una base de datos externa.

---


## Estructura de Datos y Persistencia Jerárquica

Programacion_Hualpa_Integrador/
│
├── crud/
│   ├── agregar.py                # Funcion para agregar productos
│   ├── mostrar.py                # Funcion para mostrar productos
│   ├── modificar.py              # Funcion para modificar productos existentes
│   ├── eliminar.py               # Funcion para eliminar productos
│   └── estadisticas_ordenar.py # Funciones de estadisticas y ordenamiento
│
├── utilidades/
│   ├── archivos.py               # Manejo de directorios y archivos CSV
│   └── recorridos.py             # Recorridos recursivos de carpetas de datos
│
├── menus/
│   └── menu_principal.py         # Menú principal del sistema
│
├── datos/                        # Carpeta donde se guardan los CSV generados
│
└── main.py                       # Archivo principal de ejecución

Por ejemplo, al registrar un producto:
Categoría: Televisores
Marca: Samsung
Modelo: QLED
Nombre: SmartTV 50"

El programa creará automáticamente esta ruta:
datos/Televisores/Samsung/QLED/productos.csv


Cada archivo `productos.csv` contiene las columnas:
nombre, precio, stock



Este diseño permite **filtrar y recorrer los productos de forma recursiva**, representando la jerarquía del dominio:  
**Categoría → Marca → Modelo → Producto**.

---
 Lógica de Funcionamiento
 
- **Creación automática de directorios:**  
  Si la carpeta de una categoría, marca o modelo no existe, el programa la crea.

- **Almacenamiento en CSV:**  
  Cada modelo guarda sus productos en un archivo `productos.csv`.

- **Recorrido recursivo:**  
  Una función recorre todas las carpetas dentro de `datos/` para reconstruir la lista completa de productos.

- **Filtros y operaciones disponibles:**
  - Mostrar todos los productos o filtrar por categoría.  
  - Modificar precio o stock de un producto existente.  
  - Eliminar productos.  
  - Ordenar por nombre o precio.  
  - Calcular estadísticas generales.

---

## Instrucciones de Uso

1. **Clonar el repositorio**
   ```bash
   git clone https://github.com/usuario/tienda-electronicos.git
   cd tienda-electronicos
Ejecutar el programa

python tienda.py
Usar el menú interactivo:

1. Agregar producto
2. Mostrar productos
3. Modificar producto
4. Eliminar producto
5. Estadísticas
6. Ordenar
7. Salir
    Requisitos
Python 3.8 o superior

No requiere librerías externas (usa solo os y csv del estándar de Python)

👥 Autores
SANTINO NALDINI
BRAIAN FLORES
