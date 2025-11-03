import csv
import os

def inicializar_archivo(): # crea el archivo si no existe
    if not os.path.exists('inventario.csv'):
        with open('inventario.csv', 'w', newline='', encoding='utf-8') as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=['instrumento', 'unidades'])
            escritor.writeheader()


def cargar_datos(): # carga el archivo
    try:
        lista = [] # donde se guarda
        with open('inventario.csv', 'r', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo, fieldnames=['instrumento', 'unidades'])
            next(lector) # saltea la linea de encabezados
            for fila in lector:
                try:
                    fila['unidades'] = int(fila['unidades']) #validar datos
                    lista.append(fila)
                except ValueError:
                    print(f'Datos inválidos.')
        return lista
    except FileExistsError: # el formato o el nombre esta mal
        print('Csv incorrecto.')


def actualizar_datos(lista):
    with open('inventario.csv', 'w', newline='', encoding='utf-8') as archivo: # write ya que se actualiza la lista en memoria
        escritor = csv.DictWriter(archivo, fieldnames=['instrumento','unidades'])
        escritor.writeheader() # escribe las cabeceras
        escritor.writerows(lista)


def mostrar_inventario(lista):
    if not lista:
        print('No hay instrumentos disponibles.')
    else:
        for elem in lista:
            print(f'- {elem['instrumento'].capitalize()} - {elem['unidades']} unidades.')


def agregar_elementos(lista):
    try:
        cant_inst = int(input('Cuantos instrumentos quiere agregar? '))
        for i in range(cant_inst):
            nombre = input(f'Nombre del instrumento {i+1}: ').lower().strip()
            while True:
                cant = input('Cantidad de unidades: ')
                if cant.isdigit():
                    cant = int(cant)
                    break
            lista.append({'instrumento':nombre, 'unidades':cant})
        actualizar_datos(lista)
        return lista
    except ValueError:
        print('Debés ingresar un número entero.')


def editar_elemento(lista):
    instrumento = input('Ingrese el nombre del instrumento que quiere editar: ').lower().strip()
    for elem in lista:
        if(instrumento == elem['instrumento']):
            while True:
                try:
                    unidad = int(input('Ingrese las unidades del instrumento: '))
                    elem['unidades'] = unidad
                    actualizar_datos(lista)
                    return lista
                except ValueError:
                    print('Ingrese un número entero.')


def eliminar_elemento(lista):
    lista_nva = []
    instrumento = input('Ingrese el nombre del instrumento que quiere eliminar: ').lower().strip()
    for elem in lista:
        if(instrumento == elem['instrumento']): # Ignora el elemento 
            continue
        lista_nva.append(elem) # Actualiza la lista nueva (ignorando el elemento a eliminar)
    actualizar_datos(lista_nva)
    return lista_nva


def mostrar_sin_stock(lista):
    for elem in lista:
        if(elem['unidades'] == 0):
            print(f'- {elem['instrumento']}')


def vender_comprar(lista):
    inst = input('Qué instrumento quiere vender o comprar? ').lower().strip()
    for elem in lista:
        if inst == elem['instrumento']:
            opcion = input('Querés vender o comprar? (v/c): ').lower().strip()
            if opcion not in ('v', 'c'):
                print('Opción incorrecta.')
                return lista
            try:
                cant = int(input('Cuántas unidades? '))
                if cant <= 0:
                    print('La cantidad debe ser positiva.')
                    return lista
            except ValueError:
                print('Las unidades deben ser números enteros.')
                return lista
            if opcion == 'v':
                if elem['unidades'] < cant:
                    print('No hay unidades disponibles.')
                else:
                    elem['unidades'] -= cant
                    print('Unidades vendidas.')
            else:  # opcion == 'c'
                elem['unidades'] += cant
                print('Unidades agregadas.')
            actualizar_datos(lista)
            return lista
    print('Instrumento no encontrado.')
    return lista



def consultar_stock(lista):
    if not lista:
        print('No hay instrumentos disponibles.')
    else:
        instrumento = input('Ingrese el nombre del instrumento que quiere consultar: ').lower().strip()
        for elem in lista:
            if instrumento == elem['instrumento']:
                print(f'{elem['unidades']} unidades disponibles.')
            else:
                print('No existe ese instrumento.')


def mostrar_menu():
    print('--- MENU PRINCIPAL ---')
    print('1- Mostrar inventario.')
    print('2- Agregar instrumentos.')
    print('3- Editar unidades.')
    print('4- Eliminar instrumento.')
    print('5- Mostrar sin stock.')
    print('6- Vender / Comprar')
    print('7- Consultar stock.')
    print('8- Salir.')


def programa_principal():
    inicializar_archivo()
    inventario = cargar_datos()
    while True:
        try:
            mostrar_menu()
            opcion = int(input('Ingrese una opción: '))
            
            match opcion:
                case 1:
                    mostrar_inventario(inventario) # usar la lista en memoria
                case 2:
                    inventario = agregar_elementos(inventario)
                case 3:
                    inventario = editar_elemento(inventario)
                case 4:
                    inventario = eliminar_elemento(inventario)
                case 5:
                    mostrar_sin_stock(inventario)
                case 6:
                    inventario = vender_comprar(inventario)
                case 7:
                    consultar_stock(inventario)
                case 8:
                    print('Hasta luego.')
                    break
        except ValueError:
            print('Ingreso incorrecto.')
            
if __name__ == '__main__':
    programa_principal()