import random

# Lista de jugadores de fútbol (en minúscula para evitar problemas con las comparaciones)
player_list = [
    "messi", "maradona", "pele", "ronaldo", "zidane", "cruyff",
    "puskas", "platini", "beckenbauer", "ronaldinho", "neymar",
    "suarez", "vanbasten", "kaka", "garrincha",
    "pirlo", "buffon", "savic", "pepe"
]

# Función para seleccionar un jugador al azar
def player_select():
    return random.choice(player_list)

# Función para crear la matriz de guiones bajos
def matrix_create(word):
    return ["_" if letter != " " else " " for letter in word]

# Función para mostrar el estado actual de la palabra
def show_matrix(matrix):
    return " ".join(matrix)

# Función principal del juego
def game():
    player_selected = player_select()
    matrix = matrix_create(player_selected)
    tries = 6
    guessed_letters = []

    print("\n  Bienvenido al game del Ahorcado: ¡Adivina el Jugador de Fútbol!")
    print(f"\nLa palabra tiene {len(player_selected)} letters.")

    while tries > 0:
        print("\nEstado actual del jugador:")
        print(show_matrix(matrix))
        print("\nLetras adivinadas:", ", ".join(sorted(guessed_letters)))

        # Pedir letra valida
        while True:
            letter = input(f"🔤 Te quedan {tries} intentos. Ingresa una letra: ").lower()
            if len(letter) != 1 or not letter.isalpha():
                print("❌ Por favor, ingresa solo una letra válida.")
            elif letter in guessed_letters:
                print(f"⚠️ Ya adivinaste la letra '{letter}'. Intenta con otra.")
            else:
                break

        guessed_letters.append(letter)

        if letter in player_selected:
            print(f"\n✅ ¡Bien! La letter '{letter}' está en la palabra.")
            for i, char in enumerate(player_selected):
                if char == letter:
                    matrix[i] = letter
        else:
            tries -= 1
            print(f"❌ La letra '{letter}' no está en la palabra. Te quedan {tries} intentos.")

        if "_" not in matrix:
            print("\n🎉 ¡Felicidades! Has adivinado el jugador:", player_selected.upper())
            break

    if tries == 0:
        print("\n💀 ¡Se acabaron los intentos! El jugador era:", player_selected.upper())
        print("🛑 ¡PERDISTE!")

    # Preguntar si desea volver a jugar
    while True:
        play_again = input("\n¿Quieres jugar otra vez? (s/n): ").lower()
        if play_again == "s":
            game()  # Recursivamente reiniciar el juego
            break
        elif play_again == "n":
            print("👋 ¡Gracias por jugar! Hasta la próxima.")
            break
        else:
            print("Por favor, responde con 's' o 'n'")

# Ejecutar el juego
game()
