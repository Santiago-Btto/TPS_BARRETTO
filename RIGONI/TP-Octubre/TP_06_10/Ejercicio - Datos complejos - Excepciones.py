def crear_bag(): # 1
    while True:
        try:
            bag_space = int(input('Ingrese el tamaño de la mochila (número positivo): '))
            if bag_space <= 0:
                print('Error: El tamaño debe ser un número positivo mayor que cero.')
                continue
            return [None] * bag_space  # crea lista con espacios vacíos
        except ValueError:
            print('Error: Entrada inválida. Por favor, ingrese un número entero positivo.')


def mostrar_bag(bag): # 2
    print('\nContenido de la mochila:')
    for i, item in enumerate(bag):
        if item is None:
            print(f'Espacio {i}: --- vacío ---')
        else:
            print(f'Espacio {i}: {item}')


def guardar_objeto(bag): # 3
    try:
        position = int(input(f'Ingrese la posición (0 a {len(bag)-1}) donde desea guardar el objeto: '))
        if position < 0 or position >= len(bag):
            raise IndexError('Posición fuera de rango.')
        objeto = input('Ingrese el nombre del objeto mágico: ').strip()
        if not objeto:
            print('Error: El nombre del objeto no puede estar vacío.')
            return
        bag[position] = objeto
        print(f'Objeto "{objeto}" guardado en el espacio {position}.')
    except ValueError:
        print('Error: Entrada inválida. Por favor, ingrese un número entero para la posición.')
    except IndexError as e:
        print(f'Error: {e}')


def eliminar_objeto(bag): # 4
    try:
        position = int(input(f'Ingrese la posición (0 a {len(bag)-1}) del objeto que desea eliminar: '))
        if position < 0 or position >= len(bag):
            raise IndexError('Posición fuera de rango.')
        if bag[position] is None:
            print(f'Error: No hay ningún objeto en el espacio {position} para eliminar.')
        else:
            eliminado = bag[position]
            bag[position] = None
            print(f'Objeto "{eliminado}" eliminado del espacio {position}.')
    except ValueError:
        print('Error: Entrada inválida. Por favor, ingrese un número entero para la posición.')
    except IndexError as e:
        print(f'Error: {e}')


# Programa principal
bag = crear_bag()

while True:
    print('\n--- Menú de la Mochila ---')
    print('1. Guardar objeto')
    print('2. Ver mochila')
    print('3. Salir')
    print('4. Eliminar objeto (opcional)')
    opcion = input('Elige una opción (1-4): ').strip()

    if opcion == '1':
        guardar_objeto(bag)
    elif opcion == '2':
        mostrar_bag(bag)
    elif opcion == '3':
        print('Adios!')
        break
    elif opcion == '4':
        eliminar_objeto(bag)
    else:
        print('Error: Opción inválida. Por favor, seleccione una opción del 1 al 4.')
