from data_stark_1 import lista_personajes
# A. Recorrer la lista imprimiendo por consola todos los datos de cada superhéroe
# B. Recorrer la lista y mostrar la identidad y el peso del superhéroe con mayor
# fuerza (MÁXIMO)
# C. Recorrer la lista y mostrar nombre e identidad del superhéroe más bajo
# (MÍNIMO)
# D. Recorrer la lista y determinar el peso promedio de los superhéroes
# masculinos (PROMEDIO)
# E. Recorrer la lista y mostrar nombre y peso de los superhéroes (cualquier
# género) los cuales su fuerza supere a la fuerza promedio de todas las
# superhéroes de género femenino

# NOTA: Se debe construir un menú en el que se sea posible acceder a cada una de
# las opciones (A-E)

personaje_min_height = None
personaje_max_strong = None
identidad_max = None
peso_max = None
identidad_min = None
nombre_min = None
accumulator_pesos = 0
listlen = 0
listlen_f = 0
accumulator_fuerzas_mujer = 0
lista_mayores = []
lista_fuerza_max = []

for personaje in lista_personajes:
    # B. Recorrer la lista y mostrar la identidad y el peso del superhéroe con mayor
    # fuerza (MÁXIMO)
    personaje_actual_int = int(personaje["fuerza"])
    if personaje_max_strong is None or personaje_max_strong < personaje_actual_int:
        personaje_max_strong = personaje_actual_int
        identidad_max = personaje["identidad"]
        peso_max = personaje["peso"]
        lista_fuerza_max = [{'identidad': identidad_max, 'peso': peso_max, 'fuerza': personaje_max_strong}]
    elif personaje_max_strong == personaje_actual_int:
        lista_fuerza_max.append({'identidad': personaje["identidad"], 'peso': personaje["peso"], 'fuerza': personaje_actual_int})
    # C. Recorrer la lista y mostrar nombre e identidad del superhéroe más bajo
    # (MÍNIMO)
    personaje_actual_altura_int = float(personaje["altura"])
    if(personaje_min_height == None or personaje_min_height > personaje_actual_altura_int):
        personaje_min_height = personaje_actual_altura_int
        identidad_min = personaje["identidad"]
        nombre_min = personaje["nombre"]
    # D. Recorrer la lista y determinar el peso promedio de los superhéroes
    # masculinos (PROMEDIO)
    peso_actual_float = float(personaje["peso"])
    genero_actual = personaje["genero"]
    if(genero_actual == 'M' and peso_actual_float > 0):
        accumulator_pesos += peso_actual_float
        listlen += 1
    # E. Recorrer la lista y mostrar nombre y peso de los superhéroes (cualquier
    # género) los cuales su fuerza supere a la fuerza promedio de todas las
    # superhéroes de género femenino
    fuerza_actual_float = float(personaje["fuerza"])
    if(genero_actual == 'F' and fuerza_actual_float > 0):
        accumulator_fuerzas_mujer += fuerza_actual_float
        listlen_f += 1

#PROMEDIOS
average = accumulator_pesos / listlen
average_f = accumulator_fuerzas_mujer / listlen_f

#LISTADO DE SUPERHEROES MAYORES A PROMEDIO DE MUJERES
for i in lista_personajes:
    fuerza_actual_float = float(i["fuerza"])
    if(fuerza_actual_float > average_f):
        lista_mayores.append({'nombre':i["nombre"],'peso':i['peso'],'fuerza':i["fuerza"]})

#MENSAJES A PRINTEAR
mensaje_c = (f'El personaje mas bajo es {nombre_min} {identidad_min} y su altura es {personaje_min_height} ')
mensaje_d = (f'el promedio de los pesos superheroes masculinos es {average}')

menu_stark = input('ingrese una letra del A-E para acceder a los resultados')
match(menu_stark):
    case 'A':
        for personaje in lista_personajes:
            print("-------------------------")
            for atributo in personaje:
                print(atributo,":",personaje[atributo])
    case 'B':
        for iter in lista_fuerza_max:
            print(f'los superheroes maximos son {iter["identidad"]}, con fuerza {iter["fuerza"]} y peso {iter["peso"]} ')
    case 'C':
        print(mensaje_c)
    case 'D':
        print(mensaje_d)
    case 'E':
        print(f'Lista de superheroes con fuerza mayor al promedio de mujeres que es {average_f}:')
        for personaje in lista_mayores:
            print(f"Nombre: {personaje['nombre']}\n Peso: {personaje['peso']}\n Fuerza: {personaje['fuerza']}")
    case _:
        print('opcion incorrecta ingrese nuevamente')
        