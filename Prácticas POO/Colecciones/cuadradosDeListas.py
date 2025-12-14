#Escribir una función que reciba una muestra de números en una lista y devuelva otra lista con sus cuadrados.

def cuadrados_lista(numeros):
    numeros = [1, 2, 3, 4, 5]
    cuadrados = [x**2 for x in numeros]
    return cuadrados

lista1 = []
cuadrado = (cuadrados_lista(lista1))
print("Los cuadrados de los valores de la lista es ", cuadrado)


