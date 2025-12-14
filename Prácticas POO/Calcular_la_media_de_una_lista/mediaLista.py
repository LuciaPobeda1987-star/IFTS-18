#Escribir una función que reciba una muestra de números en una lista y retorne su media.

def media_lista():
    lista=[]
    while True:
        valor = int(input("Ingresar un valor (0 para salir): "))
        if valor == 0:
            break
        lista.append(valor)
    suma_lista= sum(lista)
    longitud = len(lista)
    return print("La media de los valores de la lista es: ", suma_lista / longitud)
  
media_lista()        