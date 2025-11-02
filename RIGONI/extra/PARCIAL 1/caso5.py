platos = []
porciones = []
opcion = 0

while opcion != 9:
    print('\nSi desea salir ingrese el número 9')
    print('1. Ingresar lista de platos')
    print('2. Ingresar porciones disponibles')
    print('3. Mostrar platos con porciones')
    print('4. Consultar porciones')
    print('5. Listar agotados')
    print('6. Agregar plato')
    print('7. Vender/Devolver porcion')
    print('8. Ver platos con porciones disponibles')
    print('9. Salir')

    opcion = input('\nIngrese la opción que desea: ')
    if not opcion.isdigit():
        print('Valor inválido.')
        continue
    opcion = int(opcion)

    if opcion == 1:
        plato_usuario = input('Ingrese el plato que desea agregar: ').lower()
        platos.append(plato_usuario)
        porciones.append(0)

    elif opcion == 2:
        if platos:
            for i in range(len(platos)):
                porc_usuario = input(f'Ingrese el número de porciones disponibles para el plato {platos[i]}: ')
                if porc_usuario.isdigit():
                    porciones[i] = int(porc_usuario)
                else:
                    print('Valor inválido.')
        else:
            print('No hay platos registrados.')

    elif opcion == 3:
        if platos:
            for i in range(len(platos)):
                print(f'{platos[i]}: {porciones[i]} porciones')
        else:
            print('No hay platos registrados.')

    elif opcion == 4:
        if platos:
            plato_usuario = input('Ingrese el plato que desea ver sus porciones: ').lower()
            if plato_usuario in platos:
                ind = platos.index(plato_usuario)
                print(f'Para el plato {plato_usuario}, hay {porciones[ind]} porciones disponibles.')
            else:
                print(f'No se encontró el plato {plato_usuario}')
        else:
            print('No hay platos registrados.')

    elif opcion == 5:
        if platos:
            print('Platos agotados:')
            agotados = False
            for i in range(len(platos)):
                if porciones[i] == 0:
                    print(platos[i])
                    agotados = True
            if not agotados:
                print('No hay platos agotados.')
        else:
            print('No hay platos registrados.')

    elif opcion == 6:
        plato_usuario = input('Ingrese el plato a agregar: ').lower()
        if plato_usuario in platos:
            print('Ese plato ya se encuentra añadido')
        else:
            platos.append(plato_usuario)
            porciones.append(0)

    elif opcion == 7:
        opcion_usuario = input('Ingrese si desea registrar la venta (v) o la devolución (d): ').lower()
        if opcion_usuario == 'v':
            venta = input('Ingrese el plato que se vendió: ').lower()
            if venta in platos:
                i = platos.index(venta)
                num_porc = input('Ingrese la cantidad de porciones que se vendió: ')
                if num_porc.isdigit():
                    num_porc = int(num_porc)
                    if 0 < num_porc <= porciones[i]:
                        porciones[i] -= num_porc
                    else:
                        print('Valor fuera de rango.')
                else:
                    print('Valor inválido.')
            else:
                print('No se encontró plato.')
        elif opcion_usuario == 'd':
            devolucion = input('Ingrese el plato que devolvieron: ').lower()
            if devolucion in platos:
                ind = platos.index(devolucion)
                dev_num = input('Ingrese el número de porciones devueltas: ')
                if dev_num.isdigit():
                    dev_num = int(dev_num)
                    if dev_num > 0:
                        porciones[ind] += dev_num
                    else:
                        print('Valor incorrecto.')
                else:
                    print('Valor inválido.')
            else:
                print('No se encontró el plato.')

    elif opcion == 8:
        if platos:
            for i in range(len(platos)):
                print(f'{platos[i]}: {porciones[i]} porciones disponibles.')
        else:
            print('No hay platos registrados.')

    elif opcion == 9:
        print('Saliendo del programa...')
    else:
        print('Valor inválido')
