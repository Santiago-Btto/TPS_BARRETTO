bienvenida = "--------------¡Bienvenido al juego de Bingo!--------------"
print(bienvenida)

import random

number = random.sample(range(1, 51), 25)
bingo_card = [number[i:i+5] for i in range(0, 25, 5)]

while True:
    number_draw = random.randint(1, 51) #numero sorteado
    print(f'Salió el número: {number_draw}')

    for i in range(5):
        for j in range(5):
            if number_draw == bingo_card[i][j]:
                bingo_card[i][j] = 0
                print("El número está en el cartón.")

    for i in range(5):
        for j in range(5):
            print(f"{bingo_card[i][j]:2}", end=" ")  # que se vea mas bonito la matriz
        print()

    if all(cell == 0 for row in bingo_card for cell in row):
        print("¡Bingo!")
        break

    else:
        print("El número no está en el cartón.")
        print('--------------------------------') # para 'separar'
        continue
    