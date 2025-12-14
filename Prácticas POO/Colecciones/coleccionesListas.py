#Elementos ordenados por indice correlativo(comenzando en 0)
#Los elementos pueden ser de direfente tipo de datos (incluso otra lista)
#Los elementos pueden estar repetidos
#Se pueden realizar rebanadas(como las vistas en String)
#Son mutables(se pueden cambiar los calores de los elementos)

#CREAMOS UNA LISTA
""" 
lista = []
lista = list()

lista = ["Hola", 1.4,78,[10,20,30], False, 78]

print(lista[3])

lista2 = list(range(5)) #nos da un rango del 0 al 4

print(lista2)
"""

#Append(elemento) agrega un elemento al final de la lista

# lista = [1,2,3]
# lista.append(5) salida [1,2,3,5]

#Extend (lista) agrega una lista a otra

# lista = [1,2,3]
#lista.extend([4,5,6]) salida [1,2,3,4,5,6]

#Insert (posición, elemento) agrega un elemento a una posición específica y desplaza el resto de la lista (si colocamos una posición inexistente agrega el elemento al final)

# lista = [1,2,3]
#lista.insert(1,5) salida [1,5,2,3]

#ELIMINAR ELEMENTOS DE UNA LISTA

#pop() elimina el ultimo elemento de la lista o el elemento cuyo índice se le pasa como parámetro

#remove(elemento) elimina el elemento que se le pasa como parámetro (el elemento debe existir en la lista)

#del lista[posición] elimina el elemento de la posición indicada

#clear() elimina todos los elementos de la lista

#MODIFICAR Y VER ELEMENTOS DE UNA LISTA

#lista[posicion] = valor // modificamos el elemento en esa posición o índice, ejemplo: lista[4] = "Hola"

# index(elemento) obtenemos el índice del elemento pasado como parámetro

# lista[posicion] accedemos al elemento en dicha posicion indicada

# lista[2:5] obtenemos una rebanada de la lista, siempre devuelve otra lista.

#OTRAS OPERACIONES UTILES

# len(lista) para obtener la longitud
#Pertenencia elemento in lista (retornará True si el elemento está en la lista)
# Concatenación lista+otra_lista (similar al lista.extend)
# count(elemento) cuenta cuantas veces está el elemento pasado como un parámetro.



cualquier_cosa = ["Hola",78,98,True]
#Agregar un elemento al final
cualquier_cosa.append(5)

print(cualquier_cosa)

#Agregar el 7 despues del 6
cualquier_cosa.insert(1,7)

print(cualquier_cosa)

cualquier_cosa.append("Hola")

print(cualquier_cosa)

print("Eliminando......")

#Eliminar conociendo el dato o el elemento

cualquier_cosa.remove(78)

print(cualquier_cosa)









