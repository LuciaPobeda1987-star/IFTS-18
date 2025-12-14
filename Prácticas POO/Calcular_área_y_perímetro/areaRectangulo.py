#Ejercicio 1). Escribir un programa que calcule perímetro y área de un rectángulo según los datos que me de el usuario.

altura_rectangulo = float(input("Ingrese la altura del rectángulo: "))
base_rectangulo = float(input("Ingrese la base del rectángulo: "))

#Cáculo perímetro:
perimetro_rectangulo = 2*(altura_rectangulo+base_rectangulo)
print("El perímetro es: ", perimetro_rectangulo)

#Calculo área:
area_rectangulo= altura_rectangulo*base_rectangulo
print("El área es: ", area_rectangulo)
