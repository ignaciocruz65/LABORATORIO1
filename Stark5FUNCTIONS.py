import json
import re

heroe = {}


def imprimir_dato(dato):
    print(dato)

def imprimir_heroe(dato: dict, datodos: str):
    '''
    La función  `imprimir_heroe`  se encarga de imprimir el nombre y un dato específico de un héroe a partir de un diccionario dado.
    '''
    if 'nombre' in dato and datodos in dato:
        print('nombre:', dato['nombre'])
        print(datodos + ':', dato[datodos])
    else:
        print('No se encontró el nombre o el dato ingresado en el diccionario.')

def imprimir_menu_desafio_5():
    imprimir_dato("A-Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M")
    imprimir_dato("B-Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F")
    imprimir_dato("C-Recorrer la lista y determinar cuál es el superhéroe más alto de género M")
    imprimir_dato("D-Recorrer la lista y determinar cuál es el superhéroe más alto de género F")
    imprimir_dato("E-Recorrer la lista y determinar cuál es el superhéroe más bajo de género M")
    imprimir_dato("F-Recorrer la lista y determinar cuál es el superhéroe más bajo de género F")
    imprimir_dato("G-Recorrer la lista y determinar la altura promedio de los superhéroes de género M")
    imprimir_dato("H-Recorrer la lista y determinar la altura promedio de los superhéroes de género F")
    imprimir_dato("I-Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (ítems C a F)")
    imprimir_dato("J-Determinar cuántos superhéroes tienen cada tipo de color de ojos.")
    imprimir_dato("K-Determinar cuántos superhéroes tienen cada tipo de color de pelo.")
    imprimir_dato("L-Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de no tener, Inicializarlo con ‘No Tiene’).")
    imprimir_dato("M-Listar todos los superhéroes agrupados por color de ojos.")
    imprimir_dato("N-Listar todos los superhéroes agrupados por color de pelo.")
    imprimir_dato("O-Listar todos los superhéroes agrupados por tipo de inteligencia")
    imprimir_dato("Z-SALIR")

def stark_menu_principal_desafio_5():
    imprimir_menu_desafio_5()
    opcion = input("Opcion: ")
    str_txt = r'^[a-zA-Z\s]$'
    if re.match(str_txt, opcion):
        return opcion
    else:
        return -1

def leer_archivo(nombre_archivo: str) -> list:
    '''
    Este código define una función llamada  `leer_archivo`  que lee un archivo JSON y devuelve una lista de héroes.
    '''
    archivo = open(nombre_archivo, "r")
    diccionario = json.load(archivo)
    archivo.close()
    return diccionario["heroes"]

lista_personajes = leer_archivo("PROGRAMACION 1/stark.json")

def guardar_archivo(nombre_archivo, contenido):
    '''
    La función  `guardar_archivo`  se encarga de crear un archivo con el nombre y contenido proporcionados. Retorna True si el archivo se crea exitosamente, y False en caso contrario.
    '''
    try:
        archivo = open(nombre_archivo, "w+")
        archivo.write(contenido)
        archivo.close()
        print(f"Se creo el archivo: {nombre_archivo}")
        return True
    except:
        print(f"Error al crear el archivo: {nombre_archivo}")
        return False


def capitalizar_palabras(frase):
    '''
    La función  `capitalizar_palabras`  toma una cadena de texto como entrada y capitaliza la primera letra de cada palabra en la cadena.
    '''
    palabras = frase.split()
    palabras_capitalizadas = [palabra.capitalize() for palabra in palabras]
    return ' '.join(palabras_capitalizadas)

def obtener_nombre_capitalizado(heroe):
    '''
    La función  `obtener_nombre_capitalizado`  recibe como entrada un diccionario  `heroe`  y devuelve una cadena de texto formateada que incluye el nombre del héroe con la primera letra en mayúscula.
    '''
    nombre = heroe["nombre"]
    nombre_formateado = capitalizar_palabras(nombre)
    return f"Nombre: {nombre_formateado}"


def obtener_nombre_y_dato(heroe, clave):
    '''
    La función  `obtener_nombre_y_dato`  recibe como entrada un diccionario  `heroe`  y una cadena  `clave` . Devuelve una cadena de texto formateada que incluye el nombre del héroe con la primera letra en mayúscula, la clave en mayúscula y el valor correspondiente del diccionario del héroe. Si la clave no está presente en el diccionario del héroe, devuelve una cadena indicando que los datos no están disponibles.
    '''
    nombre_formateado = obtener_nombre_capitalizado(heroe)
    if clave in heroe:
        dato = heroe[clave]
        return f"{nombre_formateado} | {clave.capitalize()}: {dato}"
    else:
        return f"{nombre_formateado} | {clave.capitalize()}: No disponible"

def es_genero(heroe, genero):
    '''
    La función  `es_genero`  verifica si el género de un héroe dado coincide con un género especificado.
    '''
    if genero == heroe["genero"]:
        return True
    else:
        return False


def stark_guardar_heroe_genero(lista_heroes, genero):
    '''
    La función  `stark_guardar_heroe_genero`  recibe una lista de héroes y un género como entrada. Itera a través de la lista de héroes y verifica si cada héroe coincide con el género especificado. Si un héroe coincide con el género, su nombre se formatea y se agrega a una nueva lista llamada  `heroes_coincidentes` . Luego, la función crea un archivo con un nombre basado en el género y guarda los nombres de los héroes formateados como valores separados por comas en el archivo. La función devuelve True si el archivo se guarda correctamente, y False en caso contrario.
    '''
    heroes_coincidentes = []
    for heroe in lista_heroes:
        if es_genero(heroe, genero):
            nombre_formateado = obtener_nombre_capitalizado(heroe)
            imprimir_dato(nombre_formateado)
            heroes_coincidentes.append(nombre_formateado)   
    nombre_archivo = f"heroes_{genero}.csv"
    contenido = ",".join(heroes_coincidentes)
    if guardar_archivo(nombre_archivo, contenido):
        return True
    else:
        return False

def calcular_min(lista_personajes, key):
    '''
    Esta función calcula el valor mínimo de una clave específica en una lista de diccionarios.
    '''
    min_value = float('inf')
    minimo_heroe = None
    for personaje in lista_personajes:
        if key in personaje:
            dato = float(personaje[key])
            if dato < min_value:
                min_value = dato
                minimo_heroe = personaje
    return minimo_heroe

def calcular_min_genero(lista_personajes, key, genero):
    '''
    Esta función calcula el valor mínimo de una clave específica para un género dado en una lista de personajes.
    '''
    min_value = float('inf')
    min_hero = None
    for personaje in lista_personajes:
        if personaje['genero'] == genero:
            if key in personaje:
                dato = float(personaje[key])
                if dato < min_value:
                    min_value = dato
                    min_hero = personaje
    if min_hero is not None:
        return min_hero
    else:
        return None


def calcular_max(lista_personajes, key):
    '''
    La función  `calcular_max`  calcula el valor máximo de una clave específica en una lista de diccionarios.
    '''
    max_value = float('-inf')
    maximo_heroe = None
    for personaje in lista_personajes:
        if key in personaje:
            dato = float(personaje[key])
            if dato > max_value:
                max_value = dato
                maximo_heroe = personaje
    return maximo_heroe

def calcular_max_genero(lista_personajes, key, genero):
    '''
    Esta función calcula el valor máximo de una clave específica para un género dado en una lista de personajes.
    '''
    max_value = float('-inf')
    max_hero = None
    for personaje in lista_personajes:
        if personaje['genero'] == genero:
            if key in personaje:
                dato = float(personaje[key])
                if dato > max_value:
                    max_value = dato
                    max_hero = personaje
    if max_hero is not None:
        return max_hero
    else:
        return None
    
def calcular_max_min_dato_genero(genero, max_o_min, key):
    '''
    Esta función calcula el valor máximo o mínimo de una clave dada para un género específico en una lista de personajes.
    '''
    if genero in ["M", "F", "NB"]:
        if max_o_min == "minimo":
            return calcular_min_genero(lista_personajes, key, genero)
        elif max_o_min == "maximo":
            return calcular_max_genero(lista_personajes, key, genero)
        else:
            return "Opción inválida: max_o_min debe ser 'minimo' o 'maximo'"
    else:
        return "Género inválido: debe ser 'M', 'F' o 'NB'"

def stark_calcular_imprimir_guardar_heroe_genero(lista_personajes, genero, max_o_min, key):
    '''
    Esta función calcula, imprime y guarda información sobre un héroe basándose en su género.
    '''
    heroe = calcular_max_min_dato_genero(genero, max_o_min, key)
    if heroe is not None:
        mensaje = obtener_nombre_y_dato(heroe, key)
        imprimir_dato(mensaje)
        nombre_archivo = f"heroes_{max_o_min}_{key}_{genero}.csv"
        contenido = mensaje
        guardar_archivo(nombre_archivo, contenido)
        return True
    else:
        return False


def sanitizar_entero(numero:str):
    '''
    La funcion recibira como parametro un numero en string, con el metodo strip se le suprimiran los espacios vacios, se verificara si el numero empieza con - es negativo y retornara -2, se utiliza una expresion regular para buscar un caracter que no sea digito en el numero y si lo encuentra retornara -1 y si ninguna de las condiciones anteriores se cumple retornara -3.
    '''
    numero = numero.strip()
    if numero.startswith('-'):
        return -2
    elif re.search(r'[^0-9]', numero):
        return -1
    elif re.match(r'^\d+$', numero):
        return int(numero)
    else:
        return -3    

def sanitizar_flotante(numero:str):
    '''
    La funcion recibira como parametro un numero float de tipo string, con el metodo strip suprimiremos los espacios en blanco, se verifica que el numero string empiece con - y si el numero es flotante, en caso de que lo sea retornara -2, si el numero es flotante positivo se parseara a float y retornara el numero parseado, si el string contiene algun caracter que no sea un digito, retornara -1, en caso de que ninguna de las condiciones se cumpla retornara -3.
    '''
    numero = numero.strip()
    flotante = r'^[-+]?[0-9]*\.?[0-9]+([-+]?[0-9]+)?$'
    if numero.startswith('-') and re.match(flotante,numero):
        return -2
    elif re.match(flotante,numero):
        numero = float(numero)
        return numero
    elif re.search(r'[^0-9]', numero):
        return -1
    else:
        return -3

def sanitizar_string(valorstr:str,valorpd:str):
    '''
    La funcion recibira como parametro dos strings, valorstr y valorpd, se verifica que el valorstr contenga solo caracteres alfabeticos y espacios, si lo son, se convertira en minusculas retornara el texto, si el valorstr contiene algun digito retornara N/A, y si es una cadena vacia retornara el valor por defecto.
    '''
    valorstr = valorstr.strip()
    valorpd = valorpd.strip()
    if re.match('[a-zA-Z\s]+',valorstr):
        valorstr.replace("/","\s")
        texto = valorstr.lower()
        return texto
    elif re.findall(r'\d+',valorstr):
        return "N/A"
    elif valorstr == "":
        return valorpd.lower()

def sanitizar_dato(heroe:dict,clave:str,tipo_dato:str):
    '''
    La funcion recibe como parametro un diccionario(heroe), una clave y un tipo de dato en string, se convierte el tipo de dato en minuscula, se verifica que el tipo de dato sea string,entero o flotante, si no lo es retorna false, se verifica que la clave existe en el diccionario, si no lo esta se imprime un mensaje de error y retornara false, luego se verifica que el tipo de dato es un string, se llama a la funcion sanitizar string y se sanitiza el valor del diccionario, en caso de que sea entero se usa la funcion sanitizar entero y el valor, lo mismo en el al ser un flotante, se usa la funcion sanitizar flotante y el valor, la funcion retornara true.
    '''
    tipo_dato = tipo_dato.lower()
    if tipo_dato not in ['string', 'entero', 'flotante']:
        print('Tipo de dato no reconocido')
        return False
    if clave not in heroe:
        print('La clave especificada no existe en el héroe')
        return False
    valor = heroe[clave]
    if tipo_dato == 'string':
        heroe[clave] = sanitizar_string(valor,"pordefecto")
    elif tipo_dato == 'entero':
        heroe[clave] = sanitizar_entero(valor)
    elif tipo_dato == 'flotante':
        heroe[clave] = sanitizar_flotante(valor)
    
    return True

def stark_normalizar_datos(lista:list):
    '''
    La funcion recibe como parametro una lista, se verifica que la lista no este vacia, si lo esta se retorna un mensaje de error, si no, se sanitizan los datos solicitados con la funcion sanitizar dato y retornara un mensaje exitoso.
    '''
    if not lista:
        return "Error lista de heroes"
    else:
        for item in lista:
            sanitizar_dato(item,'altura','flotante')
            sanitizar_dato(item,'peso','flotante')
            sanitizar_dato(item,'fuerza','entero')
            sanitizar_dato(item,'color_ojos','string')
            sanitizar_dato(item,'color_pelo','string')
            sanitizar_dato(item,'inteligencia','string')
        return True

def sumar_dato_heroe_genero(lista, clave, genero):
    '''
    Esta función calcula la suma de un atributo de datos específico para todos los héroes de un género dado en una lista de héroes.
    '''
    if not lista:
        print('La lista está vacía')
        return -1
    suma = 0
    for heroe in lista:
        if isinstance(heroe, dict) and heroe and heroe.get('genero') == genero:
            if clave in heroe:
                valor = heroe[clave]
                if isinstance(valor, int) or isinstance(valor, float):
                    suma += valor
                else:
                    print('El valor no es numérico')
    
    if suma > 0:
        return suma
    else:
        return -1

def cantidad_heroes_genero(lista_heroes, genero):
    '''
    Esta función calcula el número de héroes en una lista dada que tienen un género específico.
    '''
    count = 0
    for heroe in lista_heroes:
        if heroe['genero'] == genero:
            count += 1
    return count

def dividir(divisor,dividendo):
    '''La funcion recibe como parametro dos numeros, dividendo y divisor, se verifica que el diviso sea distinto a 0, si lo es retornara la funcion como false, en caso de que no, se realizara la division'''
    if(divisor != 0):
        div = divisor/dividendo
        return div
    else:
        return False

def calcular_promedio_genero(lista_heroes, key, genero):
    suma = sumar_dato_heroe_genero(lista_heroes, key, genero)
    cantidad = cantidad_heroes_genero(lista_heroes, genero)
    if suma != -1 and cantidad != 0:
        promedio = dividir(suma, cantidad)
        return promedio
    else:
        return -1

def stark_calcular_imprimir_guardar_promedio_altura_genero(lista_personajes, genero):
    '''
    Esta función calcula el valor promedio de un atributo específico (clave) para un género dado en una lista de héroes.
    '''
    if len(lista_personajes) > 0:
        promedio = calcular_promedio_genero(lista_personajes, 'altura', genero)
        if promedio != -1:
            mensaje = f"Altura promedio género {genero}: {promedio:.2f}"
            imprimir_dato(mensaje)
            nombre_archivo = f"heroes_promedio_altura_{genero}.csv"
            contenido = mensaje
            return guardar_archivo(nombre_archivo, contenido)
        else:
            imprimir_dato("Error: No se pudo calcular el promedio")
            return False
    else:
        imprimir_dato("Error: Lista de héroes vacía")
        return False

def calcular_cantidad_tipo(lista_heroes, tipo_dato):
    '''
    Esta función calcula la cantidad de un tipo de dato específico en una lista de héroes. Retorna un diccionario con los valores capitalizados del tipo de dato como claves y el conteo correspondiente como valores.
    '''
    if not lista_heroes:
        return {"Error": "La lista se encuentra vacía"}
    cantidad_tipo = {}
    for heroe in lista_heroes:
        if tipo_dato in heroe:
            valor = heroe[tipo_dato]
            valor_capitalizado = capitalizar_palabras(valor)
            if valor_capitalizado in cantidad_tipo:
                cantidad_tipo[valor_capitalizado] += 1
            else:
                cantidad_tipo[valor_capitalizado] = 1
    diccionario_salteado = json.dumps(cantidad_tipo, indent = 4)
    dict_final = json.loads(diccionario_salteado)
    return dict_final

def guardar_cantidad_heroes_tipo(diccionario, tipo_dato):
    '''
    La función  `guardar_cantidad_heroes_tipo`  recibe como entrada un diccionario y un tipo de dato. Verifica si la entrada es un diccionario y, si es así, itera sobre los pares clave-valor en el diccionario. Para cada par, crea una cadena de mensaje que incluye el tipo de dato, la clave y el valor. Luego guarda este mensaje en un archivo con un nombre específico basado en el tipo de dato. Si el archivo se guarda correctamente, la función devuelve True; de lo contrario, devuelve False.
    '''
    mensaje = ""
    if isinstance(diccionario, dict):
        for key, value in diccionario.items():
            mensaje += f"Caracteristica: {tipo_dato} {key} - Cantidad de heroes: {value}\n"
        nombre_archivo = f"heroes_cantidad_{tipo_dato}.csv"
        if guardar_archivo(nombre_archivo, mensaje):
            return True
        else:
            return False
    else:
        return False

def stark_calcular_cantidad_por_tipo(lista_heroes, tipo_dato):
    '''
    Esta función calcula la cantidad de un tipo de dato específico en una lista de héroes y lo guarda si es exitoso.
    '''
    cantidad_tipo = calcular_cantidad_tipo(lista_heroes, tipo_dato)
    if guardar_cantidad_heroes_tipo(cantidad_tipo, tipo_dato)  == True:
        return True
    else:
        return False

def obtener_lista_de_tipos(lista_heroes:list, dato:str):
    '''
    La función  obtener_lista_de_tipos  toma como entrada una lista de héroes y un tipo de dato, y devuelve un conjunto de valores únicos para ese tipo de dato.
    '''
    lista_valores = []
    for heroe in lista_heroes:
        valor = heroe.get(dato, "")
        if not valor:
            valor = "N/A"
        lista_valores.append(valor)
    lista_valores = set([capitalizar_palabras(valor) for valor in lista_valores])
    return lista_valores

def normalizar_dato(dato, valor_default):
    '''
    La función  `normalizar_dato`  recibe como entrada un dato y un valor por defecto ( `valor_default` ). Verifica si el dato está vacío o no. Si el dato está vacío, retorna el valor por defecto. De lo contrario, retorna el dato mismo.
    '''
    if not dato:
        return valor_default
    else:
        return dato

def normalizar_heroe(heroe:dict, clave:str):
    '''
    Este código define una función llamada  `normalizar_heroe`  que toma como entrada un diccionario  `heroe`  y una cadena  `clave` . La función normaliza el valor asociado con la clave dada en el diccionario  `heroe`  aplicando dos funciones de normalización:  `normalizar_dato`  y  `capitalizar_palabras` . También capitaliza el valor asociado con la clave "nombre" en el diccionario  `heroe` . Luego, la función devuelve el diccionario  `heroe`  modificado.
    '''
    if clave in heroe:
        valor = heroe[clave]
        valor_normalizado = normalizar_dato(valor, "N/A")
        valor_normalizado = capitalizar_palabras(valor_normalizado)
        heroe[clave] = valor_normalizado

    if "nombre" in heroe:
        nombre = heroe["nombre"]
        nombre_capitalizado = capitalizar_palabras(nombre)
        heroe["nombre"] = nombre_capitalizado

    return heroe

def obtener_heroes_por_tipo(lista_heroes:list, conjunto_tipos:set, clave_a_evaluar):
    '''
    La función  `obtener_heroes_por_tipo`  recibe una lista de héroes, un conjunto de tipos y una clave para evaluar. Crea un diccionario vacío para almacenar los héroes según sus tipos. Luego, itera sobre cada héroe en la lista y verifica si la clave existe en los atributos del héroe. Si existe, normaliza el valor y lo compara con cada tipo en el conjunto. Si hay una coincidencia, agrega el nombre del héroe al tipo correspondiente en el diccionario. Finalmente, devuelve el diccionario con los héroes agrupados por tipo.
    '''
    diccionario_variedades = {}

    for tipo in conjunto_tipos:
        diccionario_variedades[tipo] = []

    for heroe in lista_heroes:
        if clave_a_evaluar in heroe:
            valor = normalizar_dato(heroe[clave_a_evaluar], "N/A").lower()
            for tipo in conjunto_tipos:
                if valor == tipo.lower():
                    diccionario_variedades[tipo].append(heroe["nombre"])
        else:
            print('la clave no esta en la lista')
    return diccionario_variedades

def guardar_heroes_por_tipo(diccionario_variedades, tipo_dato):
    '''
    Esta función toma un diccionario de héroes categorizados por un tipo de dato específico y guarda los nombres de los héroes en un archivo CSV según su tipo de dato.
    '''
    mensaje = ""
    for tipo, heroes in diccionario_variedades.items():
        if heroes:
            nombres = " | ".join(heroes)
            mensaje += f"{tipo_dato} {tipo}: {nombres}\n"
    nombre_archivo = f"heroes_segun_{tipo_dato}.csv"
    return guardar_archivo(nombre_archivo, mensaje)

def stark_listar_heroes_por_dato(lista_heroes, tipo_dato):
    '''
    La función  `stark_listar_heroes_por_dato`  recibe una lista de héroes y un tipo de dato como entrada. Luego, obtiene una lista de tipos basada en el tipo de dato dado y crea un diccionario de héroes basado en estos tipos. Finalmente, guarda los héroes por tipo y devuelve el resultado.
    '''
    tipos = obtener_lista_de_tipos(lista_heroes, tipo_dato)
    diccionario_variedades = obtener_heroes_por_tipo(lista_heroes, tipos, tipo_dato)
    return guardar_heroes_por_tipo(diccionario_variedades, tipo_dato)

def imprimir_menu_desafio_5(menu:str):
    """
    La función  `imprimir_menu_desafio_5`  se encarga de imprimir un menú recibido como entrada.
    """
    print(menu)

##///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#1.2
def stark_menu():
    """
    La función  `stark_menu`  devuelve una cadena de texto que contiene una lista de opciones para una aplicación de superhéroes.
    """
    menu = """
    
    (✌ﾟ∀ﾟ)☞ stark 5 ლ(╹◡╹ლ)
    A. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M
    B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F
    C. Recorrer la lista y determinar cuál es el superhéroe más alto de género M
    D. Recorrer la lista y determinar cuál es el superhéroe más alto de género F
    E. Recorrer la lista y determinar cuál es el superhéroe más bajo de género M
    F. Recorrer la lista y determinar cuál es el superhéroe más bajo de género F
    G. Recorrer la lista y determinar la altura promedio de los superhéroes de género M
    H. Recorrer la lista y determinar la altura promedio de los superhéroes de género F
    I. Informar cual es el Nombre del superhéroe asociado a cada uno de los
        indicadores anteriores (ítems C a F)
    J. Determinar cuántos superhéroes tienen cada tipo de color de ojos.
    K. Determinar cuántos superhéroes tienen cada tipo de color de pelo.
    L. Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de
        no tener, Inicializarlo con No Tiene).
    M. Listar todos los superhéroes agrupados por color de ojos.
    N. Listar todos los superhéroes agrupados por color de pelo.
    O. Listar todos los superhéroes agrupados por tipo de inteligencia
    z. salir 
    """
    return menu


def validacion_de_menu(respuesta:str):
    """
    La función  `validacion_de_menu`  valida la entrada del usuario para una opción de menú. Verifica si la entrada es un único carácter entre 'a' y 'o' (sin importar mayúsculas o minúsculas), y devuelve la entrada si es válida. De lo contrario, devuelve -1.
    """
    validacion = r'^[a-oA-OzZ]$'
    if re.match(validacion,respuesta):
        mensaje = respuesta
    else:
        mensaje = -1 
    return mensaje


def stark_menu_principal_desafio_5():
    """
    Esta función se utiliza para mostrar un menú, solicitar al usuario una entrada, validar la entrada y devolver la entrada validada o -1 si la entrada no es válida.
    """
    menu = stark_menu()
    imprimir_menu_desafio_5(menu)
    respuesta = input()
    mensaje = validacion_de_menu(respuesta)
    return mensaje


def stark_marvel_app_5(lista_personajes):
    bandera = True
    stark_normalizar_datos(lista_personajes)
    while bandera:
        impresion = stark_menu_principal_desafio_5()
        if impresion == "A":
            stark_guardar_heroe_genero(lista_personajes, "M")
        ##///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        elif impresion == "B":
            stark_guardar_heroe_genero(lista_personajes, "F")
        ##///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        elif impresion == "C":
            dato = calcular_max_min_dato_genero("M", "maximo", "altura")
            imprimir_heroe(dato,'altura')
        ##///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        elif impresion == "D":
            dato = calcular_max_min_dato_genero("F", "maximo", "altura")
            imprimir_heroe(dato,'altura')
        ##///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        elif impresion == "E":
            dato = calcular_max_min_dato_genero("M", "minimo", "altura")
            imprimir_heroe(dato,'altura')
        ##///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        elif impresion == "F":
            dato = calcular_max_min_dato_genero("F", "minimo", "altura")
            imprimir_heroe(dato,'altura')
        ##///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        elif impresion == "G":
            dato = calcular_promedio_genero(lista_personajes,'altura',"M")
            print(f'El promedio de altura es {dato} ')
        ##///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        elif impresion == "H":
            dato = calcular_promedio_genero(lista_personajes,'altura',"F")
            print(f'El promedio de altura es {dato}')
        ##///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        elif impresion == "I":
                ALTURA = [calcular_max_min_dato_genero("M", "maximo", "altura")]
                for I in ALTURA:
                    print(F"NOMBRE DE LA PERSONA MAS ALTA MASCULINA : {I['nombre']}")
            ##//////////////////////////////////////////////////////////////////////////////////////////////////////////////            

                ALTURA = [calcular_max_min_dato_genero("F", "maximo", "altura")]
                for I in ALTURA:
                    print(F"NOMBRE DE LA PERSONA MAS ALTA MASCULINA : {I['nombre']}")
            ##//////////////////////////////////////////////////////////////////////////////////////////////////////////////            

                ALTURA = [calcular_max_min_dato_genero("M", "minimo", "altura")]
                for I in ALTURA:
                    print(F"NOMBRE DE LA PERSONA MAS BAJA MASCULINA : {I['nombre']}")
            ##//////////////////////////////////////////////////////////////////////////////////////////////////////////////            
                ALTURA = [calcular_max_min_dato_genero("F", "minimo", "altura")]
                for I in ALTURA:
                    print(F"NOMBRE DE LA PERSONA MAS BAJA FEMENINA  : {I['nombre']}")
        ##///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        elif impresion == "J":
            cantidad_color_ojos = calcular_cantidad_tipo(lista_personajes, "color_ojos")
            for color, cantidad in cantidad_color_ojos.items():
                print(f"Color de ojos: {color} - Cantidad de superhéroes: {cantidad}")
        ##///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        elif impresion == "K":
            cantidad_color_ojos = calcular_cantidad_tipo(lista_personajes, "color_pelo")
            for color, cantidad in cantidad_color_ojos.items():
                print(f"Color de pelo: {color} - Cantidad de superhéroes: {cantidad}")
        ##///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        elif impresion == "L":
            cantidad_color_ojos = calcular_cantidad_tipo(lista_personajes, "inteligencia")
            for color, cantidad in cantidad_color_ojos.items():
                print(f"Color de ojos: {color} - Cantidad de superhéroes: {cantidad}")
        ##///////////////////////////////////////////////////////////////////////////////////////////////////////////////////Lrevisar
        elif impresion == "M":
            tipos_color_ojos = obtener_lista_de_tipos(lista_personajes, "color_ojos")
            diccionario_heroes_por_color_ojos = obtener_heroes_por_tipo(lista_personajes, tipos_color_ojos, "color_ojos")
            for color_ojos, heroes in diccionario_heroes_por_color_ojos.items():
                print(f"Color de ojos: {color_ojos}")
                for heroe in heroes:
                    print(heroe)
                print()
        ##///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        elif impresion == "N":
            tipos_color_pelo = obtener_lista_de_tipos(lista_personajes, "color_pelo")
            diccionario_heroes_por_color_pelo = obtener_heroes_por_tipo(lista_personajes, tipos_color_pelo, "color_pelo")
            for color_pelo, heroes in diccionario_heroes_por_color_pelo.items():
                print(f"Color de pelo: {color_pelo}")
                for heroe in heroes:
                    print(heroe)
                print()
        ##///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        elif impresion == "O":
            lista_de_tipos_set = obtener_lista_de_tipos(lista_personajes, "inteligencia")
            diccionario_heroes_por_inteligencia = obtener_heroes_por_tipo(lista_personajes, lista_de_tipos_set, "inteligencia")
            for inteligencia, heroes in diccionario_heroes_por_inteligencia.items():
                print(f"Nivel inteligencia: {inteligencia}")
                for heroe in heroes:
                    print(heroe)
                print()
        ##///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        elif impresion == "Z":
            break
        else:
            print("COLOCAR ALGUNA LETRA VALIDA")