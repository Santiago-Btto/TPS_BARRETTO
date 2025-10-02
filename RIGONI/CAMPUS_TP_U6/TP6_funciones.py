# Funcion para código mas legible
def presentar_ejercicio(num):
    print('')
    print(f'Ejercicio: {num}')
    print('')
    return


#Ejercicio 1
presentar_ejercicio(1)

def imprimir_hola_mundo():
    print('Hola Mundo!')
    return

imprimir_hola_mundo() # tomamos como programa principal cualquier cosa fuera de las funciones (.py)


#Ejercicio 2
presentar_ejercicio(2)

def saludar_usuario(nombre):
    print(f'Hola {nombre}!')
    return

nombre = input('Ingresa tu nombre para el saludo personalizado: ').title()
saludar_usuario(nombre)


#Ejercicio 3
presentar_ejercicio(3)

def informacion_personal(nombre, apellido, edad, residencia):
    print(f'Soy [{nombre}] [{apellido}], tengo [{edad}] años y vivo en [{residencia}]')

nombre3 = input('Ingresa tu nombre: ').title()
apellido3 = input('Ingresa tu apellido: ').title()
edad3 = int(input('Ingresa tu edad: '))
residencia3 = input('Ingresa tu residencia: ').title()

informacion_personal(nombre3, apellido3, edad3, residencia3)

#Ejercicio 4
import math
presentar_ejercicio(4)

def calcular_area_circulo(radio):
    print ('Area de un circulo:')
    print (math.pi * pow(radio, 2)) # pow (base, exponente) en vez de  radio ** 2

def calcular_perimetro_circulo(radio):
    print ('Perimetro de un circulo:')
    print (2 * math.pi * radio)

radio = int(input('Ingrese el radio: '))
calcular_area_circulo(radio)
calcular_perimetro_circulo(radio)

#Ejercicio 5
presentar_ejercicio(5)

def segundos_a_horas(segundos):
    hora = (segundos / 3600)  # 3600s = 1h   ó  round(segundos / 3600, 2)
    print(f'{segundos}s son {hora:.2f}h')

segundos = int(input('Ingrese los segundos para pasarlos a hora: '))
segundos_a_horas(segundos)

#Ejercicio 6
presentar_ejercicio(6)

def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f'{numero} x {i} = {i*numero}')


num = int(input('Ingrese un número para ver su tabla de multiplicar: '))
tabla_multiplicar(num)

#Ejercicio 7
presentar_ejercicio(7)

def operaciones_basicas(a, b):
    suma = (a + b)
    resta = (a - b)
    multiplicar = (a * b)
    if b != 0:
        dividir = (a / b)
    else:
        dividir = 'No posible'

    return (suma, resta, multiplicar, dividir) # tupla


tupla = operaciones_basicas(6, 3) # no pide ingreso de datos al usuario

print(f'Suma: {tupla[0]}')
print(f'Resta: {tupla[1]}')
print(f'Multiplicacion: {tupla[2]}')
print(f'Division: {tupla[3]:.2f}')

#Ejercicio 8
presentar_ejercicio(8)

def calcular_imc(peso, altura):  # basado en ejercicio 8 tp1

    imc = round(peso / (altura**2), 2)

    print(f"Su indice de masa corporal es de: {imc}")


altura = float(input("Ingrese su altura en metros: "))
peso = float(input("Ingrese su peso en kilogramo: "))

calcular_imc(peso, altura)

#Ejercicio 9
presentar_ejercicio(9)

def celsius_a_fahrenheit(celsius): # basado en ejercicio 9 tp1
    fahrenheit = round((9/5 * celsius + 32), 2)

    print(f"Su equivalente en grados Fahrenheit es de: {fahrenheit} °F")

temperatura = float(input("Ingrese la temperatura en grados Celsius: "))

celsius_a_fahrenheit(temperatura)

#Ejercicio 10
presentar_ejercicio(10)

def calcular_promedio(a, b, c): # basado en ejercicio 10 tp1
    total_num = 3
    prom = ((a + b + c) / total_num)

    print(f"El promedio de dichos numeros es de: {prom:.2f}")

nota1 = float(input("Ingrese el primer numero: "))
nota2 = float(input("Ingrese el segundo numero: "))
nota3 = float(input("Ingrese el tercer numero: "))

calcular_promedio(nota1, nota2, nota3)