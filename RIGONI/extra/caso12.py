excursiones = []
cupos = []
opcion = ''

while opcion != 9:
    print('\n1. Ingresar excursiones')
    print('2. Ingresar cupos por excursión')
    print('3. Mostrar oferta/cupos')
    print('4. Consultar cupo por nombre')
    print('5. Listar excursiones sin cupo')
    print('6. Agregar excursión')
    print('7. Actualizar cupos: ')
    print('8. Ver todas excursiones')
    print('9. Salir')
    opcion = input('Ingrese una opción: ')

    if not opcion.isdigit():
        print('ERROR. Valor inválido.')
        continue
    else:
        opcion = int(opcion)
        if opcion == 1:
            cant = input('Ingrese la cantidad de excursiones que desea agregar: ')
            if cant.isdigit():
                cant = int(cant)
                for i in range(cant):
                    excursion_usuario = input('Ingrese el nombre de la excursion: ').lower()
                    excursiones.append(excursion_usuario)
                    cupos.append(0)
            else:
                print('ERROR. Valor inválido.')

        elif opcion == 2:
            if excursiones:
                for i in range(len(excursiones)):
                    cupo_usuario = input(f'Ingrese la cantidad de cupos para {excursiones[i]}: ')
                    if cupo_usuario.isdigit():
                        cupos[i] = int(cupo_usuario)
                    else:
                        print('ERROR. Valor inválido.')
            else:
                print('No hay excursiones registradas.')

        elif opcion == 3:
            if excursiones:
                for i in range(len(excursiones)):
                    print(f'Excursión: {excursiones[i]}, Cupos: {cupos[i]}')
            else:
                print('No hay excursiones registradas.')

        elif opcion == 4:
            if excursiones:
                excursion_usuario = input('Ingrese el nombre de una excursión: ').lower()
                if excursion_usuario in excursiones:
                    ind = excursiones.index(excursion_usuario)
                    print(f'Excursión: {excursion_usuario}, Cupos: {cupos[ind]}')
                else:
                    print(f'No se encontró la excursión {excursion_usuario}')
            else:
                print('No hay excursiones registradas.')

        elif opcion == 5:
            if excursiones:
                agotados = False
                print('Excursiones sin cupo: ')
                for i in range(len(excursiones)):
                    if cupos[i] == 0:
                        print(excursiones[i])
                        agotados = True
                if not agotados:
                    print('No hay excursiones sin cupo.')
            else:
                print('No hay excursiones registradas.')

        elif opcion == 6:
            excursion_usuario = input('Ingrese el nombre de la excursion: ').lower()
            excursiones.append(excursion_usuario)
            cupos.append(0)

        elif opcion == 7:
            if excursiones:
                excursion_usuario = input('Ingrese la excursión para cambiar sus cupos: ')
                if excursion_usuario in excursiones:
                    ind = excursiones.index(excursion_usuario)
                    cambiar_cupo = input(f'Ingrese la cantidad de cupos nuevos para {excursion_usuario}: ')
                    if cambiar_cupo.isdigit():
                        cupos[ind] = int(cambiar_cupo)
                    else:
                        print('ERROR. Valor inválido.')
                else:
                    print(f'No se encontró la excursión {excursion_usuario}')
            else:
                print('No hay excursiones registradas.')

        elif opcion == 8:
            if excursiones:
                for i in range(len(excursiones)):
                    print(f'Excursión: {excursiones[i]}, Cupos: {cupos[i]}')
            else:
                print('No hay excursiones registradas.')

        elif opcion == 9:
            print('Saliendo del programa...')

        else:
            print('Valor fuera de rango.')



