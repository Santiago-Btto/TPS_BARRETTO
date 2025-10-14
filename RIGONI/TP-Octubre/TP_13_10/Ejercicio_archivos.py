import csv
import os

ARCHIVO = "productos.csv"

# =================== FUNCIONES ===================

def inicializar_archivo():
    """Crea el archivo CSV si no existe, con los encabezados 'nombre' y 'precio'."""
    if not os.path.exists(ARCHIVO):
        with open(ARCHIVO, mode='w', newline='') as archivo:
            writer = csv.DictWriter(archivo, fieldnames=["nombre", "precio"])
            writer.writeheader()

def mostrar_productos():
    """Muestra todos los productos registrados y el total de precios."""
    try:
        with open(ARCHIVO, mode='r', newline='') as archivo:
            reader = csv.DictReader(archivo)
            productos = list(reader)

            if not productos:
                print("No hay productos registrados.")
                return

            total = 0
            print("Productos registrados:")
            for producto in productos:
                nombre = producto['nombre']
                precio = float(producto['precio'])
                print(f"- {nombre} → ${precio}")
                total += precio

            print(f"Total de precios: ${total}")
    except Exception as e:
        print(f"Error al leer el archivo: {e}")

def agregar_producto():
    """Agrega un nuevo producto al archivo CSV."""
    nombre = input("Ingrese el nombre del producto: ").strip()
    try:
        precio = float(input("Ingrese el precio: "))
        if precio <= 0:
            print("El precio debe ser un número positivo.")
            return
    except ValueError:
        print("Precio inválido. Debe ser un número.")
        return

    with open(ARCHIVO, mode='a', newline='') as archivo:
        writer = csv.DictWriter(archivo, fieldnames=["nombre", "precio"])
        writer.writerow({"nombre": nombre, "precio": precio})
    print("Producto agregado correctamente.")

def eliminar_producto():
    """Elimina un producto del archivo CSV si existe."""
    nombre_a_eliminar = input("Ingrese el nombre del producto a eliminar: ").strip()
    encontrado = False

    try:
        with open(ARCHIVO, mode='r', newline='') as archivo:
            productos = list(csv.DictReader(archivo))

        nueva_lista = []
        for producto in productos:
            if producto['nombre'].lower() != nombre_a_eliminar.lower():
                nueva_lista.append(producto)
            else:
                encontrado = True

        if encontrado:
            with open(ARCHIVO, mode='w', newline='') as archivo:
                writer = csv.DictWriter(archivo, fieldnames=["nombre", "precio"])
                writer.writeheader()
                writer.writerows(nueva_lista)
            print(f"Producto '{nombre_a_eliminar}' eliminado correctamente.")
        else:
            print("Producto no encontrado.")
    except Exception as e:
        print(f"Error al eliminar el producto: {e}")

def actualizar_precio():
    """Actualiza el precio de un producto existente."""
    nombre_a_actualizar = input("Ingrese el nombre del producto a actualizar: ").strip()
    encontrado = False

    try:
        with open(ARCHIVO, mode='r', newline='') as archivo:
            productos = list(csv.DictReader(archivo))

        for producto in productos:
            if producto['nombre'].lower() == nombre_a_actualizar.lower():
                try:
                    nuevo_precio = float(input("Ingrese el nuevo precio: "))
                    if nuevo_precio <= 0:
                        print("El precio debe ser positivo.")
                        return
                    producto['precio'] = str(nuevo_precio)
                    encontrado = True
                except ValueError:
                    print("Precio inválido.")
                    return
                break

        if encontrado:
            with open(ARCHIVO, mode='w', newline='') as archivo:
                writer = csv.DictWriter(archivo, fieldnames=["nombre", "precio"])
                writer.writeheader()
                writer.writerows(productos)
            print("Precio actualizado correctamente.")
        else:
            print("Producto no encontrado.")
    except Exception as e:
        print(f"Error al actualizar el producto: {e}")

# =================== MENÚ PRINCIPAL ===================

def mostrar_menu():
    print("\n====== MENÚ DE PRODUCTOS ======")
    print("1. Mostrar productos")
    print("2. Agregar producto")
    print("3. Eliminar producto")
    print("4. Actualizar precio")
    print("5. Salir")
    print("================================")

def main():
    inicializar_archivo()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == '1':
            mostrar_productos()
        elif opcion == '2':
            agregar_producto()
        elif opcion == '3':
            eliminar_producto()
        elif opcion == '4':
            actualizar_precio()
        elif opcion == '5':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

main()