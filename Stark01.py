from data_stark import lista_personajes
from Stark01Functions import *


stark_menu = input('Ingrese una letra del A-J para ingresar')

preg = True
while preg:
    match(stark_menu):
        case 'A':
            verificarNB(lista_personajes)
            break
        case 'B':
            max_height_gen_f(lista_personajes)
            break
        case 'C':
            max_height_gen_m(lista_personajes)
            break
        case 'D':
            min_strenght_gen_m(lista_personajes)
            break
        case 'E':
            min_strenght_gen_nb(lista_personajes)
            break
        case 'F':
            promedio_super_nb(lista_personajes)
            break
        case 'G':
            print_verif_c_o()
            break
        case 'H':
            imprimir_c_p()
            break
        case 'I':
            imprimir_c_o()
            break
        case 'J':
            imprimir_intelig()
            break
        case _: 
            print('El string es incorrecto')
            preg = False