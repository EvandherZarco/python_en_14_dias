#Programa elaborado por: Zarco Hernandez Evandher Joel

#Este programa sugerirá una actividad en base al estado de animo del usuario 

energia = int(input("Del 1 al 10 ¿Cuánta energía tienes? "))

while not (1 <= energia <= 10):
    energia = int(input("Número invalido. Ingresa un número del 1 al 10, por favor unu \n"))

respuesta = input("¿Tienes tareas pendientes? (Si/No)").strip().lower()
respuesta = respuesta.replace("í" , "i")

while respuesta not in ("si" , "no"):
    respuesta = input("Por favor solo responde \"si\" o \"no\" unu \n").strip().lower()
    respuesta = respuesta.replace("í" , "i")

tarea = (respuesta == "si")

if(tarea):
    if(energia <= 3): 
        print("Haz una tarea mínima de 15 minutos y un descansa uwu")
    elif(4 <= energia < 7 ) :
        print("Haz una tarea que tarde de 20 a 45 minutos uwu") 
    else:
        print("Modo bestia: Tarea que dura 60 minutos y algo extra uwu")

elif(not tarea):
    if(energia <= 3): 
         print("Haz ejercicio leve o practica tu instrumento por 20 minutos uwu")
    elif(4 <= energia < 7 ):
        print("Haz ejercicio medio y practica tu instrumento")
    else:
        print("Haz ejercicio intenso, descansa y después practica tu instrumento uwu")

