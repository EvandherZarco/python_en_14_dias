#Programa elaborado por Zarco Hernandez Evandher Joel
#Este programa pedirá un número e imprimirá si es par o impar

numero = " "
numero_decimal = 0


numero = input("Ingresa un número: ")
numero_decimal = int(numero)

residuo = numero_decimal%2

if (residuo == 0):
    print("El número es par uwu")

elif(residuo > 0):
    print("El número es impar uwu")


