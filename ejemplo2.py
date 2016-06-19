#!/usr/python
# -*- coding: utf-8 -*-

import MySQLdb

# Establecemos la conexión
Conexion = MySQLdb.connect(host='localhost', user='oso',passwd='panda', db='Tienda')

# Creamos el cursor
micursor = Conexion.cursor()

# Insertamos algunos registros (de forma cutre e ineficiente) para tener con qué trabajar
query= "INSERT INTO articulos (articulo,descripcion,precio,stock) VALUES (\"olla\",\"olla para cocinar cosas\", 21, True);"

micursor.execute(query)

query= "INSERT INTO articulos (articulo,descripcion,precio,stock) VALUES (\"sarten\",\"sarten para cocinar cosas\", 31, True);"

micursor.execute(query)

query= "INSERT INTO articulos (articulo,descripcion,precio,stock) VALUES (\"cacerola\",\"cacerola para cocer cosas\", 21.00, True);"

micursor.execute(query)

query= "INSERT INTO articulos (articulo,descripcion,precio,stock) VALUES (\"cuchillo\",\"cuchillo para acuchillar cosas\", 1.00, True);"

micursor.execute(query)

query= "INSERT INTO articulos (articulo,descripcion,precio,stock) VALUES (\"tenedor\",\"tenedor para pinchar cosas\", 9.00, True);"

micursor.execute(query)

# Hacemos un commit, por si las moscas
Conexion.commit()

# Ahora vamos a hacer un SELECT
query= "SELECT * FROM articulos;"

micursor.execute(query)

# Obtenemos el resultado con fetchmany
registros= micursor.fetchmany(2)

# para cada lista retornada (de 2 registros)...
while (registros):

    # ...recorremos la lista...

    for registro in registros:

       # ... mprimimos el registro...

       print registro

       # ...y recargamos los registros dentro del bucle, si quedan

    registros= micursor.fetchmany(2)

# Esto que sigue es para borrar el contenido de la base de datos,
# y que no se nos acumule al ir haciendo pruebas
#query= "DELETE FROM Victimas WHERE 1;"
#micursor.execute(query)

