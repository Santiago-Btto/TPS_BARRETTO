#Ejercicio 1:
print("EJERCICIO 1")
print("Hola Mundo!")

print("") # Espacio

#Ejercicio 2:
print("EJERCICIO 2")
name = input("Ingrese su nombre: ")
print("Hola, " + name + "!") #o print(f"Hola {name}!")

print("") # Espacio

#Ejercicio 3:
print("EJERCICIO 3")
name = input("Ingrese su nombre: ")
surname = input("Ingrese su apellido: ")
year = input("Ingrese su edad: ")
residence = input("Ingrese su lugar de residencia: ")

print(f"Soy {name} {surname}, tengo {year} años y vivo en {residence}")

print("") # Espacio

#Ejercicio 4:
print("EJERCICIO 4")
radio = float(input("Ingrese el radio del circulo: ")) # sino cambiar 3.14 por math.py (si colocamos import math)
area = 3.14 * (radio)**2 
perimetro = 2 * 3.14 * radio
print(f"El area del circulo es: {area}, y su perimetro es {perimetro}")

print("") # Espacio

#Ejercicio 5:
print("EJERCICIO 5")
seconds = int(input("Ingrese los segundos: "))
minutes = seconds / 60
hours = round(minutes / 60, 2) # round() para redondear y despues de la , cuantos decimales

print(f"{seconds} segundos, equivale a {hours} horas")

print("") # Espacio

#Ejercicio 6:
print("EJERCICIO 6")
num = int(input("Ingrese un numero para ver su tabla de multiplicar: "))

num_x0 = num * 0
num_x1 = num * 1
num_x2 = num * 2
num_x3 = num * 3
num_x4 = num * 4
num_x5 = num * 5
num_x6 = num * 6
num_x7 = num * 7
num_x8 = num * 8
num_x9 = num * 9

""" for i in range(11): #0 a 10
    print(f"{num} x {i} = {num * i} ") """
print(f"""
{num} x 0 = {num_x0}
{num} x 1 = {num_x1}
{num} x 2 = {num_x2}
{num} x 3 = {num_x3}
{num} x 4 = {num_x4}
{num} x 5 = {num_x5}
{num} x 6 = {num_x6}
{num} x 7 = {num_x7}
{num} x 8 = {num_x8}
{num} x 9 = {num_x9}
""")

print("") # Espacio

#Ejercicio 7:
print("EJERCICIO 7")
num_a = 1
num_b = 1
""" while num_a == 0: """
num_a = float(input("Ingrese el primer numero DISTINTO de 0: "))
"""while num_b == 0:"""
num_b = float(input("Ingrese el segundo numero DISTINTO de 0: ")) 

print(f"{num_a} + {num_b} = {num_a+num_b}")
print(f"{num_a} / {num_b} = {num_a/num_b}")
print(f"{num_a} x {num_b} = {num_a*num_b}")
print(f"{num_a} - {num_b} = {num_a-num_b}")

print("") # Espacio

#Ejercicio 8: 
print("EJERCICIO 8")
height = float(input("Ingrese su altura en metros: "))
weight = float(input("Ingrese su peso en kilogramo: "))

imc = round(weight / (height**2), 2)

print(f"Su indice de masa corporal es de: {imc}")

print("") # Espacio

#Ejercicio 9:
print("EJERCICIO 9")
celsius = float(input("Ingrese la temperatura en grados Celsius: "))
fahrenheit = round((9/5 * celsius + 32), 2)

print(f"Su equivalente en grados Fahrenheit es de: {fahrenheit} °F")

print("") # Espacio

#Ejercicio 10:
print("EJERCICIO 10")
num_a = float(input("Ingrese el primer numero: "))
num_b = float(input("Ingrese el segundo numero: "))
num_c = float(input("Ingrese el tercer numero: "))
total_num = 3
prom = round((num_a + num_b + num_c) / total_num, 2)

print(f"El promedio de dichos numeros es de: {prom}")