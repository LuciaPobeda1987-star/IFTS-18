#Ejercicio 2). Escribir un programa que pida 2 números por consola y realice las operaciones de suma, resta multiplicación y división entre ellos.

#Función suma
def suma (num_1, num_2):
        return (num_1 + num_2)
         
#Función resta
def resta (num_1, num_2):
        return (num_1 - num_2)
    
#Función multiplicación
def multiplicacion (num_1, num_2):
        return (num_1 * num_2)
#Función división
def division (num_1, num_2):
        return (num_1 / num_2)
    
num_1 = int(input("Ingrese el primer valor: "))
num_2 = int(input("Ingrese el segundo valor: "))

flag = True
while flag:
    respuesta_usuario = input("Ingrese el nombre de la operación que desea realizar entre suma (1), resta (2), multiplicacion (3) y division (4) o 'Fin' para finalizar: ")
    
    #match es como el switch de Java.
    match respuesta_usuario:
        case "1":
            print(f"El resultado de la suma es {suma(num_1, num_2)}")
        case "2":
            print(f"El resultado de la resta es {resta(num_1, num_2)}")
        case "3":
            print(f"El resultado de la multiplicación es {multiplicacion(num_1, num_2)}")
        case "4":
            print(f"El resultado de la división es {division(num_1, num_2)}")
        case "Fin":
            print("Has finalizado.")
            flag = False # sino, sin bandera y con break se sale finaliza el bucle
        case _:
            print("La opción ingresada no es correcta")

    
