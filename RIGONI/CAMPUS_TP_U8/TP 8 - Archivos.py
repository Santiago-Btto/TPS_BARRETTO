import os # para manejar archivos
import csv # para manejar archivos csv

# Funcion para código mas legible
def presentar_ejercicio(num):
    print('')
    print(f'Ejercicio: {num}')
    print('')
    return

# Ejercicio 1
presentar_ejercicio(1)

ARCHIVO = './productos.txt'

def inicializar_archivo():
    """Crea el archivo txt si no existe, con los encabezados 'nombre' 'precio' y 'cantidad'"""
    if not os.path.exists(ARCHIVO):
        with open(ARCHIVO, mode='w', newline='') as archivo: # 'w' para escribir, 'newline' para evitar lineas en blanco y with open para cerrar el archivo automaticamente
            writer = csv.DictWriter(archivo, fieldnames=['nombre', 'precio', 'cantidad'])
            writer.writeheader()
            writer.writerows([ 
                {'nombre': 'Lapicera', 'precio': 120.5, 'cantidad': 30},
                {'nombre': 'Goma', 'precio': 80.0, 'cantidad': 77},
                {'nombre': 'Regla', 'precio': 150.0, 'cantidad': 20}
            ])
        print("Archivo 'productos.txt' creado con 3 productos iniciales.")
    else:
        print("El archivo ya existe.")

inicializar_archivo()

# Ejercicio 2
presentar_ejercicio(2)

with open(ARCHIVO, mode = 'r', newline = '') as archivo: # 'r' para leer
    reader = csv.DictReader(archivo)
    productos = list(reader)

if productos:
    for p in productos:
        print(f'Producto: {p['nombre']} | Precio: {p['precio']} | Cantidad: {p['cantidad']}')
else:
    print('No hay productos cargados.')

# Ejercicio 3
presentar_ejercicio(3)

producto_usuario = input('Ingrese el producto, precio y cantidad separados por coma: ').strip().split(',')

if len(producto_usuario) == 3:
    nombre = producto_usuario[0].strip().capitalize()

    try:
        # validar datos
        precio = float(producto_usuario[1].strip())
        cantidad = int(producto_usuario[2].strip())

        # validar con raise
        if precio <= 0:
            raise ValueError('El precio debe ser mayor que 0.')
        if cantidad <= 0:
            raise ValueError('La cantidad debe ser mayor que 0.')

    except ValueError as e:
        print(f'Error: {e}')
    else: # por si no hay error
        with open(ARCHIVO, mode='a', newline='') as archivo:
            archivo.write(f'{nombre},{precio},{cantidad}\n')
        print(f'Producto agregado: {nombre}, ${precio}, cantidad: {cantidad}')
else:
    print('Error: Debe ingresar los tres valores separados por coma (producto, precio, cantidad).')

# Ejercicio 4
presentar_ejercicio(4)

productos = []  # lista de diccionarios

with open(ARCHIVO, mode='r', newline='') as archivo:
    lector = csv.DictReader(archivo)
    for fila in lector:
        productos.append(fila)  # agrer cada fila (diccionario) a la lista

# Mostrar productos
for p in productos:
    print(f"{p['nombre']} - ${p['precio']} - Cantidad: {p['cantidad']}")


# Ejercicio 5
presentar_ejercicio(5)

buscar_producto = input('Ingrese el nombre del producto: ').strip()
encontrado = False  # flag para saber si se encontro el producto


for p in productos:
    if p['nombre'].lower() == buscar_producto.lower():
        print(f'{p['nombre']} - ${p['precio']} - Cantidad: {p['cantidad']}')
        encontrado = True
        break

if not encontrado:
    print(f'No se encontró el producto {buscar_producto}')

# Ejercicio 6
presentar_ejercicio(6)

with open(ARCHIVO, mode='w', newline='') as archivo:
    writer = csv.DictWriter(archivo, fieldnames=['nombre', 'precio', 'cantidad'])
    writer.writeheader()
    writer.writerows(productos)

print('Archivo productos.txt actualizado correctamente.')
