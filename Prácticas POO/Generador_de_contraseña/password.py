import random

class Password:
    #Dos atributos de clase privados:
    __LONGITUD = 8
    __CARACTERES_VALIDOS ="0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ<=> @#%&+"
    
    def __init__(self, longitud):
        #Dos atributos de instancia privados:
        self.set_longitud(longitud)
        self.set_password()

    # Método para verificar si la contraseña es fuerte
    def esFuerte(self) -> bool:
        condicion_mas_de_una_mayuscula = 0
        condicion_mas_de_un_caracter_esp = 0
        condicion_mas_de_una_minuscula = 0
        condicion_mas_de_un_numero = 0
        passw = Password.__CARACTERES_VALIDOS
        for letra in Password.__CARACTERES_VALIDOS:
            for letraPass in passw:
                if(letraPass == letra):
                    if(letraPass.isupper()):
                        condicion_mas_de_una_mayuscula += 1
                        print("condicion_mas_de_una_mayuscula", letraPass)
                    if (letraPass.islower()):
                        condicion_mas_de_una_minuscula += 1
                        print("condicion_mas_de_una_minuscula", letraPass)
                    if (letraPass.isdigit()):
                        condicion_mas_de_un_numero +=1
                        print("condicion_mas_de_un_numero", letraPass)
                    if(not(letraPass.isupper())and (not(letraPass.islower()))and (not(letraPass.isdigit()))):
                        print("***", letraPass)   
                        condicion_mas_de_un_caracter_esp += 1
                        print("Caracter especial:", letraPass)
                        print("condicion_mas_de_1_mayuscula", condicion_mas_de_una_mayuscula)                     
                        print("condicion_mas_de_1_minuscula", condicion_mas_de_una_minuscula)                     
                        print("condicion_mas_de_1_numero", condicion_mas_de_un_numero)                     
                        print("condicion_1_caracter_especial", condicion_mas_de_un_caracter_esp)               

            if((condicion_mas_de_una_mayuscula > 1) and (condicion_mas_de_una_minuscula > 1) and (condicion_mas_de_un_numero > 1) and (condicion_mas_de_un_caracter_esp >= 1)):
                return True
            else: 
                return False
            
    #Generar password.     
    def generarPassword(self):
        return ''.join(random.choices(Password.__CARACTERES_VALIDOS, k=self.__longitud))
    
    #Obtener longitud.   
    def get_longitud(self):
        return self.__longitud
    
    #Settear longitud.
    def set_longitud(self, longitud):
         if longitud < 6 or longitud > 15:
            print("Password inválido: su longitud es menor a 6 o mayor a 15 caracteres; >>> SE ASIGNA VALOR POR DEFECTO.")
            self.__longitud = Password.__LONGITUD
         else: 
            self.__longitud = longitud

    #Obtener la password.           
    def get_password(self):
        return self.__password
    #Settear la password.
    def set_password(self):
        self.__password = self.generarPassword()

    # Sobreescribir __str__() para mostrar la contraseña y si es fuerte
    def __str__(self):
        return f"{self.__password} - {self.esFuerte()}"

# Crear una lista de objetos de tipo Password
def crear_contraseñas():
    lista_passwords = [Password(random.randint(6, 15)) for _ in range(10)]
    for password in lista_passwords:
        if password.esFuerte():
            print("Password es segura")
        else:
            password.set_password
        


var= Password(7)
print(var.get_longitud())
print(var.generarPassword())
print(var.get_password)
var.esFuerte()
#crear_contraseñas()







        
                

        
        