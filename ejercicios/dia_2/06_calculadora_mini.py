#Programa elaborado por: Zarco Hernandez Evandher Joel

#Este programa ejecutará la operación aritmética básica que entre 2 números que elija el usuario. 

num_uno = int(input("Ingrese el primer número uwu: "))

num_dos = int(input("Ingrese el segundo número número uwu: "))

op = input("¿Que operación desear realizar? (+ , - , * , /): ")

match op:
    case "+":
        print("El resultado es: ", num_uno + num_dos)
    case "-":
        print("El resultado es: ", num_uno - num_dos)
    case "*":
        print("El resultado es: ", num_uno * num_dos)
    case "/":
        print("El resultado es: ", num_uno / num_dos)
    case _:
        print("Operación invalida. Intentelo de nuevo unu")
    
    


    