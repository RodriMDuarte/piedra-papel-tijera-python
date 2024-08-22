


print("\n-----------------------------------------------")
print("BIENVENIDOS AL JUEGO DE PIEDRA, PAPEL O TIJERAS")
print("-----------------------------------------------")

nombre1 = input("¿Cómo se llamará el Jugar 1: ")
nombre2 = input("¿Cómo se llamará el Jugar 2: ")


while True:
    num_partidas = input("¿Cúantas partidas desea jugar, 3 o 5?: ")
    if int(num_partidas) in [3, 5]:
        num_partidas = int(num_partidas)
        break
    else:
        print("Por favor, ingrese 3 o 5.")

victoria_jug1 = 0
victoria_jug2 = 0

opc_valida = ["piedra", "papel", "tijera"]

for partida in range(num_partidas):
    print(f"---Partida {partida+1}---")
    
    while True:
        jugador1 = input("Hola, " + nombre1 + " ¿Qué eliges? Piedra, Papel o Tijera?: ").lower()
        if jugador1 in opc_valida:
            break
        else:
            print("Lo ingresado es incorrecto. Por favor, elige entre Piedra, Papel o Tijera.")

    while True:
        jugador2 = input("Hola, " + nombre2 + " ¿Qué eliges? Piedra, Papel o Tijera?: ").lower()
        if jugador2 in opc_valida:
            break
        else:
            print("Lo ingresado es incorrecto. Por favor, elige entre Piedra, Papel o Tijera.")


condicion1 = jugador1 == "piedra" and jugador2 == "tijera"
condicion2 = jugador1 == "papel" and jugador2 == "piedra"
condicion3 = jugador1 == "tijeras" and jugador2 == "papel"

if jugador1 == jugador2:
    print("¡Ha sido un empate!")
elif condicion1 or condicion2 or condicion3:
    print("\nHa ganado esta partida: ", nombre1)
    victoria_jug1 +=1
else:
    print("\nHa ganado esta partida: ", nombre2)
    victoria_jug2 +=1

print("RESULTADOS FINALES: ")
print(nombre1 + ", Gano: " + str(victoria_jug1) + "partidas")
print(nombre2 + ", Gano: " + str(victoria_jug2) + "partidas")

if victoria_jug1 > victoria_jug2:
    print("El ganador ha sido: ", nombre1)
else:
    print("El ganador ha sido: ", nombre2)

print("\n----------------")
print("FIN DE LA PARTIDA")
print("-----------------")