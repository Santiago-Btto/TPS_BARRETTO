habitaciones = []  # almacenar número de habitaciones (100, 101, 102, ...)
estados = []  # almacenar estado de las habitaciones (0 desocupada, 1 ocupada)
opcion = 0

while opcion != 7:
    print('\n1. Registrar habitacion')
    print('2. Mostrar habitaciones')
    print('3. Consultar estado de una habitación')
    print('4. Consultar habitaciones libres/ocupadas')
    print('5. Agregar una habitación.')
    print('6. Cambiar estado de una habitación')
    print('7. Salir')

    try: 
        opcion = int(input('Ingrese una opcion: '))
    except ValueError:
        print('Error: Debe ingresar un numero entero')
        continue

    if opcion == 1:
        cant = input('Cuantas habitaciones desea registrar? ')
        if cant.isdigit():
            cant = int(cant)
            for i in range(cant):
                habitacion = input('Ingrese el número de la habitación: ')
                if habitacion.isdigit():
                    habitaciones.append(int(habitacion))
                    
                    estado = input(f'Ingrese para la habitación {habitacion} si está libre: 0 u ocupada: 1 : ')
                    if estado.isdigit():
                        estado = int(estado)
                        if estado in (0, 1):
                            estados.append(estado)
                        else:
                            print('Estado inválido, debe ser 0 o 1. Se marca como libre.')
                            estados.append(0)  # por defecto libre
                    else:
                        print('Estado inválido, debe ser un número. Se marca como libre.')
                        estados.append(0)
                else:
                    print('Número de habitación inválido.')
        else:
            print('Cantidad inválida.')

    elif opcion == 2:
        if habitaciones:
            print('\nListado de habitaciones:')
            for i in range(len(habitaciones)):
                estado_str = 'Libre' if estados[i] == 0 else 'Ocupada'
                print(f'Habitación {habitaciones[i]} - {estado_str}')
        else:
            print('No hay habitaciones registradas todavía.')

    elif opcion == 3:
        if habitaciones:
            buscar_habitacion = input('Ingrese el número de la habitación a buscar: ')
            if buscar_habitacion.isdigit():
                buscar_habitacion = int(buscar_habitacion)
                if buscar_habitacion in habitaciones:
                    i = habitaciones.index(buscar_habitacion)
                    estado_str = 'Libre' if estados[i] == 0 else 'Ocupada'
                    print(f'La habitación {buscar_habitacion} se encuentra: {estado_str}')
                else:
                    print('Habitación no encontrada.')
            else:
                print('Número inválido.')
        else:
            print('No hay habitaciones registradas.')

    elif opcion == 4:
        if habitaciones:
            filtro = input('Ingrese si desea ver las habitaciones libres (0) u ocupadas (1): ')
            if filtro.isdigit():
                filtro = int(filtro)
                if filtro in (0, 1):
                    print(f"\nHabitaciones {'libres' if filtro == 0 else 'ocupadas'}:")
                    for i in range(len(habitaciones)):
                        if estados[i] == filtro:
                            print(habitaciones[i])
                else:
                    print('Debe ingresar 0 o 1.')
            else:
                print('Debe ingresar un número.')
        else:
            print('No hay habitaciones registradas.')

    elif opcion == 5:
        habitacion = input('Ingrese el número de la habitación: ')
        if habitacion.isdigit():
            habitaciones.append(int(habitacion))
                    
            estado = input(f'Ingrese para la habitación {habitacion} si está libre: 0 u ocupada: 1 : ')
            if estado.isdigit():
                estado = int(estado)
                if estado in (0, 1):
                    estados.append(estado)
                else:
                    print('Estado inválido, debe ser 0 o 1. Se marca como libre.')
                    estados.append(0)  # por defecto libre
            else:
                print('Estado inválido, debe ser un número. Se marca como libre.')
                estados.append(0)
        else:
            print('Número de habitación inválido.')

    elif opcion == 6:
        if habitaciones:
            cambiar = input('Ingrese el número de la habitación a cambiar estado: ')
            if cambiar.isdigit():
                cambiar = int(cambiar)
                if cambiar in habitaciones:
                    i = habitaciones.index(cambiar)
                    nuevo_estado = input(f'Ingrese el nuevo estado para la habitación {cambiar}: 0 libre / 1 ocupada: ')
                    if nuevo_estado.isdigit() and int(nuevo_estado) in (0, 1):
                        estados[i] = int(nuevo_estado)
                        print(f'Estado de la habitación {cambiar} actualizado correctamente.')
                    else:
                        print('Estado inválido, debe ser 0 o 1.')
                else:
                    print('No se encontró la habitación.')
            else:
                print('Número de habitación inválido.')
        else:
            print('No hay habitaciones registradas.')


    elif opcion == 7:
        print('Saliendo del sistema...')
    else:
        print('Opción inválida.')
