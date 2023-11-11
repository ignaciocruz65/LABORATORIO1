from data_stark import lista_personajes
import re

def stark_normalizar_datos(lista_personajes:list):
    '''La funcion recibe como parametro una lista, que recorre y verifica que la lista no este vacia, que el tipo de dato no sea del tipo que se requiera castear, en caso de que el valor no sea valido, o se mostrara por consola el error al intentar normalizar.'''
    if not lista_personajes:
        print('La lista está vacía.')
        return False
    modified = False
    for personaje in lista_personajes:
        if 'fuerza' in personaje:
            personaje['fuerza'] = int(personaje['fuerza'])
            modified = True
        if 'altura' in personaje:
            personaje['altura'] = float(personaje['altura'])
            modified = True
        if 'peso' in personaje:
            personaje['peso'] = float(personaje['peso'])
            modified = True
    if modified:
        print('Datos normalizados :)')
    else:
        print('Hubo un error al normalizar los datos. Verifique que la lista no esté vacía o que los datos ya no se hayan normalizado anteriormente.')

def obtener_dato(diccionario:list,clave:str):
    '''La funcion recibe como parametro un diccionario y una clave, este recorre el diccionario, valida que el diccionario no esta vacio y que tiene la clave solicitada, si la clave existe se imprime el dato.'''
    modified = False
    if((diccionario) and ('nombre' in diccionario)):
        print(f'El dato es {diccionario[clave]}')
        modified = diccionario[clave]
    return modified

def obtener_nombre(diccionario:list):
    '''La funcion recibe como parametro un diccionario, este recorre el diccionario, valida que el diccionario no esta vacio y que tiene la clave "nombre", si la clave existe se imprime el dato, si no, la funcion retornara false.'''
    nombre = obtener_dato(diccionario, 'nombre')
    if nombre:
        print(f'Nombre: {diccionario["nombre"]}')
        return nombre
    else:
        return False

def obtener_nombre_y_dato(diccionario:list,clave2:str):
    '''La funcion recibe como parametro un diccionario y una clave, valida que la clave nombre exista en el diccionario, y que la clave solicitada exista, si las claves existen, se muestra por consola el nombre y el dato solicitado, en caso de que no existan se imprime un mensaje del error '''
    for diccionario in diccionario:
        if 'nombre' in diccionario:
            nombre = diccionario['nombre']
            if clave2 in diccionario:
                valor = diccionario[clave2]
                print(f'Nombre: {nombre} | {clave2.capitalize()}: {valor}')
            else:
                print(f'La clave "{clave2}" no existe en el diccionario para {nombre}.')
        else:
            print("El diccionario está vacío o no tiene la clave 'nombre'.")

def obtener_maximo(lista: list,clave1:str):
    '''La funcion recibe como parametro una lista y una clave, iteramos la lista y verificamos que la lista no este vacia, o que la clave no este en la lista, en caso de que se cumpla, retornara false, si no, se obtiene el maximo del dato solicitado, y se imprime por consola.'''
    num_max = None
    modified = False
    
    for iter in lista:
        if not lista and clave1 not in lista:
            return modified
        valor = iter[clave1]
        if num_max is None or num_max < valor:
            num_max = valor
            modified = True
            nombre_mayor = iter['nombre']
            
    
    print(f'El numero maximo es {num_max} y es {nombre_mayor}')
    return num_max

def obtener_minimo(lista:list,clave1:str):
    '''La funcion recibe como parametro una lista y una clave, iteramos la lista y verificamos que la lista no este vacia, o que la clave no este en la lista, en caso de que se cumpla, retornara false, si no, se obtiene el minimo del dato solicitado, y se imprime por consola.'''
    num_min = None
    modified = False
    
    for iter in lista:
        if not lista and clave1 not in lista:
            return modified
        valor = iter[clave1]
        if num_min is None or num_min > valor:
            num_min = valor
            modified = True
            nombre_menor = iter['nombre']
    
    print(f'El numero minimo es {num_min} y es {nombre_menor}')
    return num_min

def obtener_dato_cantidad(lista:list,dato1:str,clave1:str):
    '''
    La funcion recibe como parametro una lista, un dato a buscar, y la clave, se verifica que los datos iterados cumplan con la condicion del dato solicitado y se agrega a una lista. En caso de que no cumplan la condicion la funcion retornara false.
    '''
    container_characters = []
    if not lista:
        print('La lista esta vacia')
        return False
    for iter in lista:
        if (dato1 == iter[clave1]):
            container_characters.append(iter)
            print(f'Nombre:{iter["nombre"]} | {clave1}: {iter[clave1]}')

    if len(container_characters) == 0:
        return False
    else:
        return container_characters

def stark_imprimir_heroes(dicc):
    '''La funcion recibe como parametro un diccionario la cual se imprimira por consola'''
    if not dicc:
        print('nohaynada')
        return False
    else:
        for dato,personajes in dicc.items():
            print(f'{dato.capitalize()}: {personajes}')

def sumar_dato_heroe(lista:list, clave:str):
    '''La funcion recibe como parametro una lista y una clave, se valida que la lista no este vacia, luego se recorre la lista comprobando que la clave solicitada exista, si la clave es un string se agregara a la variable no numero, si no, se suma el valor solicitado, si una de las dos variables es mayor a 0 se retornara esa variable'''
    if not lista:
        print('La lista esta vacia')
        return False
    suma = 0
    suma_no_num = 0
    for iter in lista:
        if (clave.isalpha() in iter):
            suma_no_num += 1
        elif clave in iter:
            suma += iter[clave]
    if suma > 0:
        return suma
    elif suma_no_num > 0:
        return suma_no_num

def dividir(divisor,dividendo):
    '''La funcion recibe como parametro dos numeros, dividendo y divisor, se verifica que el diviso sea distinto a 0, si lo es retornara la funcion como false, en caso de que no, se realizara la division'''
    if(divisor != 0):
        div = divisor/dividendo
        return div
    else:
        return False

def calcular_promedio(lista:list, clave1):
    '''La funcion recibira como parametro una lista y una clave, se llamara a la opcion sumar_dato_hero, que servira de acumulador, con la funcion len buscaremos el largo de la lista, y con la funcion dividir, que recibe parametros de divisor y dividendo, a las variables accumulador_heroes y lista_len'''
    lista_len=len(lista)
    accumulador_heroes = sumar_dato_heroe(lista,clave1)
    promedio = dividir(accumulador_heroes,lista_len)
    return promedio

def mostrar_promedio_dato(lista:list,clave1:str):
    '''La funcion recibira como parametro una lista y una clave del dato que se quiere obtener,,se valida que la lista no este vacia y que la clave sea de tipo int o float, si no lo es la funcion retornara como false, en caso de que si sea se imprimira por consola el promedio solicitado. '''
    if not lista:
        print('la lista vacia')
    for iter in lista:
        if clave1 in iter:
            dato = iter[clave1]
            if (type(dato) == int) or (type(dato) == float):
                print("El promedio es:")
                print(calcular_promedio(lista,clave1))
                return True
            else:
                print(f"No se encontraron valores numéricos en la clave '{clave1}'")
                return False


def lista_color(dicc,clave1):
    '''
    La funcion recibe como parametro un diccionario y una clave, se recorre el diccionario y se verifica que el dato solicitado este en el,
    en caso de que el dato se encuentre, se agrega al diccionario, caso contrario se crea una nueva clave color en el diccionario y le asigna una lista que contiene el nombre del elemento actual.
    '''
    dicct = {}
    for iter in dicc:
        dato = iter[clave1].lower()
        if dato in dicct:
            dicct[dato].append(iter["nombre"])
        else:
            dicct[dato] = [iter["nombre"]]      
    return dicct

def listar_cantidad(dicc,clave1):
    '''La funcion recibe como parametro un diccionario y una clave, se recorre el diccionario y se verifica que el dato solicitado este en el, en caso de que el dato se encuentre, se agrega al diccionario, caso contrario se crea una nueva clave del dato en el diccionario y le asigna una lista que contiene el nombre del elemento actual.'''
    dicct = {}
    for iter in dicc:
        actual_color = iter[clave1].lower()

        if actual_color in dicct:
            dicct[actual_color] += 1
        else:
            dicct[actual_color] = 1
    return dicct


def imprimir_menu():
    '''La funcion imprime el menu.'''
    print("Menú Principal:")
    print("1. Normalizar datos (No se debe poder acceder a los otros puntos)")
    print("2. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género NB")
    print("3. Recorrer la lista y determinar cuál es el superhéroe más alto de género F")
    print("4. Recorrer la lista y determinar cuál es el superhéroe más alto de género M")
    print("5. Recorrer la lista y determinar cuál es el superhéroe más débil de género M)")
    print("6. Recorrer la lista y determinar cuál es el superhéroe más débil de género NB")
    print("7. Recorrer la lista y determinar la fuerza promedio de los superhéroes de género NB")
    print("8. Determinar cuántos superhéroes tienen cada tipo de color de ojos")
    print("9. Determinar cuántos superhréoes tienen cada tipo de color de pelo")
    print("10. Listar todos los superhéroes agrupados por color de ojos")
    print("11. Listar todos los superhéroes agrupados por tipo de inteligencia")
    print("12. Salir")

def validar_entero(num):
    '''La funcion recibe como parametro un string de número, este se verificara si es un digito y retornara un true. En caso contrario retornara un false.'''
    if num.isdigit():
        return True
    else:
        return False

def stark_menu_principal():
    '''La funcion que se le otorga a esta es pedirle al usuario que ingrese un numero de las opciones elegidas, se validara que sea un numero, en caso de serlo se retornara la funcion casteada a int, en caso de que no lo sea se imprimira un mensaje de error y se retornara false.'''
    while True:
        imprimir_menu()
        opcion = input('Ingrese el número de la opción deseada (o Q para salir): ').strip().lower()
        if validar_entero(opcion):
            return int(opcion)
        else:
            print("Opcion no valida. Ingrese solo digitos")
            return False    

def stark_marvel_app(lista):
    '''La funcion se encargara de ejecutar nuestro programa al pasar por parametro una lista.'''
    flag = False
    while True:
        opcion = stark_menu_principal()
        if opcion == 1:
            stark_normalizar_datos(lista)
            flag = True
        if flag == True:
            if opcion == 2:
                lista_nb = obtener_dato_cantidad(lista,'NB','genero')
                
            elif opcion == 3:
                lista_f = obtener_dato_cantidad(lista,'F','genero')
                obtener_maximo(lista_f,'altura')
                
            elif opcion == 4:
                lista_m = obtener_dato_cantidad(lista,'M','genero')
                obtener_maximo(lista_m,'altura')
                
            elif opcion == 5:
                lista_m = obtener_dato_cantidad(lista,'M','genero')
                obtener_minimo(lista_m,'fuerza')
                
            elif opcion == 6:
                lista_nb = obtener_dato_cantidad(lista,'NB','genero')
                obtener_minimo(lista_nb,'fuerza')
                
            elif opcion == 7:
                lista_nb = obtener_dato_cantidad(lista,'NB','genero')
                mostrar_promedio_dato(lista_nb,'fuerza')
                
            elif opcion == 8:
                lista_ojos = listar_cantidad(lista,'color_ojos')
                stark_imprimir_heroes(lista_ojos)
                
            elif opcion == 9:
                lista_pelo = listar_cantidad(lista,'color_pelo')
                stark_imprimir_heroes(lista_pelo)
                
            elif opcion == 10:
                lista_colores_pelo = lista_color(lista,'color_pelo')
                stark_imprimir_heroes(lista_colores_pelo)
                
            elif opcion == 11:
                lista_inteligencia = lista_color(lista,'inteligencia')
                stark_imprimir_heroes(lista_inteligencia)
                
            elif opcion == 12:
                print("¡Hasta luego!")
                break
        else:
            print("Debe normalizar los datos para acceder a los siguientes puntos")
