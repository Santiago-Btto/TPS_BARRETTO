# ======================================================================
# Sistema simple de gestión de productos (sin imports, Python 3.8+)
# - Lectura nativa (split/strip), uso de 'with'
# - Archivo CSV relativo: 'productos.csv'
# - Validación de líneas, creación de archivo si no existe
# - CRUD básico: listar, agregar, eliminar (por ID o nombre exacto)
# ======================================================================

# Ruta relativa (archivo en el mismo directorio que el script)
RUTA_ARCHIVO = "./Archivos/productos.csv"
ENCABEZADOS = "id,nombre,precio"

# -------------------------
# 1) UTILIDADES DE PARSING
# -------------------------
def _validar_y_parsear_linea(linea, num_linea):
    """
    Valida y parsea una línea CSV (id,nombre,precio).
    Retorna diccionario {'id': int, 'nombre': str, 'precio': float} o None si es inválida.
    """
    ##################### VALIDACIONES #####################################

    if linea is None:
        return None

    texto = linea.strip()
    if texto == "":
        # línea en blanco -> ignorar
        return None

    partes = [p.strip() for p in texto.split(",")]

    if len(partes) != 3:
        print(f"--- Advertencia: Línea {num_linea} descartada. Formato incorrecto (se esperaban 3 campos): {texto}")
        return None

    id_str, nombre, precio_str = partes  # CORRECCIÓN: tomar cada campo separado

    if nombre == "":
        print(f"--- Advertencia: Línea {num_linea} descartada. Nombre vacío.")
        return None
    # Validación de tipo String
    try:
        producto_id = int(id_str)
    except ValueError:
        print(f"--- Advertencia: Línea {num_linea} descartada. ID no numérico: {id_str!r}")
        return None

    if producto_id <= 0:
        print(f"--- Advertencia: Línea {num_linea} descartada. ID no positivo: {producto_id}")
        return None

    # Validación de tipo numérico flotante
    try:
        producto_precio = float(precio_str)
    except ValueError:
        print(f"--- Advertencia: Línea {num_linea} descartada. Precio no numérico: {precio_str!r}")
        return None

    if producto_precio < 0:
        print(f"--- Advertencia: Línea {num_linea} descartada. Precio negativo: {producto_precio}")
        return None

    return {"id": producto_id, "nombre": nombre, "precio": producto_precio}

############################################################################

# -------------------------
# 2) CARGA Y GUARDADO
# -------------------------
def cargar_productos(ruta_archivo):
    """
    Lee el archivo CSV, valida cada línea y devuelve la lista de productos válidos.
    Si el archivo no existe lo crea con encabezado y retorna lista vacía.

    ✅ Recomendación

    Para este tipo de ejercicios didácticos y con archivos pequeños, podés usar range() sin problema, por ejemplo:

    with open(ruta_archivo, "r", encoding="utf-8") as f:
        lineas = f.readlines()
        for i in range(1, len(lineas) + 1):
            linea = lineas[i - 1]
            # Aquí podés usar la misma lógica del código original


    Pero si querés que sea más eficiente, claro y profesional, enumerate() sigue siendo la mejor opción.

    """
    productos = []
    try:
        with open(ruta_archivo, "r", encoding="utf-8") as f:
            for i, linea in enumerate(f, start=1):
                # Detectar y saltar encabezado en caso de coincidir (insensible a mayúsculas)
                if i == 1:
                    primera = linea.strip().lower()
                    if primera == ENCABEZADOS.lower() or ("id" in primera and "nombre" in primera and "precio" in primera):
                        # es encabezado, lo saltamos
                        # print(f"Encabezado detectado en la línea 1: {linea.strip()}")
                        continue
                producto = _validar_y_parsear_linea(linea, i)
                if producto:
                    productos.append(producto)
    except FileNotFoundError:
        # Si no existe, lo creamos con encabezado y devolvemos lista vacía
        try:
            with open(ruta_archivo, "w", encoding="utf-8") as f:
                f.write(ENCABEZADOS + "\n")
            print(f"Archivo '{ruta_archivo}' no encontrado. Se creó con encabezado.")
            return []
        except OSError:
            print(f"--- ERROR CRÍTICO: No se pudo crear el archivo '{ruta_archivo}'. Verifique permisos.")
            return None
    except OSError as e:
        print(f"--- ERROR: No se pudo leer el archivo '{ruta_archivo}': {e}")
        return None

    # Opcional: advertir y eliminar IDs duplicados, manteniendo la primera aparición
    ids_vistos = set()
    productos_unicos = []
    for p in productos:
        if p['id'] in ids_vistos:
            print(f"--- Advertencia: Producto con ID duplicado {p['id']} ('{p['nombre']}') omitido.")
            continue
        ids_vistos.add(p['id'])
        productos_unicos.append(p)

    return productos_unicos


def guardar_productos(ruta_archivo, productos):
    """
    Guarda la lista completa de productos en el CSV (sobrescribe).
    Formato: id,nombre,precio (precio con 2 decimales).
    """
    try:
        with open(ruta_archivo, "w", encoding="utf-8") as f:
            f.write(ENCABEZADOS + "\n")
            for p in productos:
                # Asegurarse de que id y precio tengan formato adecuado
                try:
                    linea = f"{int(p['id'])},{p['nombre']},{float(p['precio']):.2f}\n"
                except Exception:
                    # En caso de que haya un producto mal formado, lo mostramos y lo omitimos
                    print(f"--- Advertencia: Producto mal formado omitido al guardar: {p}")
                    continue
                f.write(linea)
        # print("Datos guardados correctamente.")
    except OSError:
        print("--- ERROR: No se pudo escribir el archivo. Verifique permisos de escritura.")


# -------------------------
# 3) LÓGICA (CRUD)
# -------------------------
def _generar_id_unico(productos):
    """
    Retorna max_id + 1 o 1 si la lista está vacía. Asume que productos contiene IDs enteros válidos.
    """
    if not productos:
        return 1
    max_id = productos[0]['id']
    for p in productos:
        try:
            if p['id'] > max_id:
                max_id = p['id']
        except Exception:
            continue
    return max_id + 1


def add_producto(productos):
    """
    Interfaz para agregar un producto: pide nombre y precio, valida y persiste.
    """
    print("\n--- AGREGAR NUEVO PRODUCTO ---")
    nombre = input("Nombre: ").strip()
    if not nombre:
        print("El nombre no puede estar vacío. Operación cancelada.")
        return

    precio = None
    while precio is None:
        entrada = input("Precio: ").strip()
        try:
            precio_val = float(entrada)
            if precio_val <= 0:
                print("El precio debe ser un número positivo mayor que cero.")
            else:
                precio = precio_val
        except ValueError:
            print("Precio inválido. Ingrese un número (ej: 12.50).")

    nuevo_id = _generar_id_unico(productos)
    nuevo = {"id": nuevo_id, "nombre": nombre, "precio": precio}
    productos.append(nuevo)
    guardar_productos(RUTA_ARCHIVO, productos)
    print(f"Producto agregado: ID={nuevo_id}, Nombre='{nombre}', Precio={precio:.2f}")


def remove_producto(productos):
    """
    Permite eliminar productos por ID (único) o por nombre exacto.
    Versión simplificada para aprendizaje: usa estructuras básicas y bucles.
    """
    print("\n--- ELIMINAR PRODUCTO ---")
    modo = input("Eliminar por ID (I) o por Nombre exacto (N)? [I/N]: ").strip().upper()

    # --- Eliminación por ID ---
    if modo == "I":
        entrada = input("Ingrese ID: ").strip()
        try:
            id_elim = int(entrada)
        except ValueError:
            print("ID inválido. Debe ser un número entero.")
            return

        encontrado = False
        for p in productos:
            if p.get('id') == id_elim:
                productos.remove(p)
                encontrado = True
                break  # ID es único, no hace falta seguir buscando

        if encontrado:
            guardar_productos(RUTA_ARCHIVO, productos)
            print(f"Producto con ID {id_elim} eliminado correctamente.")
        else:
            print(f"No se encontró producto con ID {id_elim}.")

    # --- Eliminación por Nombre Exacto ---
    elif modo == "N":
        nombre = input("Ingrese nombre exacto a eliminar: ").strip()
        if not nombre:
            print("Nombre vacío. Operación cancelada.")
            return

        eliminados = 0
        # Creamos una lista temporal para evitar modificar la original mientras iteramos
        productos_a_eliminar = []
        for p in productos:
            if p.get('nombre').strip().upper() == nombre.upper():
                productos_a_eliminar.append(p)

        # Eliminamos los productos encontrados
        for p in productos_a_eliminar:
            productos.remove(p)
            eliminados += 1

        if eliminados > 0:
            guardar_productos(RUTA_ARCHIVO, productos)
            print(f"Se eliminaron {eliminados} producto(s) con el nombre '{nombre}'.")
        else:
            print(f"No se encontró ningún producto con el nombre '{nombre}'.")

    else:
        print("Opción no válida. Use 'I' o 'N'.")


def print_products(productos):
    """
    Imprime la lista de productos y muestra el total acumulado de precios.
    """
    print("\n================ PRODUCTOS =================")
    if not productos:
        print("No hay productos registrados.")
        print("===========================================")
        return

    # Ordenar por id para mostrarlos de forma coherente
    try:
        productos_ordenados = sorted(productos, key=lambda x: int(x['id']))
    except Exception:
        productos_ordenados = productos[:]  # si hay problemas, dejar el orden original

    total = 0.0
    print(f"{'ID':>4}  {'NOMBRE':<30}  {'PRECIO':>10}")
    print("-" * 50)
    for p in productos_ordenados:
        try:
            pid = int(p['id'])
            nombre = p['nombre']
            precio = float(p['precio'])
            print(f"{pid:4d}  {nombre:<30}  ${precio:10.2f}")
            total += precio
        except Exception:
            print(f"--- ERROR: producto mal formado encontrado y omitido en listado: {p}")
    print("-" * 50)
    print(f"Total acumulado: ${total:,.2f}")
    print("===========================================")


# -------------------------
# 4) INTERFAZ / MAIN
# -------------------------
def mostrar_menu():
    print("\n=== MENÚ ===")
    print("1 - Mostrar productos")
    print("2 - Agregar producto")
    print("3 - Eliminar producto (ID o Nombre)")
    print("4 - Salir")
    print("============")


def main():
    productos = cargar_productos(RUTA_ARCHIVO)
    if productos is None:
        # Error crítico leyendo/creando archivo
        return

    while True:
        mostrar_menu()
        opcion = input("Seleccione opción (1-4): ").strip()
        if opcion == "1":
            print_products(productos)
        elif opcion == "2":
            add_producto(productos)
        elif opcion == "3":
            remove_producto(productos)
        elif opcion == "4":
            print("Guardando y saliendo. ¡Hasta luego!")
            guardar_productos(RUTA_ARCHIVO, productos)
            break
        else:
            print("Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
    main()
