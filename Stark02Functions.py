from data_stark import lista_personajes


# Desafío #02:
# Usando como base lo realizado en el anterior desafío realizar los siguientes
# informes en un menú


'''FUNCTIONS'''

# A. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de
# género NB
def verificarNB(lista_personajes):
    for iter in lista_personajes:
        if(iter['genero'] == 'NB'):
            print(iter['nombre'])

# B. Recorrer la lista y determinar cuál es el superhéroe más alto de género F
def max_height_gen_f(lista_personajes):
    max_height_f = 0
    name_max_height_f = ""
    for iter in lista_personajes:
        if iter["genero"] == "F" and float(iter["altura"]) > float(max_height_f):
            max_height_f = iter["altura"]
            name_max_height_f = iter["nombre"]
    print(f"El superhéroe más alto de género F es: {name_max_height_f}")

# C. Recorrer la lista y determinar cuál es el superhéroe más alto de género M

def max_height_gen_m(lista_personajes):
    max_height_m = 0
    name_max_height_m = ""
    for iter in lista_personajes:
        if iter["genero"] == "M" and float(iter["altura"]) > float(max_height_m):
            max_height_m = iter["altura"]
            name_max_height_m = iter["nombre"]
    print(f"El superhéroe más alto de género M es: {name_max_height_m}")

# D. Recorrer la lista y determinar cuál es el superhéroe más débil de género M

def min_strenght_gen_m(lista_personajes):
    min_strenght_m = None
    name_min_strenght_m = ""
    for iter in lista_personajes:
        actual_strenght = int(iter["fuerza"])
        if (iter["genero"] == "M") and (min_strenght_m == None or min_strenght_m > actual_strenght) :
            min_strenght_m = actual_strenght
            name_min_strenght_m = iter["nombre"]
    print(f"El superhéroe más debil de género M es: {name_min_strenght_m} y su fuerza es {min_strenght_m}")

# E. Recorrer la lista y determinar cuál es el superhéroe más débil de género NB

def min_strenght_gen_nb(lista_personajes):
    min_strenght_nb = None
    name_min_strenght_nb = ""
    for iter in lista_personajes:
        actual_strenght = int(iter["fuerza"])
        if (iter["genero"] == "NB") and (min_strenght_nb == None or min_strenght_nb > actual_strenght) :
            min_strenght_nb = actual_strenght
            name_min_strenght_nb = iter["nombre"]
    print(f"El superhéroe más debil de género NB es: {name_min_strenght_nb} y su fuerza es {min_strenght_nb}")

# F. Recorrer la lista y determinar la fuerza promedio de los superhéroes de
# género NB

def promedio_super_nb(lista_personajes):
    iterator_nb = 0
    accumulator_nb = 0
    
    for iter in lista_personajes:
        actual_strenght = int(iter['fuerza'])
        if(iter['genero'] == 'NB'):
            iterator_nb += 1
            accumulator_nb += actual_strenght
    if(iterator_nb>0):
        average_nb = accumulator_nb / iterator_nb
        print(f'El promedio de las fuerzas del genero NB es {average_nb}')
    else:
        print('No hay NB')

# G. Determinar cuántos superhéroes tienen cada tipo de color de ojos.

def verificar_color_ojos(lista_personajes):
    count_ojos = {}
    for iter in lista_personajes:
        actual_color = iter['color_ojos'].lower()

        if actual_color in count_ojos:
            count_ojos[actual_color] += 1
        else:
            count_ojos[actual_color] = 1

    return count_ojos

def print_verif_c_o():
    resultado_conteo = verificar_color_ojos(lista_personajes)
    for color in resultado_conteo:
        cantidad = resultado_conteo[color]
        print(f"Color de ojos: {color} - Cantidad: {cantidad}")


# H. Determinar cuántos superhéroes tienen cada tipo de color de pelo.

def verificar_color_pelo(lista_personajes):
    count_pelo = {}
    for iter in lista_personajes:
        actual_color = iter['color_pelo'].lower()

        if actual_color in count_pelo:
            count_pelo[actual_color] += 1
        else:
            count_pelo[actual_color] = 1
    return count_pelo

def imprimir_c_p():
    resultado_conteo_pelo = verificar_color_pelo(lista_personajes)
    for color in resultado_conteo_pelo:
        cantidad = resultado_conteo_pelo[color]
        print(f"Color de pelo: {color} - Cantidad: {cantidad}")

# I. Listar todos los superhéroes agrupados por color de ojos.

def lista_color_ojos(lista_personajes):
    dicc = {}
    for iter in lista_personajes:
        color_ojos = iter["color_ojos"].lower()
        
        if color_ojos in dicc:
            dicc[color_ojos].append(iter["nombre"])
        else:
            dicc[color_ojos] = [iter["nombre"]]        
    return dicc

def imprimir_c_o():
    conteo_ojos = lista_color_ojos(lista_personajes)
    for color in conteo_ojos:
        print(f"Color de ojos: {color}")
        for nombre in conteo_ojos[color]:
            print(f"- {nombre}")

# J. Listar todos los superhéroes agrupados por tipo de inteligencia

def listar_inteligencia(lista_personajes):
    dicc = {}
    for iter in lista_personajes:
        inteligencia = iter['inteligencia']
        
        if inteligencia in dicc:
            dicc[inteligencia].append(iter["nombre"])
        else:
            dicc[inteligencia] = [iter["nombre"]]        
    return dicc
def imprimir_intelig():
    conteo_inteligencia = listar_inteligencia(lista_personajes)
    for inteligencia in conteo_inteligencia:
        print(f"Inteligencia: {inteligencia}")
        for nombre in conteo_inteligencia[inteligencia]:
            print(f"- {nombre}")