#Ejercicio 2 {Clase}

name = input('Ingrese su nombre: ')
surname = input('Ingrese su apellido: ')
id_patient = input('Ingrese su numero de DNI (Solo numeros): ') # 'ID' es palabra reservada

if len(id_patient) < 7 or len(id_patient)>10 or not id_patient.isdigit(): #Si es argentino
    print('DNI Invalido')
    exit()

age = int(input('Ingrese su edad: '))
health_insurance = input('¿Posee obra social? [Si/No]: ').lower() #obra social
priority = int(input(
'Ingrese su prioridad (En numero)\n ' \
'1: Emergencia\n ' 
'2: Urgencia\n ' 
'3: Control\n '))

if priority == 1:
    attention = 'Asignar a emergencia'
elif priority == 2:
    if health_insurance == 'si':
        attention = 'Turno en menos de 24 hs'
    else:
        attention = 'Turno en menos de 48 hs'
elif priority == 3:
    if age > 65:
        attention = 'Turno preferencial en 72 hs'
    else:
        attention = 'Turno normal en 7 dias'

print(f'✔ Paciente: {name} {surname}')
print(f'DNI: {id_patient}')
print(f'Edad: {age}')
print(f'Prioridad: {priority}')
print(f'Turno asignado: {attention}')
