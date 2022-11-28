import psycopg2

# Conectamos a la base de datos POSTGRESQL
conn = psycopg2.connect(database = 'actividad_', user = 'postgres', password = 'example',
                        host = 'localhost', port = 5432)
# Abrimos un cursor para operar sobre la base de datos
cur = conn.cursor()

# En nuestro caso ya tenemos tanto la base de datos como las diferentes
# tablas creadas, vamos a proceder con los diferentes ejercicios.

# EJERCICIO 1.- Poblar las bases de datos
# Como la tabla notas tiene una clave foránea con la tabla edición,
# comenzamos poblando la tabla edición.
to_insert_ed = ['Uno', 'Dos', 'Tres']
try:
    for elem in to_insert_ed:
        cur.execute("INSERT INTO edicion (numero) VALUES (%s)", (elem, ))
except psycopg2.Error as e:
    print("Error al insertar dato: %s", str(e))
conn.commit()

# Proseguimos insertando los datos en la tabla notas
to_insert_grades = [('Isabel Maniega', 30, 5.6, 1),
                    ('José Manuel Peña', 30, 7.8, 1),
                    ('Pedro López', 30, 5.2, 2),
                    ('Julia García', 22, 7.3, 1),
                    ('Amparo Mayora', 28, 8.4, 3),
                    ('Juan Martínez', 30, 6.8, 3),
                    ('Fernando López', 35, 6.1, 2),
                    ('María Castro', 41, 5.9, 3)]
try:
    for tup in to_insert_grades:
        cur.execute("INSERT INTO notas (name, edad, notas, id_edic) VALUES (%s, %s, %s, %s)", (tup[0], tup[1], tup[2], tup[3]))
except psycopg2.Error as e:
    print("Error al insertar dato %s", str(e))
conn.commit()

# EJERCICIO 2.- Actualización de datos en la tabla notas
grades_to_update = [('Pedro López', 6.4), ('María Castro', 5.2)]
try:
    for tup in grades_to_update:
        cur.execute("UPDATE notas SET notas = (%s) WHERE name = %s", (tup[1], tup[0]))
except psycopg2.Error as e:
    print("Error al actualizar el dato: %s", str(e))
conn.commit()

# # EJERCICIO 3.- Lectura de los datos en la tabla notas
try:
    cur.execute("SELECT * FROM NOTAS;")
    rows = cur.fetchall()
    for row in rows:
        print(row)
except psycopg2.Error as e:
    print("Error leyendo datos: %s", str(e))

# # EJERCICIO 4.- Leer notas entre 5 y 6.5
try:
    cur.execute("SELECT * FROM notas WHERE notas BETWEEN 5.0 AND 6.5")
    rows = cur.fetchall()
    for row in rows:
        print(row)
except psycopg2.Error as e:
    print("Error leyendo datos: %s", str(e))

# EJERCICIO 5.- Buscar alumnos pertenecientes a la edición Dos
try:
    cur.execute("SELECT * FROM notas WHERE id_edic IN (SELECT id_edic FROM edicion WHERE numero = 'Dos')")
    rows = cur.fetchall()
    for row in rows:
        print(row)
except psycopg2.Error as e:
    print("Error leyendo los datos: %s", str(e))


# # EJERCICIO 6.- Eliminar los datos del alumno Pedro López
try:
    cur.execute("DELETE FROM notas WHERE name = 'Pedro López'")
except psycopg2.Error as e:
    print("Error al eliminar el dato: %s", str(e))
conn.commit()

# Cerramos el cursor y la conexión
cur.close()
conn.close()