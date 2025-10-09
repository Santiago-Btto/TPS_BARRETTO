# Funcion para código mas legible
def presentar_ejercicio(num):
    print('')
    print(f'Ejercicio: {num}')
    print('')
    return

#Ejercicio 1
presentar_ejercicio(1)

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

precios_frutas['Naranja'] = 1100
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

#Ejercicio 2
presentar_ejercicio(2)

precios_frutas['Banana'] = 1330
precios_frutas['Ananá'] = 1700
precios_frutas['Melón'] = 2800

#Ejercicio 3
presentar_ejercicio(3)

frutas_sin_precio = list(precios_frutas.keys()) 

""" frutas_sin_precio = []

for fruta in precios_frutas:
    frutas_sin_precio.append(fruta) """

#Ejercicio 4
presentar_ejercicio(4)

agenda = {}

# Cargar 5 contactos
for i in range(5):
    entrada = input('Ingrese el nombre del contacto y, separado por coma, su numero: ')
    partes = entrada.split(',')
    
    if len(partes) != 2:
        print('Formato incorrecto. Use el formato: nombre , numero')
        continue
    
    nombre = partes[0].strip()
    numero = partes[1].strip()
    agenda[nombre] = numero

# Consultar contacto
consulta = input('Ingrese el nombre del contacto a buscar: ').strip()

if consulta in agenda:
    print(f'El numero de {consulta} es {agenda[consulta]}')
else:
    print(f'No se encontró el contacto "{consulta}"')

#Ejercicio 5
presentar_ejercicio(5)

frase = input('Ingrese una frase: ').lower().split()
Palabras_unicas = set(frase)
Recuento = {palabra: frase.count(palabra) for palabra in Palabras_unicas}

print(f'Palabras_únicas: {Palabras_unicas}')
print(f'Recuento: {Recuento}')

#Ejercicio 6
presentar_ejercicio(6)

for i in range(3):
    alumno = input('Ingrese el nombre del alumno: ')
    tupla_notas = ()  # reiniciamos para cada alumno
    
    for j in range(3):
        try:
            nota = float(input(f'Ingrese la nota {j+1} de {alumno}: '))
            tupla_notas += (nota,)
        except ValueError:
            print('Entrada invalida. Por favor, ingrese un numero (Se asigna 0 a la nota)')
            tupla_notas += (0.0,)  # 0.0 en caso de error
            
    
    promedio = sum(tupla_notas) / len(tupla_notas) # calculamos promedio sumando las tuplas y dividiendo por el total
    print(f'El promedio de las notas de {alumno} es: {promedio:.2f}')

#Ejercicio 7
presentar_ejercicio(7)

alumnos = {
    'Parcial 1': {'Ana', 'Luis', 'Carlos', 'Marta'},
    'Parcial 2': {'Luis', 'Marta', 'Jorge', 'Pepe'}
}

parcial1 = alumnos['Parcial 1']
parcial2 = alumnos['Parcial 2']

ambos = parcial1 & parcial2 # interseccion
print(f'Alumnos que aprobaron ambos parciales: {ambos}')

solo_uno = parcial1 ^ parcial2 # diferencia simetrica
print(f'Alumnos que aprobaron solo uno de los dos parciales: {solo_uno}')

al_menos_uno = parcial1 | parcial2 # union
print(f'Alumnos que aprobaron al menos un parcial: {al_menos_uno}')

#Ejercicio 8
presentar_ejercicio(8)

supermercado = { # key nombre | value stock
    'manzana': 50,
    'banana': 30,
    'lechuga': 20,
    'tomate': 25,
    'cebolla': 15
}

consulta_8 = input('Ingrese el nombre del producto a consultar: ').lower().split()
if consulta_8 in supermercado:
    print(f'El stock de {consulta_8} es: {supermercado[consulta_8]}')
else:
    print(f'El producto {consulta_8} no se encuentra en el supermercado.')

actualizar_stock = input('Ingrese el nombre del producto para agregar su stock: ').lower().split()
if actualizar_stock in supermercado:
    try:
        cantidad = int(input(f'Ingrese la cantidad a agregar al stock de {actualizar_stock}: '))
        if cantidad < 0:
            print('La cantidad no puede ser negativa.')
        else:
            supermercado[actualizar_stock] += cantidad
            print(f'Se ha actualizado el stock de {actualizar_stock}. Nuevo stock: {supermercado[actualizar_stock]}')
    except ValueError:
        print('Entrada invalida. Por favor, ingrese un numero entero.')

agregar_producto = input('Ingrese el nombre del nuevo producto a agregar: ').lower().split()
if agregar_producto in supermercado:
    print(f'El producto {agregar_producto} ya existe en el supermercado.')
else:
    try:
        cantidad_nueva = int(input(f'Ingrese la cantidad inicial para {agregar_producto}: '))
        if cantidad_nueva < 0:
            print('La cantidad no puede ser negativa.')
        else:
            supermercado[agregar_producto] = cantidad_nueva
            print(f'Se ha agregado el producto {agregar_producto} con un stock de {cantidad_nueva}.')
    except ValueError:
        print('Entrada invalida. Por favor, ingrese un numero entero.')

#Ejercicio 9
presentar_ejercicio(9)
agenda_9 = {
    ('lunes', '10:00'): 'Reunión',
    ('martes', '15:00'): 'Clase de inglés',
    ('miércoles', '11:00'): 'Clase de yoga',
    ('jueves', '16:00'): 'Llamada con cliente',
    ('viernes', '10:00'): 'Revisión de proyecto'
}

consulta_9 = input('Ingrese el día y la hora para consultar (formato: día,hora): ').split(',')
if len(consulta_9) != 2:
    print('Formato incorrecto. Use el formato: día , hora')
else:
    dia = consulta_9[0].strip().lower()
    hora = consulta_9[1].strip()
    clave = (dia, hora)
    
    if clave in agenda_9:
        print(f'Actividad programada: {agenda_9[clave]}')
    else:
        print('No hay actividades programadas para ese día y hora.')

#Ejercicio 10
presentar_ejercicio(10)

original = {'Argentina': 'Buenos Aires', 'Chile': 'Santiago'}

# Creamos un nuevo diccionario invertido
invertido = {capital: pais for pais, capital in original.items()}

print(f'Diccionario invertido: {invertido}')





