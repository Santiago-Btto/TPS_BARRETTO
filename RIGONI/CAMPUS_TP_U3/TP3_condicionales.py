##EJERCICIO 1
print('EJERCICIO 1')

user_year = int(input('Ingrese su edad: '))
if user_year > 17:
    print('Es mayor de edad')

print('') # Espacio


#EJERCICIO 2
print('EJERCICIO 2')

user_note = int(input('Ingrese su nota: '))
if user_note >= 6:
    print('Aprobado') #Mayor igual a 6 (6 a infinito)
else:
    print('Desaprobado') 

print('') # Espacio


#EJERCICIO 3
print('EJERCICIO 3')

user_number = int(input('Ingrese un numero entero: ')) # Los numeros decimales no pueden ser pares ni impares
if user_number % 2 == 0:
    print('Ha ingresado un número par')
else:
    print('Por favor, ingrese un número par')

print('') # Espacio


#EJERCICIO 4
print('EJERCICIO 4')

user_year4 = int(input('Ingrese su edad: '))
if user_year4 < 12: # Si pone valores negativos tambien entran aqui
    print('Niño/a')
elif 12 <= user_year4 < 18: # Me ahorro el uso de and
    print('Adolescente')
elif 18 <= user_year4 < 30:
    print('Adulto/a joven')
else:
    print('Adulto/a')  
    

print('') # Espacio


#EJERCICIO 5
print('EJERCICIO 5')

user_password = input('Ingrese una contraseña de entre [8 y 14] caracteres: ')

if 8 <= len(user_password) <= 14:
    print('Ha ingresado una contraseña correcta')
else:
    print('Por favor, ingrese una contraseña de entre 8 y 14 caracteres')


print('') # Espacio

#EJERCICIO 6
print('EJERCICIO 6') # Usamos español en las variables solo en este ejercicio

from statistics import mode, median, mean #moda, mediana, media
import random

numeros_aleatorios = [random.randint(1, 100) for i in range(50)] #Crea una lista con 50 numeros del 1 al 100 aleatorios

moda_aleatoria = mode(numeros_aleatorios)
mediana_aleatoria = median(numeros_aleatorios)
media_aleatoria = mean(numeros_aleatorios)

# Para verificar
""" print(f"Moda: {moda_aleatoria}")
print(f"Mediana: {mediana_aleatoria}")
print(f"Media: {media_aleatoria}") """

if (media_aleatoria > mediana_aleatoria) and (mediana_aleatoria > moda_aleatoria):
    print('Sesgo positivo o a la derecha')
elif (media_aleatoria < mediana_aleatoria) and (mediana_aleatoria < moda_aleatoria):
    print('Sesgo negativo o a la izquierda')
else:
    print('Sin sesgo')


print('') # Espacio

#EJERCICIO 7
print('EJERCICIO 7')

phrase = input('Ingrese una frase o palabra: ')

last_letter = phrase[-1].lower() # Localizar la ultima letra con indice [-1] 

if last_letter in 'a e i o u':
    phrase += '!' # Signo de exclamacion al final {tambien el += se puede usar con strings}
    print(phrase)
else:
    print(phrase)


print('') # Espacio

#EJERCICIO 8
print('EJERCICIO 8')

user_name = input('Ingrese su nombre: ')
option_number = input ('Ingrese el numero\n ' 
'1: Si quiere su nombre en mayúsculas\n ' 
'2: Si quiere su nombre en minúsculas\n ' 
'3: Si quiere su nombre con la primera letra mayúscula \n ')

if option_number == '1':
    print(user_name.upper())
elif option_number == '2':
    print(user_name.lower())
elif option_number == '3':
    print(user_name.title())

print('') # Espacio

#EJERCICIO 9
print('EJERCICIO 9')

earthquake_magnitude = float(input('Ingrese la magnitud del terremoto: '))

#Escala Richter
if earthquake_magnitude < 3:
    magnitude = '"Muy leve" (imperceptible)'
elif  earthquake_magnitude < 4:
    magnitude = '"Leve" (ligeramente perceptible).'
elif earthquake_magnitude < 5:
    magnitude = '"Moderado" (sentido por personas, pero generalmente no causa daños).'
elif earthquake_magnitude < 6:
    magnitude = '"Fuerte" (puede causar daños en estructuras débiles).'
elif earthquake_magnitude < 7:
    magnitude = '"Muy Fuerte" (puede causar daños significativos).'
else:
    magnitude = '"Extremo" (puede causar graves daños a gran escala).' 

print(magnitude)

print('') # Espacio

#EJERCICIO 10
print('EJERCICIO 10')

hemisphere = input('¿En cual hemisferio se encuentra? (N/S):').lower()
user_month = input('Ingrese que mes del año es: ').lower()
user_day = int(input('Ingrese que dia es: '))

month = { # Diccionario de meses
    'enero': 1,
    'febrero': 2,
    'marzo': 3, 
    'abril': 4,
    'mayo': 5,
    'junio': 6,
    'julio': 7,
    'agosto': 8,
    'septiembre': 9,
    'octubre': 10,
    'noviembre': 11,
    'diciembre': 12
}

# Convertimos el mes a número usando el diccionario
month_num = month.get(user_month, 0) # Busca en el diccionario la 'clave' con el mes q escribio el usuario

if hemisphere == 'n':
    if (month_num == 12 and user_day >= 21) or month_num in [1, 2] or (month_num == 3 and user_day <= 20): # verifica si es diciembre 21 >= | O enero o febrero | O marzo <= 20
        season = "Invierno"
    elif (month_num == 3 and user_day >= 21) or month_num in [4, 5] or (month_num == 6 and user_day <= 20):
        season = "Primavera"
    elif (month_num == 6 and user_day >= 21) or month_num in [7, 8] or (month_num == 9 and user_day <= 20):
        season = "Verano"
    else:
        season = "Otoño"

if hemisphere == 's':
    if (month_num == 12 and user_day >= 21) or month_num in [1, 2] or (month_num == 3 and user_day <= 20): # verifica si es diciembre 21 >= | O enero o febrero | O marzo <= 20
        season = "Verano"
    elif (month_num == 3 and user_day >= 21) or month_num in [4, 5] or (month_num == 6 and user_day <= 20):
        season = "Otoño"
    elif (month_num == 6 and user_day >= 21) or month_num in [7, 8] or (month_num == 9 and user_day <= 20):
        season = "Invierno"
    else:
        season = "Primavera"

#Se repite el codigo y solo cambia el hemisferio, se puede simplificar

print(f'Usted se encuentra en: {season}')

print('') # Espacio