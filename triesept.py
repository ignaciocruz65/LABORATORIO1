import sqlite3


def intentos(intentos: int):
    retorno = None
    for iter in range(intentos):
        valor = input('Ingrese su primer nombre: ')
        try:
            valor = int(valor)
            retorno = valor
            break
        except ValueError:
            print('El valor ingresado no es una palabra.')
    return retorno

intentos(2)