#Programa elaborado por: Zarco Hernandez Evandher Joel

#Este programa recibirá 3 número e imprimirá el mayor

numero_uno = int(input("Ingresa el primer número uwu: "))
numero_dos = int(input("Ingresa el segundo número uwu: "))
numero_tres = int(input("Ingresa el tercer número uwu: "))

if(numero_uno > numero_dos and numero_uno > numero_tres):
    print("El número " , numero_uno , " es el mayor uwu")
elif(numero_dos > numero_uno and numero_dos > numero_tres):
    print("El número " , numero_dos , " es el mayor uwu")
elif(numero_tres > numero_uno and numero_tres > numero_dos):
    print("El número " , numero_tres , " es el mayor uwu")
elif(numero_uno == numero_dos and numero_uno == numero_tres):
    print("Los tres números son iguales uwu")

