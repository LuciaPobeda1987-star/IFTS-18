#Escribir una función que reciba una muestra de números en una lista y retorne los cuadrados de los valores de esa lista.

def cuadrados_lista (lista):
    nueva_lista = []
    for valor in lista:
        nueva_lista.append(valor **2)
    return nueva_lista

print(cuadrados_lista([2, 3, 5]))