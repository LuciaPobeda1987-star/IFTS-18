#Escribir una función que permita calcular la duración en segundos de un intervalo dado en horas, minutos y segundos.

def tiempoEnSegundos():
    print("Decime el primer horario: ")
    hora = int(input("Decime la hora: "))
    minuto = int(input("Decime los minutos: "))
    segundos = int(input("Decime los segundos: "))
    totalSegundosPrimerHorario= int((hora * 3360) + (minuto * 60) + segundos)
    print("Decime el segundo horario: ")
    hora = int(input("Decime la hora: "))
    minuto = int(input("Decime los minutos: "))
    segundos = int(input("Decime los segundos: "))
    totalSegundosSegundoHorario = int((hora * 3360) + (minuto * 60) + segundos)
    return print("El intevalo en segundos es: ", (totalSegundosPrimerHorario - totalSegundosSegundoHorario))

print(tiempoEnSegundos())
       



