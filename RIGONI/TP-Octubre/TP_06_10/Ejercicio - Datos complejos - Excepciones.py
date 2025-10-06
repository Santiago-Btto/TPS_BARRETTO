def create_bag():
    print('Mochila creada correctamente.')
    return []  # mochila vacía


def show_bag(bag):
    if len(bag) == 0:
        print('La mochila está vacía.')
    else:
        print('Contenido de la mochila:')
        for i, item in enumerate(bag):
            print(f'Posición {i}: {item}')


def save_object(bag):
    objeto = input('Ingrese el nombre del objeto mágico: ').strip()
    if not objeto:
        print('Error: El nombre del objeto no puede estar vacío.')
        return
    bag.append(objeto)
    print(f'Objeto -{objeto}- guardado en la posición {len(bag)-1}.')


def delete_object(bag):
    if len(bag) == 0:
        print('Error: La mochila está vacía. No hay objetos para eliminar.')
        return
    try:
        position = int(input(f'Ingrese la posición (0 a {len(bag)-1}) del objeto que desea eliminar: '))
        if position < 0 or position >= len(bag):
            raise IndexError('Posición fuera de rango.')
        deleted_object = bag.pop(position)  # elimina directamente el objeto
        print(f'Objeto -{deleted_object}- eliminado de la posición {position}.')
    except ValueError:
        print('Error: Entrada inválida. Por favor, ingrese un número entero para la posición.')
    except IndexError as e:
        print(f'Error: {e}')


# el main()
bag = create_bag()

while True:
    print('\nMenú:')
    print('1. Guardar objeto')
    print('2. Ver mochila')
    print('3. Salir')
    print('4. Eliminar objeto')
    opcion = input('Seleccione una opción (1-4): ').strip()

    if opcion == '1':
        save_object(bag)
    elif opcion == '2':
        show_bag(bag)
    elif opcion == '3':
        print('Adios!')
        break
    elif opcion == '4':
        delete_object(bag)
    else:
        print('Error: Opción inválida. Por favor, seleccione una opción del 1 al 4.')
