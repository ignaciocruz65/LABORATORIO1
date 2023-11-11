from data_stark import lista_personajes
import re

def extraer_iniciales(nombre_heroe:str):
    '''
    La funcion recibira como parametro un string, se validara que no este vacio y con una expresion regular se realizara un split de los caracteres en minuscula, guiones y espacios, con el metodo join se agregara a la cadena el .
    '''
    if (not nombre_heroe):
        return 'N/A'
    iniciales = re.split('[a-z- ]+', nombre_heroe)
    return '.'.join(iniciales)

def definir_iniciales_nombre(heroe:dict):
    '''
    La funcion recibira como parametro un diccionario de heroe, se verificara que el parametro sea un diccionario y que contenga una key llamada "nombre", y se agregara al diccionario la key "iniciales", en caso de que no se cumpla esto, la funcionr retornara false.
    '''
    for key in heroe:
        if isinstance(heroe, dict) and 'nombre' in key:
            nombre = heroe['nombre']
            lista_inicial = extraer_iniciales(nombre)
            heroe["iniciales"] = lista_inicial
            return lista_inicial
        else:
            return False

def agregar_iniciales_nombre(lista:list):
    '''
    La funcion recibira como parametro una lista de personajes, se validara que sea del tipo lista y que al menos tenga un elemento, y se reutilizara la funcion definir_iniciales_nombre como parametro el diccionario iterado, en caso de que la funcion retorne falso se imprimira por consola un mensaje de error, si no, pass.
    '''
    if not isinstance(lista,list) or not lista:
        return "No hay elementos"

    for item in lista:
        nombre_iniciales = definir_iniciales_nombre(item)
        if (nombre_iniciales is False):
            print('El origen de datos no contiene el formato correcto')
            break
        else:
            pass


def stark_imprimir_nombre_con_iniciales(lista):
    '''
    La funcion recibira como parametro una lista, se verificara que la lista no este vacia, que sea del tipo lista , si no es una lista retornara un mensaje "no hay elementos", en caso de que si, se verificara que la key "nombre" e "iniciales" se encuentren en personaje iterado, si lo estan, se imprmira por consola el mensaje y si no, se imprmira mensaje un error.
    '''
    agregar_iniciales_nombre(lista)
    if not isinstance(lista, list) or len(lista) == 0:
        return False
    for item in lista:
        if 'nombre' in item and 'iniciales' in item:
            print(f"* {item['nombre']} ({item['iniciales']})")
        else:
            print("*Nombre o iniciales faltantes")



def generar_codigo_heroe(hero_id:int, genero:str):
    '''
    La funcion recibira como parametro un id_heroe y un genero, se realizara una lista de las opciones validas, se verificara que el id_hero sea de tipo entero, si no lo es retornara N/A, se verificara que si el genero ingresado no esta en la lista si no lo esta retornara N/A,
    luego se verificara el genero ingresado, si es NB se agregaran siete ceros con la expresion zfill, si es M o F ocho ceros, la funcion retornara el codigo del heroe.
    '''
    generos = ['M', 'F', 'NB']
    if (not isinstance(hero_id, int)):
        return 'N/A'
    
    if not genero or genero not in generos:
        return 'N/A'
    
    if(genero == 'NB'):
        codigo_heroe = f"{genero}-{str(hero_id).zfill(7)}"
    else:
        codigo_heroe = f"{genero}-{str(hero_id).zfill(8)}"
    return codigo_heroe

def agregar_codigo_heroe(hero_id:int,heroe:dict):
    '''
    La funcion recibira como parametro un diccionario y un heroe_id, se verificara que la key "genero" se encuentre en el diccionario, se generara el codigo del heroe con la funcion generar_codigo_heroe y verificar que el largo de la lista sea igual a diez y retornara el heroe, si no se cumple retornara false.
    '''
    if ('genero' in heroe):
        genero = heroe['genero']
        lista_inicial = generar_codigo_heroe(hero_id,genero)
        if(len(lista_inicial) == 10):
            heroe["codigo_heroe"] = lista_inicial
            return heroe
        else:
            return False

def stark_generar_codigo_heroes(lista: list):
    '''
    La funcion recibira como parametro una lista, se verificara en una misma condicion si la lista esta vacia, o si todos los elementos de la lista son diccionarios y contienen la clave "genero", si alguna de estas condiciones no se cumple se imprime el mensaje de error, si se cumplen ambas condiciones se recorre la lista y con la funcion enumerate se le asigna a cada personaje un numero a medida que se recorre el for y se agrega el codigo heroe pasandole el parametro i(numero). Despues de recorrer la lista se imprimira el numero de codigos asignados, el primer heroe y el ultimo.
    '''
    if not lista or not all(isinstance(item, dict) and 'genero' in item for item in lista):
        print("La lista de personajes está vacía o El origen de datos no contiene el formato correcto.")
        return

    for i, personaje in enumerate(lista,1):
        codigo_heroe = agregar_codigo_heroe(i, personaje)        
    
    print(f"Se asignaron {i} códigos")
    print(f"El código del primer héroe es: {lista[0]}")
    print(f"El código del último héroe es: {lista[-1]}")


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
        return print('Datos normalizados :)')

def generar_indice_nombres(lista:list):
    '''
    La funcion recibe como parametro una lsita, se verifica que la lista no este vacia, si lo esta se retornara false, si no se creara una lista con los indices del nombre, se realizara un bucle con la lista y se tomara la key nombre con el valor iterado y con el metodo extend se agregara el nombre iterado con el metodo split, la funcion retornara la lista con los nombres separados.
    '''
    if not lista:
        return False
    else:
        indice_nombres = []
        for item in lista:
            nombre_iterado = item['nombre']
            indice_nombres.extend(nombre_iterado.split())
        return indice_nombres   

def stark_imprimir_indice_nombre(lista:list):
    '''
    La funcion recibira como parametro una lista, y se utilizara la funcion generar indice nombres en una variable, se usara el metodo join para agregarle el guion entre cadena y cadena.
    '''
    lista_nombres = generar_indice_nombres(lista)
    agrupar = '-'
    agrupar =  agrupar.join(lista_nombres)
    print(agrupar)

def convertir_cm_a_mtrs(valor_cm):
    '''
    La funcion recibira como parametro un valor en cm, el valor se convertira en un string, y se verificara que el string empiece con el signo negativo, y con expresion regular se verificara que sea un numero flotante, si se cumple retornara -1, si no se cumple, se convertira el valor cm en un numero flotante y se dividira en cien para obtener los metros, esto retornara el numero en metros. 
    '''
    valor_cm = str(valor_cm)
    if valor_cm.startswith('-') and re.match(r'^[-+]?[0-9]+(\.[0-9]+)?',valor_cm):
        return -1
    elif re.match(r'^[-+]?[0-9]+(\.[0-9]+)?',valor_cm):
        numero = float(valor_cm)
        numero_mts = numero / 100
        numero_mts = round(numero_mts, 2)
        return numero_mts    

def generar_separador(patron:str,largo:int,imprimir=True):
    '''
    La funcion recibira como parametro patron(string), largo(int) y un parametro opcional imprimir que por defecto estara en True, se verifica que el largo del patron sea mayor a uno y menor que dos caracteres y si el largo es un entero entre uno y doscientos treinta y cinco caracteres, si una de estas condiciones no se cumple retornara N/A, se genera un separador entre el patron por el largo, si imprimir esta true, se imprimira el separador en la consola, esto retornara separador
    '''
    if (len(patron) < 1 or len(patron) > 2)or(not isinstance(largo, int) or largo < 1 or largo > 235) :
        return 'N/A'
    separador = patron * largo
    if imprimir:
        print(separador)
    
    return separador

def generar_encabezado(titulo:str):
    '''
    La funcion recibe como parametro un titulo(string), se realiza un separador por el largo de la pantalla, se convierte el titulo mayusculas con el metodo upper y se imprime el encabezado, la funcion retornara encabezado.
    '''
    separador = '*' * 149
    titulo = titulo.upper()
    encabezado = f'{separador}\n{titulo}\n{separador}'
    return encabezado


def imprimir_ficha_heroe(dicc:dict):
    '''
    La función recibira como parametro un diccionario, se creara una línea separadora hecha de asteriscos. Se imprime el encabezado "PRINCIPAL" seguido de la línea separadora. La función imprime el nombre del héroe, iniciales, identidad secreta y compañía utilizando los valores del diccionario. Imprime el código del héroe utilizando el valor del diccionario. La función imprime otra línea separadora se convierte la altura del héroe de centímetros a metros utilizando la función convertir cm a mtrs. La función imprime el encabezado "FISICO" luego una línea separadora. Imprime la altura, peso y fuerza del héroe utilizando los valores del diccionario. La función imprime otra línea separadora. Imprime el encabezado "SEÑAS PARTICULARES" con una línea separadora. La función imprime el color de ojos y color de pelo del héroe utilizando los valores del diccionario.
    '''
    separador = '*' * 80
    print(separador)
    print("PRINCIPAL")
    print(separador)
    
    print(f"NOMBRE DEL HÉROE: {dicc['nombre']} ({dicc['iniciales']})")
    print(f"IDENTIDAD SECRETA: {dicc['identidad']}")
    print(f"CONSULTORA: {dicc['empresa']}")
    print(f"CÓDIGO DE HÉROE: {dicc['codigo_heroe']}")
    
    print(separador)
    
    altura_mts = convertir_cm_a_mtrs(dicc['altura'])
    
    print("FISICO")
    print(separador)
    print(f"ALTURA: {altura_mts} Mtrs.")
    print(f"PESO: {dicc['peso']} Kg.")
    print(f"FUERZA: {dicc['fuerza']} N")
    
    print(separador)
    
    print("SEÑAS PARTICULARES")
    print(separador)
    print(f"COLOR DE OJOS: {dicc['color_ojos']}")
    print(f"COLOR DE PELO: {dicc['color_pelo']}")


def stark_navegar_fichas(lista:list):
    '''
    La funcion recibe como parametro una lista, luego se inicializa la variable "item" en 0 y calcula el número total de héroes en la lista,entra en un bucle while que continúa hasta que el usuario elija salir, obtiene el héroe actual de la lista utilizando el índice item, llama a la función "imprimir_ficha_heroe" para imprimir los detalles del héroe actual, se solicita al usuario que ingrese una opción: 1 para moverse al héroe anterior, 2 para moverse al siguiente héroe o S para salir, y si el usuario elige 1, actualiza el índice item al héroe anterior utilizando el módulo, si el usuario elige 2, actualiza el índice item al siguiente héroe de manera circular utilizando el módulo, si el usuario elige S, se imprime un mensaje de salida y sale del bucle y si el usuario ingresa una opción no válida, se imprime un mensaje de error y solicita nuevamente.
    '''
    item = 0
    total_heroes = len(lista)
    
    while True:
        heroe_actual = lista[item]
        imprimir_ficha_heroe(heroe_actual)
        
        opcion = input("Ingrese una opción:[1] Ir a la izquierda, [2] Ir a la derecha, [S] Salir: ")
        
        if opcion == '1':
            item = (item - 1) % total_heroes
        elif opcion == '2':
            item = (item + 1) % total_heroes
        elif opcion.upper() == 'S':
            print('¡Hasta luego!')
            break
        else:
            print("Opción inválida. Intente nuevamente.")

def imprimir_menu():
    '''
    La funcionr no recibe parametros, se encarga de imprimir el menu para que el usuario decida.
    '''
    print("1 - Imprimir la lista de nombres junto con sus iniciales\n2 - Generar códigos de héroes\n3 - Normalizar datos\n4 - Imprimir índice de nombres\n5 - Navegar fichas\nS - Salir")

def stark_menu_principal():
    '''
    La funcion no recibe parametros, se encarga de imprimir el menu y de pedirle al usuario que ingrese la opcion que desee. LA funcion retornara la opcion solicitada.
    '''
    imprimir_menu()
    opcion = input("Ingrese la opcion que desee")
    return opcion

def stark_marvel_app_3(lista:list):
    '''
    La funcion recibe como parametro una lista, entra en un bucle while true hasta que el usuario elija salir, en el bucle, la función llama a la función stark_menu_principal para mostrar un menú y solicitar al usuario una opción, si la opción es uno, la función llama a la función stark_imprimir_nombre_con_iniciales para imprimir nombres con iniciales, si la opción es dos la función llama a la función stark_generar_codigo_heroes para generar códigos de héroe, si la opción es tres la función llama a la función stark_normalizar_datos para normalizar datos, si la opción es cuatro llama a la función stark_imprimir_indice_nombre para imprimir el índice y el nombre, si la opción es cinco llama a la función stark_navegar_fichas para navegar por los perfiles de los personajes y si la opción es S la función imprime un mensaje y sale del bucle finalizando el programa
    '''
    while True:
        opcion = stark_menu_principal()
        if opcion == '1':
            stark_imprimir_nombre_con_iniciales(lista)
        elif opcion == '2':
            stark_generar_codigo_heroes(lista)
        elif opcion == '3':
            stark_normalizar_datos(lista)
        elif opcion == '4':
            stark_imprimir_indice_nombre(lista)
        elif opcion == '5':
            stark_navegar_fichas(lista)
        elif opcion.upper() == "S":
            print('Saliendo del programa.¡Hasta luego!')
            break

stark_marvel_app_3(lista_personajes)