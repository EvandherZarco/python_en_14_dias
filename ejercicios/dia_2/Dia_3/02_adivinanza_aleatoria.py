#Programa elaborado por Zarco Hernandez Evandher Joel
#Este programa tendrá un número aleatorio que el usuario tendrá que adivinar
import random

numero_a_adivinar = random.randint(1,10)

numero_usuario = int(input("Adivina el número uwu: ").strip())

while numero_usuario != numero_a_adivinar:
    numero_usuario = int(input("Intentelo de nuevo unu: ").strip())

print("Correcto uwu")
