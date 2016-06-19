#!/usr/python
# -*- coding: utf-8 -*-

import MySQLdb

# Establecemos la conexión
Conexion = MySQLdb.connect(host='localhost', user='oso',passwd='panda', db='Tienda')

# Creamos el cursor, pero especificando que sea de la subclase DictCursor
micursor = Conexion.cursor(MySQLdb.cursors.DictCursor)

# Insertamos un par de registros
query= "INSERT INTO articulos (articulo,descripcion,precio,stock) VALUES (\"lapiz\",\"lapiz para pintar cosas\", 21, True);"

micursor.execute(query)

query= "INSERT INTO articulos (articulo,descripcion,precio,stock) VALUES (\"goma\",\"goma para borrar cosas\", 44, True);"

micursor.execute(query)

# Ahora vamos a hacer un SELECT
query= "SELECT * FROM articulos;"

micursor.execute(query)

# Obtenemos el resultado con fetchall
registros= micursor.fetchall()

for registro in registros:

# ... imprimimos el registro...
 print registro["precio"] + " sirve para " + registro["articulo"]

# Esto que sigue es para borrar el contenido de la base de datos,
# y que no se nos acumule al ir haciendo pruebas
#query= "DELETE FROM Victimas WHERE 1;"

micursor.execute(query)
