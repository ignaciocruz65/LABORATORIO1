import sqlite3
def crear_tabla_si_no_existe():
    with sqlite3.connect('PROGRAMACION 1/JuegoPy/jugadores.db') as conexion:
        try:
            cursor = conexion.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Jugadores2';")
            tabla_existe = cursor.fetchone() is not None

            # Crear la tabla solo si no existe
            if not tabla_existe:
                sentencia_creacion = '''
                    CREATE TABLE Jugadores2
                    (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nombre TEXT,
                        score INTEGER
                    )
                '''
                conexion.execute(sentencia_creacion)
                print('Tabla creada con éxito!')

        except Exception as e:
            print('Ha ocurrido un error al crear la tabla:', e)

def insertar_datos(nombre, score):
    with sqlite3.connect('PROGRAMACION 1/JuegoPy/jugadores.db') as conexion:# Establecer conexión a la base de datos
        try:
            sentencia_insercion = '''
                INSERT INTO Jugadores2
                (
                    nombre, score
                ) VALUES (?,?)
            '''

            conexion.execute(sentencia_insercion, (nombre, score))
            print('Datos insertados con éxito')
            
            # Obtener los mejores 5 puntajes
            consulta_top5 = '''
                SELECT nombre, score FROM Jugadores2 ORDER BY score DESC LIMIT 5
            '''
            cursor = conexion.execute(consulta_top5) # Ejecutar una consulta
            mejores_puntuaciones = cursor.fetchall()# Obtener todos los resultados de la consulta
            # print('Top 5 mejores puntuaciones:', mejores_puntuaciones)

        except Exception as e:
            print('Ha ocurrido un error al insertar datos:', e)

def consultar_datos() -> list:

    lista_datos = []

    # Conectar a la base de datos
    with sqlite3.connect('PROGRAMACION 1/JuegoPy//base_datos.db') as conexion:
        # Crear un cursor
        cursor = conexion.cursor()

        # Ejecutar una consulta SELECT para obtener solo nombre y score
        cursor.execute("SELECT nombre, score FROM Jugadores ORDER BY score DESC LIMIT 5;")

        # Obtener todos los resultados
        filas = cursor.fetchall()

        # Procesar los resultados
        for fila in filas:
            # Acceder a los valores de cada columna
            nombre, score = fila
            diccionario_jugador = {'nombre': nombre, 'puntuacion': score}
            lista_datos.append(diccionario_jugador)

    return lista_datos

# def crear_y_cargar_datos(nombre, score):
#     with sqlite3.connect('PROGRAMACION 1/JuegoPy/jugadores.db') as conexion:
#         try:
#             cursor = conexion.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Jugadores';")
#             tabla_existe = cursor.fetchone() is not None

#             # Crear la tabla solo si no existe
#             if not tabla_existe:
#                 sentencia_creacion = '''
#                     CREATE TABLE Jugadores
#                     (
#                         id INTEGER PRIMARY KEY AUTOINCREMENT,
#                         nombre TEXT,
#                         score INTEGER
#                     )
#                 '''
#                 conexion.execute(sentencia_creacion)
#                 print('Tablar creada con Exito!')
        
#             sentencia_insercion = '''
#                 INSERT INTO Jugadores
#                 (
#                     nombre, score
#                 ) VALUES (?,?)
#             '''

#             conexion.execute(sentencia_insercion, (nombre, score))
#             print('created')

#         except Exception as e:
#             print('ha ocurrido un error', e)




