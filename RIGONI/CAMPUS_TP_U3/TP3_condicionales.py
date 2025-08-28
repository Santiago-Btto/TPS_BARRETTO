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
    print('Aprobado')
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

print('') # Espacio

#EJERCICIO 10
print('EJERCICIO 10')
