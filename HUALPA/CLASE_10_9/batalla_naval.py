""" 2. Cruce de matrices (tablero naval)
Crear dos matrices 5x5:
Una representa un “océano” con barcos colocados aleatoriamente (con 1 = barco y 0 = agua). Donde el usuario no debe poder ver donde esta los barcos del otro
Otra representa los disparos de un jugador.
Cada vez que el jugador dispara, se marca con una “X” si fue acierto o “O” si fue fallo.
El juego termina cuando todos los barcos son hundidos.
👉 Similar al Bingo, pero con coordenadas y validaciones. """

import random

# -------------------------------
# Configuración
# -------------------------------
TAM = 5
MAX_BARCOS = 5

# -------------------------------
# Funciones
# -------------------------------

def crear_tablero(valor): # crea una matriz TAMxTAM inicializada con 'valor'
    return [[valor for _ in range(TAM)] for _ in range(TAM)]

def colocar_barcos(tablero):
    barcos = 0
    while barcos < MAX_BARCOS: # coloca MAX_BARCOS barcos aleatoriamente
        fila = random.randint(0, TAM - 1)
        col = random.randint(0, TAM - 1)
        if tablero[fila][col] == 0:
            tablero[fila][col] = 1
            barcos += 1

def mostrar_tablero(tablero): # muestra el tablero con índices de filas y columnas 
    
    print("  ", end="")
    for i in range(TAM):
        print(i, end=" ")
    print()
    
    for i, fila in enumerate(tablero):
        print(i, end=" ")  
        for elem in fila:
            print(elem, end=" ")
        print()  

def disparar(nombre, tablero_oculto, tablero_disparos):
    barcos_hundidos = 0
    while True: # el jugador sigue tirando hasta que falle
        try: # El bloque try sirve para intentar ejecutar código que puede fallar.
            fila = int(input(f"{nombre}, ingresá la fila (0-4): "))
            col = int(input(f"{nombre}, ingresá la columna (0-4): "))

            if not (0 <= fila < TAM and 0 <= col < TAM):
                print("❌ Coordenadas fuera del tablero.")
                continue

            if tablero_disparos[fila][col] != " ":
                print("🚫 Ya disparaste ahí.")
                continue

            if tablero_oculto[fila][col] == 1:
                print("🔥 ¡Le diste a un barco! ¡Seguí tirando!")
                tablero_disparos[fila][col] = "X"
                tablero_oculto[fila][col] = -1  # marcar barco hundido
                barcos_hundidos += 1
                # No rompemos el while, sigue tirando
            else:
                print("🌊 Agua. Fin de tu turno.")
                tablero_disparos[fila][col] = "O"
                break  # acá se termina el turno
        except ValueError: # Si ocurre el error, el programa no se corta.
            print("⚠️ Ingresá números válidos (0 a 4).")

    return barcos_hundidos


# -------------------------------
# Inicialización de tableros
# -------------------------------
barcos_j1 = crear_tablero(0)
disparos_j1 = crear_tablero(" ")
colocar_barcos(barcos_j1)

barcos_j2 = crear_tablero(0)
disparos_j2 = crear_tablero(" ")
colocar_barcos(barcos_j2)

# -------------------------------
# Juego principal
# -------------------------------
hundidos_j1 = 0
hundidos_j2 = 0
turno = 1

print("🎮 ¡Bienvenidos a Batalla Naval 2 Jugadores!\n")

while hundidos_j1 < MAX_BARCOS and hundidos_j2 < MAX_BARCOS:
    print(f"\n🎯 Turno {turno} - Jugador 1")
    print("Tablero de disparos:")
    mostrar_tablero(disparos_j1)
    hundidos_j1 += disparar("Jugador 1", barcos_j2, disparos_j1)
    if hundidos_j1 == MAX_BARCOS:
        print("\n🏆 ¡Jugador 1 ganó! Hundió todos los barcos del Jugador 2.")
        break

    print(f"\n🎯 Turno {turno} - Jugador 2")
    print("Tablero de disparos:")
    mostrar_tablero(disparos_j2)
    hundidos_j2 += disparar("Jugador 2", barcos_j1, disparos_j2)
    if hundidos_j2 == MAX_BARCOS:
        print("\n🏆 ¡Jugador 2 ganó! Hundió todos los barcos del Jugador 1.")
        break

    turno += 1

# -------------------------------
# Resultados finales
# -------------------------------
print("\n🔚 El juego ha terminado.")

print("\n📊 Disparos del Jugador 1:")
mostrar_tablero(disparos_j1)

print("\n📊 Disparos del Jugador 2:")
mostrar_tablero(disparos_j2)
