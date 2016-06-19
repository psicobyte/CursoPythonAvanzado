#!/usr/python
# -*- coding: utf-8 -*-

import MySQLdb

# Establecemos la conexión
Conexion = MySQLdb.connect(host='localhost', user='oso',passwd='panda', db='Tienda')

# Creamos el cursor
micursor = Conexion.cursor()

# Ejecutamos un insert directamente
micursor.execute("INSERT INTO articulos (articulo,descripcion,precio,stock) VALUES (\"raqueta\", \"de padel\", 10.00, TRUE);")

# Lo mismo, pero por medio de una variable
query= "INSERT INTO articulos (articulo, descripcion, precio, stock) VALUES (\"pala\", \"tenis\", 20.00, TRUE);"

micursor.execute(query)

# Hacemos un commit, por si las moscas
Conexion.commit()

# Ahora vamos a hacer un SELECT
query= "SELECT * FROM articulos WHERE precio=10;"

micursor.execute(query)

# Obtenemos el resultado con fetchone
registro= micursor.fetchone()

# Imprimimos el registro resultante
print registro

#Vemos el numero de registros con la propiedad rowcount de la clase cursor, de este modo:

numero_de_registros= micursor.rowcount 

print "Se ha ingresado " + str(numero_de_registros) + " registros" 


