titulos = []
ejemplares = []
opcion = ''

while opcion != 8:
    print('\n1. Ingresar títulos')
    print('2. Ingresar ejemplares')
    print('3. Mostrar catálogo')
    print('4. Consultar disponibilidad')
    print('5. Listar agotados')
    print('6. Agregar título')
    print('7. Actualizar ejemplares (préstamo/devolución)')
    print('8. Salir')

    opcion = input('\nIngrese la opcion: ')
    if not opcion.isdigit():
        print('ERROR. Valor invalido.')
        continue
    else:
        opcion = int(opcion)

        if opcion == 1:
            cant = input('Ingrese la cantidad de libros que desea agregar: ')
            if cant.isdigit():
                cant = int(cant)
                for i in range(cant):
                    titulo_usuario = input('Ingrese el título del libro que desea agregar: ').lower()
                    if not titulo_usuario in titulos:
                        if titulo_usuario != "":
                            titulos.append(titulo_usuario)
                            ejemplares.append(0) # Se inicializa con 0 ejemplares
                        else:
                            print('Titulo vacio.')
                    else:
                        print(f'El titulo {titulo_usuario} ya se encuentra registrado.')
            else:
                print('ERROR. Valor invalido.')

        elif opcion == 2:
            if titulos:
                for i in range(len(titulos)):
                    ejemplar_usuario = input(f'Ingrese la cantidad de copias para {titulos[i]}: ').lower()
                    if ejemplar_usuario.isdigit():
                        ejemplar_usuario = int(ejemplar_usuario)
                        ejemplares[i] = ejemplar_usuario
                    else:
                        print('Valor inválido.')
            else:
                print('No hay libros registrados')

        elif opcion == 3:
            if titulos:
                for i in range(len(titulos)):
                    print(f'Título: {titulos[i]} | Copias: {ejemplares[i]}')
            else:
                print('No hay libros registrados')

        elif opcion == 4:
            if titulos:
                titulo_usuario = input('Ingrese el título que desea buscar: ').lower()
                if titulo_usuario in titulos:
                    ind = titulos.index(titulo_usuario)
                    print(f'Título: {titulo_usuario} | Copias: {ejemplares[ind]}')
                else:
                    print(f'No se encontró el libro {titulo_usuario}')
            else:
                print('No hay libros registrados')

        elif opcion == 5:
            if titulos:
                print('Títulos agotados: ')
                for i in range(len(titulos)):
                    if ejemplares[i] == 0:
                        print(f'Título: {titulos[i]}')
            else:
                print('No hay libros registrados')

        elif opcion == 6:
            titulo_usuario = input('Ingrese el nombre del título a agregar: ').lower()
            if titulo_usuario in titulos:
                print('El titulo ya se encuentra registrado.')
            else:
                titulos.append(titulo_usuario)
                ejemplares.append(0)

        elif opcion == 7:
            if titulos:
                opcion_usuario = input('Si desea actualizar un préstamo ingrese "p" | Si desea actualizar una devolución ingrese "d": ').lower()
                if opcion_usuario == 'p':
                    titulo_usuario = input('Que libro desea prestar: ').lower()
                    if titulo_usuario in titulos:
                        ind = titulos.index(titulo_usuario)
                        if ejemplares[ind] > 0:
                            ejemplares[ind] -= 1
                        else:
                            print(f'No hay suficientes ejemplares para prestar de {titulo_usuario}')
                    else:
                        print(f'No se encontró el libro: {titulo_usuario}')

                if opcion_usuario == 'd':
                    titulo_usuario = input('Que libro se va a devolver: ').lower()
                    if titulo_usuario in titulos:
                        ind = titulos.index(titulo_usuario)
                        ejemplares[ind] += 1
                    else:
                        print(f'No se encontró el libro: {titulo_usuario}')

                else:
                    print('Valor inválido.')
            else:
                print('No hay libros registrados')

        elif opcion == 8:
            print('Saliendo del programa...')

        else:
            print('Valor fuera de rango.')
            continue

