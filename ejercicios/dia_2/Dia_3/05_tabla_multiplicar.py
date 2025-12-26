#Programa elaborado por Zarco Hernandez Evandher Joel
#Este programa imprimirá la tasbla del 1 al 10 de un número "n" ingresado por el usuario

n = int(input("De que número quiere ver la tabla?"))

for i in range (1, 11):
    print(f"{n} x {i} = {n*i}")