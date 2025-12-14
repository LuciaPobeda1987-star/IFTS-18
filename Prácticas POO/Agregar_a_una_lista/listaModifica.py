#Hacer un programa que me permita agregar datos a una lista.

lista_frutas = []
while True:
    fruit = input("Ingresar una fruta a la lista (q para salir): ")
    if fruit == "q":
        break
    lista_frutas.append(fruit)
 
print("La lista de frutas es la siguiente: ", lista_frutas)

