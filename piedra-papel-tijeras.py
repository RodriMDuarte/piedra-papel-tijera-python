print("\n-----------------------------------------------")
print("BIENVENIDOS AL JUEGO DE PIEDRA, PAPEL O TIJERAS")
print("-----------------------------------------------")

nombre1 = input("¿Cómo se llamará el Jugar 1: ")
nombre2 = input("¿Cómo se llamará el Jugar 2: ")

jugador1 = input("Hola, " + nombre1 + " ¿Qué eliges? Piedra, Papel o Tijera?: ").lower()
jugador2 = input("Hola, " + nombre2 + " ¿Qué eliges? Piedra, Papel o Tijera?: ").lower()


condicion1 = jugador1 == "piedra" and jugador2 == "tijeras"
condicion2 = jugador1 == "papel" and jugador2 == "piedra"
condicion3 = jugador1 == "tijeras" and jugador2 == "papel"

if jugador1 == jugador2:
    print("¡Ha sido un empate!")
elif condicion1 or condicion2 or condicion3:
    print("\nHa ganado", nombre1)
    print("\n-----------------------------------------------")
    print("FIN DE LA PARTIDA---> GRACIAS POR PARTICIPAR")
    print("-----------------------------------------------")
else:
    print("\nHa ganado", nombre2)
    print("\n-----------------------------------------------")
    print("FIN DE LA PARTIDA---> GRACIAS POR PARTICIPAR")
    print("-----------------------------------------------")