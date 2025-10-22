def presentar_ejercicio(num):
    print('')
    print(f'Ejercicio: {num}')
    print('')


# Ejercicio 1
presentar_ejercicio(1)

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

numero = int(input('Ingrese un número para calcular su factorial: '))
print(f'El factorial de {numero} es: {factorial(numero)}')


# Ejercicio 2
presentar_ejercicio(2)

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input('Ingrese la cantidad de términos de la serie de Fibonacci: '))
for i in range(n):
    print(fibonacci(i), end=' ')
print('')


# Ejercicio 3
presentar_ejercicio(3)

def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

base = int(input('Ingrese la base: '))
exponente = int(input('Ingrese el exponente: '))
print(f'{base} elevado a {exponente} es: {potencia(base, exponente)}')


# Ejercicio 4
presentar_ejercicio(4)

def a_binario(n):
    if n < 2:
        return str(n)
    else:
        return a_binario(n // 2) + str(n % 2)

numero = int(input('Ingrese un número para convertir a binario: '))
print(f'El número {numero} en binario es: {a_binario(numero)}')


# Ejercicio 5
presentar_ejercicio(5)

def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    elif palabra[0] != palabra[-1]:
        return False
    else:
        return es_palindromo(palabra[1:-1])

texto = input('Ingrese una palabra: ').lower()
if es_palindromo(texto):
    print(f'La palabra "{texto}" es un palíndromo.')
else:
    print(f'La palabra "{texto}" no es un palíndromo.')


# Ejercicio 6
presentar_ejercicio(6)

def suma_digitos(n):
    if n == 0:
        return 0
    else:
        return n % 10 + suma_digitos(n // 10)

numero = int(input('Ingrese un número para sumar sus dígitos: '))
print(f'La suma de los dígitos de {numero} es: {suma_digitos(numero)}')


# Ejercicio 7
presentar_ejercicio(7)

def hanoi(n, origen, destino, auxiliar):
    if n == 1:
        print(f'Mover disco 1 de {origen} a {destino}')
    else:
        hanoi(n - 1, origen, auxiliar, destino)
        print(f'Mover disco {n} de {origen} a {destino}')
        hanoi(n - 1, auxiliar, destino, origen)

discos = int(input('Ingrese la cantidad de discos: '))
hanoi(discos, 'A', 'C', 'B')


# Ejercicio 8
presentar_ejercicio(8)

def contar_digitos(n):
    if n < 10:
        return 1
    else:
        return 1 + contar_digitos(n // 10)

numero = int(input('Ingrese un número para contar sus dígitos: '))
print(f'El número {numero} tiene {contar_digitos(numero)} dígitos.')