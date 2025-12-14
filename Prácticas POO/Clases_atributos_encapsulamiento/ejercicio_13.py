#Crear las clases con atributos encapsulados y sus métodos, según el siguiente escenario: 
# Se tienen clientes de los que se guarda un número de cliente, nombre, apellido, teléfono y correo electrónico.
#Los clientes realizan pedidos. Cada pedido tiene un número de pedido, una fecha asociada, un estado (sin confirmar o confirmado) y el cliente que realizó el pedido. Cada pedido tiene varias líneas de detalle, cada una con una cantidad y un artículo. Los artículos tienen un código, un nombre, una categoría y un precio.
#Para probar lo desarrollado se deben crear instancias de cada una de las clases y simular pedidos.

class Cliente:
    def __init__(self, nro_cliente, nombre, apellido, telefono, correo_electronico) :
        self.__nro_cliente = nro_cliente
        self.__nombre = nombre
        self.__apellido = apellido
        self.__telefono = telefono
        self.__correo_electonico = correo_electronico

class Articulo:
    def __init__(self, codigo, nombre, categoria, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.__categoria = categoria
        self.__precio = precio

class Pedido_Detalle:
    def __init__(self, cantidad, articulo):
        self.cantidad = cantidad
        self.articulo = articulo
        
class Pedido:
    def __init__(self, nro_pedido, fecha_asoc, estado, cliente: Cliente):
        self.nro_pedido = nro_pedido
        self.fecha_asoc = fecha_asoc
        self.estado= estado
        self.cliente = cliente
        self.__detalle_pedido = []

    def afregarArticulo(self, art: Articulo, cantidad):
        self.__detalle_pedido.append(Pedido_Detalle(cantidad, art))

    def mostrarDetalle(self):
        return self.__detalle_pedido


articulo1 = Articulo("1", "Heladera","Electro", 1000)
cliente1= Cliente("1", "Carlos", "Gonzalez", "11223344", "carlos@gmail.com")
pedido1 = Pedido("1","03/10/2025", "confirmado", cliente1)
pedido1.afregarArticulo(articulo1, 5)       
for articulo in pedido1.mostrarDetalle():
    print(articulo)