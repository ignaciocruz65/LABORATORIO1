from data_stark import lista_personajes
from Stark02Functions import *



preg = True
while preg:
    stark_menu = input('Ingrese una letra del A-J para mostrar los informes, si desea salir ingrese Q\nA. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género NB\nB. Recorrer la lista y determinar cuál es el superhéroe más alto de género F\nC. Recorrer la lista y determinar cuál es el superhéroe más alto de género M\nD. Recorrer la lista y determinar cuál es el superhéroe más débil de género M\nE. Recorrer la lista y determinar cuál es el superhéroe más débil de género NB\nF. Recorrer la lista y determinar la fuerza promedio de los superhéroes de género NB\nG. Determinar cuántos superhéroes tienen cada tipo de color de ojos.\nH. Determinar cuántos superhéroes tienen cada tipo de color de pelo.\nI. Listar todos los superhéroes agrupados por color de ojos.\nJ. Listar todos los superhéroes agrupados por tipo de inteligencia\nIngrese la opcion')
    match(stark_menu):
        case 'A':
            verificarNB(lista_personajes)
        case 'B':
            max_height_gen_f(lista_personajes)
        case 'C':
            max_height_gen_m(lista_personajes)
        case 'D':
            min_strenght_gen_m(lista_personajes)
        case 'E':
            min_strenght_gen_nb(lista_personajes)
        case 'F':
            promedio_super_nb(lista_personajes)
        case 'G':
            print_verif_c_o()
        case 'H':
            imprimir_c_p()
        case 'I':
            imprimir_c_o()
        case 'J':
            imprimir_intelig()
        case 'Q': 
            print('Saliendo del menu')
            preg = False