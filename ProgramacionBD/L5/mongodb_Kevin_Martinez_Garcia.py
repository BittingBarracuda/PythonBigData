import pymongo
from datetime import datetime

# Creamos el cliente para conectarnos a la base de datos
# añadimos el IP y el host
client = pymongo.MongoClient("localhost", 27017)
# Creamos la conexión a la base de datos actividad
db = client.actividad

# Actividad 1.- Insertar una colección de datos
# to_insert = [{"nombre":"Pedro López", "edad":25, "email":"pedro@eip.com",
#               "nota":5.2, "fecha":datetime.now().strftime("%d/%m/%Y %H:%M:%S")}, 
#               {"nombre":"Julia García", "edad":22, "email":"julia@eip.com",
#               "nota":7.3, "fecha":datetime.now().strftime("%d/%m/%Y %H:%M:%S")},
#               {"nombre":"Amparo Mayoral", "edad":28, "email":"amparo@eip.com",
#               "nota":8.4, "fecha":datetime.now().strftime("%d/%m/%Y %H:%M:%S")},
#               {"nombre":"Juan Martínez", "edad":30, "email":"juan@eip.com",
#               "nota":6.8, "fecha":datetime.now().strftime("%d/%m/%Y %H:%M:%S")}]


# db.notas.insert_many(to_insert)

# Actividad 2.- Actualizar los datos
# to_update = [("Amparo Mayoral", 9.3), ("Juan Martínez", 7.2)]
# # Buscamos todas las entradas de la colección
# datos = db.notas.find({})
# # Buscamos los datos que necesitamos
# for dato in datos:
#     if dato["nombre"] == to_update[0][0]:
#         id_mongo = dato["_id"]
#         upd = dato.copy()
#         upd["nombre"] = to_update[0][0]
#         upd["nota"] = to_update[0][1]
#         to_update.pop(0)
#         db.notas.update_one({"_id":id_mongo},
#                             {"$set":upd})

# Actividad 3.- Lectura de la colección de datos
# datos = db.notas.find({})
# for dato in datos:
#     print(dato)

# Actividad 4 .- Notas en un intervalo [7, 7.5]
# datos = db.notas.find({"nota": {"$gte": 7, "$lte": 7.5}})
# for dato in datos:
#     print(dato)

# # Actividad 5.- Eliminar los datos de Pedro López
to_delete = db.notas.find({"nombre":"Pedro López"})
try:
    alu = to_delete.next()
    db.notas.delete_one({"_id":alu["_id"]})
except StopIteration:
    print("El alumno no existe!")