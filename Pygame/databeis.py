import sqlite3

class Consultas:

    def __init__(self):
        self.path = "Clase_18/bd_test2.db"
    
    def agregar_dato(self, nombre, apellido, anio):
        with sqlite3.connect(self.path) as conexion:
            try:
                    conexion.execute("insert into personas(nombre,apellido,anio) values (?,?,?)", (nombre, apellido, anio))                                 
                    conexion.commit()# Actualiza los datos realmente en la tabla
                    print("Dato agregado correctamente")
            except:
                    print("Error")
    

consulta_mysql = Consultas()
consulta_mysql.agregar_dato("Yanina","Bonelli","1992")


#CREAR TABLA
# with sqlite3.connect("Clase_18/bd_test2.db") as conexion:
#     try:
#         sentencia = ''' create table personas
#                         (
#                                 id integer primary key autoincrement,
#                                 nombre text,
#                                 apellido text, 
#                                 anio real
#                         )
#                     '''
#         conexion.execute(sentencia)
#         print("Se creo la tabla personajes")                       
#     except sqlite3.OperationalError:
#         print("La tabla personajes ya existe")    



# #AGREGAR
# with sqlite3.connect("Clase_18/bd_test2.db") as conexion:
#     try:
#             conexion.execute("insert into personas(nombre,apellido,anio) values (?,?,?)", ("Lucas", "Nani","1968"))
#             conexion.execute("insert into personas(nombre,apellido,anio) values (?,?,?)", ("Gabriel", "Fernandez","1994"))             
#             conexion.commit()# Actualiza los datos realmente en la tabla
#     except:
#             print("Error")


# #TRAER TODOS LOS DATOS
# with sqlite3.connect("Clase_18/bd_test2.db") as conexion:
#     cursor = conexion.execute("SELECT * FROM personas")
#     for fila in cursor:
#         print(fila)        



#TRAER DATO ESPECIFICO
# id = 0
# with sqlite3.connect("Clase_18/bd_test2.db") as conexion:
#     sentencia = "SELECT * FROM personas WHERE nombre = 'David'"
#     cursor=conexion.execute(sentencia)
#     for fila in cursor:
#         print(fila)



#MODIFICAR
# id = "1"
# with sqlite3.connect("Clase_18/bd_test2.db") as conexion:
#     sentencia = "UPDATE personas SET apellido = 'Suarez' WHERE id=?"
#     cursor=conexion.execute(sentencia,(id,))
#     filas=cursor.fetchall()
#     for fila in filas:
#         print(fila)
#     conexion.commit()



#ELIMINAR
# id = "1"
# with sqlite3.connect("Clase_18/bd_test2.db") as conexion:
#   sentencia = "DELETE FROM personas WHERE id=?"
#   cursor=conexion.execute(sentencia,(id,))



