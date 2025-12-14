import sqlite3

bd = sqlite3.connect("example.db")
print("Base de datos abierta")

cur = bd.cursor()

#Crear una tabla
#cur.execute('''CREATE TABLE stocks
 #               (date text, trans text, symbol text, qty real, price real)''')

#Insertar un registro.
#cur.execute("INSERT INTO stocks VALUES ('2020-01-05','BUY','RHAT',100,35.14)")

#Guardar cambios.
#bd.commit()

#Se recomienda cerrar la conexión a la BD si hemos terminado.
#Solo debemos asegurarnos de que se hayan guardado los cambios o se perderan.
#bd.close()

#Seleccionar registros de una tabla.
t = ('RHAT',)
cur.execute('SELECT * FROM stocks WHERE symbol=?', t)
print(cur.fetchone())

#Seleccionar registros de una tabla con un iterador
for row in cur.execute('SELECT * FROM stocks ORDER BY price'):
    print(row)

#Sentencia para eliminar.
symbol = 'SONY'
sentencia = "DELETE FROM stocks WHERE symbol=?;"

#Eliminar el registro
cur.execute(sentencia, [symbol])
bd.commit()
print("Eliminado con éxito.")

#Sentencia para actuzalizar.
qty = 1500
price = 85.00
symbol = 'MSFT'
sentencia = "UPDATE stocks SET qty = ?, price = ? WHERE symbol = ?;"

#Actualizar datos
cur.execute(sentencia, [qty, price, symbol])
bd.commit()
print("Datos guardados.")