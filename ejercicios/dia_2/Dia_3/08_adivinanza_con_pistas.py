#Progama elaborador por Zarco Hernandez Evandher Joel
# Este programa generará un número aleatorio y el usuario tendrá 3 intentos. 
# Se le dará al usuario una pista cada que falle (si es un número más alto o mas bajo)

import random

num_a_adivinar = random.randint(1,10)

intentos = 3


respuesta = int(input("Ingrese el número uwu: \n"))

while intentos > 0:
    if(intentos != 0):
        if respuesta == num_a_adivinar:
            print("Correcto, felicidades haz ganado uwu ")
            break
        else:
            if(respuesta < num_a_adivinar):
                print("Respuesta incorrecta. Intenta de nuevo unu .\n")
                intentos -= 1
                print("Intentos restantes: ", intentos , "\n")
                respuesta = int(input("Pista: Más alto \n"))
            else:
                print("Respuesta incorrecta. Intenta de nuevo unu .\n")
                intentos -= 1
                print("Intentos restantes: ", intentos , "\n")
                respuesta = int(input("Pista: Más bajo \n"))
    else: 
        print("Haz perdido :c ")
        

        

