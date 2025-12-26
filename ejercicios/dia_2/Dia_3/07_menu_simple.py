#Progama elaborador por Zarco Hernandez Evandher Joel
#Este programa simulará un menu el cuál: 
# 1.Saludará al usuario
# 2. Mostrará la tabla de multiplicar que el usuario elija 
# 3. Regresa al menú principal para darle opción al usuario de elegir otro número 
# 4. Cuando el usuario ponga "Salir" el programa se detiene

salir = ""

while not salir:
    
    n = int(input("¿De que número desea su tabla? uwu \n"))

    while 0 > n:
        n = int(input("Numero invalida, ingresa un número positivo, por favor unu \n"))


    for i in range(1,11):
        print(f"{n} x {i} = {n*i}")

    salida = input("¿Quieres salir?").strip().lower()
    while salida not in ("si", "no"):
        salida = input("Respuesta invalida, por favor escribe \"si\" o \"no\" \n")
    salir = salida == "si"
    

 