import sqlite3

def conectarBD():
    bd = sqlite3.connect("Empleados.db")
    print("Base de datos abierta")

def desconectarBD():
    bd = sqlite3.connect("Empleados.db")
    bd.close()
    print("Se ha cerrado la Base de Datos.")
      
def crearTabla():
    bd = sqlite3.connect("Empleados.db")
    cur = bd.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS empleados
                  ("nro_legajo" INTEGER NOT NULL UNIQUE,
                  "dni" INTEGER NOT NULL UNIQUE,
                  "nombre" text NOT NULL,
                  "apellido" text NOT NULL,
                  "area" text NOT NULL,
                  PRIMARY KEY("id" AUTOINCREMENT)
                  );''')
    print("La tabla se ha creado correctamente")
 
def insertarRegistro():
    bd = sqlite3.connect("Empleados.db")
    cur = bd.cursor()
    nro_legajo = int(input("Ingresa el número de legajo: "))
    dni = int(input("Ingresa el número de dni: "))
    nombre = input("Ingresa el nombre del empleado: ")
    apellido = input("Ingresa el apellido del empleado: ")
    area = input("Ingresa el área del empleado: ")
    cur.execute("INSERT INTO empleados('nro_legajo', 'dni', 'nombre', 'apellido', 'area') VALUES (?,?,?,?,?)", (nro_legajo, dni, nombre, apellido, area))
    bd.commit()
    print("Se ha insertado el registro con éxito.")
    
def seleccionarPorDni():
    bd = sqlite3.connect("Empleados.db")
    cur = bd.cursor()
    dni=int(input("Ingrese el número de dni que desea buscar"))
    cur.execute("SELECT * FROM empledos WHERE dni =?", dni)
    

def todosLosRegistros():
    bd = sqlite3.connect("Empleados.db")
    cur = bd.cursor()
    cur.execute("SELECT * FROM empleados")
    print(cur.fetchall())
    print("Se han mostrado todos los registros de la tabla Empleados.")

def modificarArea():
    bd = sqlite3.connect("Empleados.db")
    cur = bd.cursor()
    area_modificada=input("A que área desea modificar este legajo? ")
    nro_legajo= int(input("Ingrese el número de lejajo al que desea modificar el área: "))
    modificacion= cur.execute("UPDATE empleados SET area = ?, WHERE nro_legajo=?")
    cur.execute(modificacion, [area_modificada, nro_legajo])
    bd.commit()
    print("Datos guardados.")


def eliminarEmpleado():
    bd = sqlite3.connect("Empleados.db")
    cur = bd.cursor()
    nro_legajo_a_eliminar = int(input("Ingrese el número de legajo que desea eliminar: "))
    sentencia = "DELETE FROM empleados WHERE symbol=?;"
    cur.execute(sentencia, [nro_legajo_a_eliminar])
    bd.commit()
    print("Eliminado con éxito.")



print("[1] Insertar un registro en la tabla.")
print("[2] Seleccionar registro por dni.")
print("[3] Seleccionar todos los resgistros.")
print("[4] Modificar el áreal de un empleado ingresando su número de legajo.")
print("[5] Eliminar un registro ingresando el número de lejajo.")
print("[6] Salir de la BBDD empleados.")
opcion= input("Elija su opción:")

match opcion:
    case "1":
        conectarBD()
        crearTabla()
        insertarRegistro()
    case "2":
        seleccionarPorDni()
    case "3":
        conectarBD()
        crearTabla()
        todosLosRegistros()
    case "4":
        modificarArea()
    case "5":
        eliminarEmpleado() 
    case "6":  # El guion bajo '_' actúa como el caso por defecto
        #desconectarBD()
        print("Has salido de la BBDD empleados.")