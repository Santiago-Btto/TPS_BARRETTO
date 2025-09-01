# FOR
# 2 equipos de 6 integrantes c/u | 1 jefe 5 oficiales

print('Ejercicio FOR')

abecedario = 'abcdefghijklmnñopqrstuvwxyz' # 27 letras

corrimiento = int(input('Ingrese el numero de corrimiento: '))


for oficial in range(1,6):
    frase = input(f'Ingrese la frase que quiere encriptar al oficial {oficial}: ').lower()
    frase_encriptada = ''

    for letra in frase:
        if letra in abecedario:
            indice_nuevo = (abecedario.index(letra) + corrimiento) % 27 # Funciona con el indice a = 0 z = 26
            letra_nueva = abecedario[indice_nuevo]
            frase_encriptada += letra_nueva
        else:
            frase_encriptada += letra

    print (f'El mensaje {oficial} encriptado es: {frase_encriptada}')


# WHILE

print('Ejercicio WHILE')

import random

from colorama import Fore, Style, init #pip install colorama

init(autoreset=True) #Inicializar colorama y se resetee conc ada print


options = ['piedra', 'papel', 'tijera']

score = 0
win = 0
lose = 0
draw = 0

option_player = ''

while option_player != 'q':
    
    option_player = input('Ingrese la opción: PIEDRA = 0 | PAPEL = 1 | TIJERA = 2 : ').lower().strip()
    print(f'{Fore.CYAN}Si desea salir, imprima la letra Q')

    if option_player == 'q':
        break # Sale del bucle

    if option_player not in ['0', '1', '2']:
        print('Opción incorrecta, coloque 0, 1, 2.')
        continue # Sigue con el bucle hasta que coloque lo de []

    # Combate
    option_bot = random.randint(0,2) # de 0 a 2
    option_player = int(option_player)

    print(f'Jugador: {options[option_player].title()} | Computadora: {options[option_bot].title()}')

    if option_bot == option_player: # EMPATE
        print(f'{Fore.YELLOW}EMPATE')
        draw += 1
        score += 1

    elif (option_bot == 0 and option_player == 2) or (option_bot == 1 and option_player == 0) or (option_bot == 2 and option_player == 1): # PERDIDA
        print(f'{Fore.RED}PERDISTE') 
        score += 1
        lose += 1

    else:
        print(f'{Fore.GREEN}GANASTE') # GANADA
        score += 1
        win += 1

print(f'FIN\nLuego de {score} partidas, usted ganó {win} veces, empató {draw} y perdió {lose}')

print(f'POR LO TANTO: ')

if lose > win:
    print(f'{Fore.RED}PERDISTE LA PARTIDA') 
elif lose < win:
    print(f'{Fore.GREEN}GANASTE LA PARTIDA')
else:
    print(f'{Fore.YELLOW}EMPATASTE LA PARTIDA')

