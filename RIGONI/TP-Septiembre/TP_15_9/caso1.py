libros = []
ejemplares = []
opcion = 0

while opcion != 10:
    print('\n1. Ingresar títulos')
    print('2. Ingresar ejemplares por título')
    print('3. Mostrar catálogo')
    print('4. Consultar disponibilidad')
    print('5. Ver agotados')
    print('6. Agregar nuevo título')
    print('8. Actualizar ejemplares (préstamo/devolución)')
    print('9. Ver catálogo completo')
    print('10. Salir')

    try:
        opcion = int(input('\nElige una opción: '))
    except ValueError:
        print("Opción inválida. Ingresa un número.")
        continue

    if opcion == 1:
        cant = int(input('Cantidad de libros a ingresar: '))
        for i in range(cant):
            titulo = input(f'Ingrese el título del libro {i+1}: ').lower()
            if titulo not in libros:
                libros.append(titulo)
                ejemplares.append(0)
            else:
                print(f'El libro "{titulo}" ya está en la lista.')

    elif opcion == 2:
        if not libros:
            print("No hay libros. Agregue títulos primero.")
        else:
            for i in range(len(libros)):
                print(f'{libros[i]}: {ejemplares[i]} ejemplares')
            titulo = input("Ingrese el título a actualizar ejemplares: ").lower()
            if titulo in libros:
                indice = libros.index(titulo)
                cantidad = int(input(f'Cantidad de ejemplares para "{titulo}": '))
                ejemplares[indice] = cantidad
            else:
                print("El título no está registrado.")

    elif opcion == 3:
        if libros:
            for i in range(len(libros)):
                print(f'{libros[i]}: {ejemplares[i]} ejemplares')
        else:
            print("No hay libros registrados.")

    elif opcion == 4:
        titulo = input("Ingrese el título a consultar disponibilidad: ").lower()
        if titulo in libros:
            indice = libros.index(titulo) 
            print(f'{titulo}: {ejemplares[indice]} ejemplares disponibles')
        else:
            print("El título no está registrado.")


    elif opcion == 5:
        agotados = [libros[i] for i in range(len(libros)) if ejemplares[i] == 0]
        if agotados:
            print(f"Libros agotados: {agotados}")
        else:
            print("No hay libros agotados.")

    elif opcion == 6:
        nuevo_libro = input("Ingrese el título del nuevo libro: ").lower()
        if nuevo_libro not in libros:
            libros.append(nuevo_libro)
            print(f'Libro "{nuevo_libro}" agregado.')
            nuevo_ejemplar = int(input(f'Cantidad de ejemplares para "{nuevo_libro}": '))
            ejemplares.append(nuevo_ejemplar)
        else:
            print(f'El libro "{nuevo_libro}" ya existe.')

    elif opcion == 8:
        titulo = input("Ingrese el título para préstamo/devolución: ").lower()
        if titulo in libros:
            indice = libros.indice(titulo)
            cambio = int(input(f'Cantidad a cambiar para "{titulo}" (positivo para devolución, negativo para préstamo): '))
            if ejemplares[indice] + cambio >= 0:
                ejemplares[indice] += cambio
                print(f'Nuevo stock de "{titulo}": {ejemplares[indice]}')
            else:
                print("Valor invalido.")
        else:
            print("El título no está registrado.")

    elif opcion == 9:
        if libros:
            for i in range(len(libros)):
                print(f'{libros[i]}: {ejemplares[i]} ejemplares')
        else:
            print("No hay libros registrados.")

    elif opcion == 10:
        print("Saliendo del programa")

    else:
        print("Opción inválida.")
