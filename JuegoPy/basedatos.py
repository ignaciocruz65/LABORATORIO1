import sqlite3


def crear_y_cargar_datos(nombre, score):
    with sqlite3.connect('PROGRAMACION 1/JuegoPy/jugadores.db') as conexion:
        try:
            cursor = conexion.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Jugadores';")
            tabla_existe = cursor.fetchone() is not None

            # Crear la tabla solo si no existe
            if not tabla_existe:
                sentencia_creacion = '''
                    CREATE TABLE Jugadores
                    (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nombre TEXT,
                        score INTEGER
                    )
                '''
                conexion.execute(sentencia_creacion)
                print('Tablar creada con Exito!')
        
            sentencia_insercion = '''
                INSERT INTO Jugadores
                (
                    nombre, score
                ) VALUES (?,?)
            '''

            conexion.execute(sentencia_insercion, (nombre, score))
            print('created')

        except Exception as e:
            print('ha ocurrido un error', e)


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