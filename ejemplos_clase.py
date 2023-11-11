import copy
import re













###############################EJEMPLOS OCTUBRE4##############################################################

alumno = { "nombre":"Juan", "apellido":"perez", "edad":20,"notas":[85,90,78]}


def obtener_propiedad(diccionario,clave):
    existe = diccionario.get(clave, "La propiedad no existe")
    if existe == "La propiedad no existe":
        print("la clave no existe se agrega")
        diccionario[clave] = ""
    else:
        return diccionario[clave]

def eliminar_propiedad(diccionario,clave):
    if clave in diccionario:
        valor = diccionario.pop(clave)
        print(valor)
    else:
        print("la clave no existe")

def mostrar(diccionario):
    for clave, valor in diccionario.items():
        print(f"{clave}:{valor}")




mostrar(alumno)
eliminar_propiedad(alumno,"edad")

copia_superficial = copy.copy(alumno)
print("copia sup")
mostrar(copia_superficial)
'''
copia_duda = alumno
print("copia ...")
mostrar(copia_duda)
'''
copia_profunda = copy.deepcopy(alumno)
print("copia profunda")
mostrar(copia_profunda)


copia_superficial["nombre"]= "maria"
copia_superficial["notas"].append(100)

'''
copia_duda["nombre"]= "anabella"
copia_duda["notas"].append(45)
'''
copia_profunda["nombre"]= "renatto"
copia_profunda["notas"].append(98)


print("Diccionario original")
print(alumno)
print(id(alumno["notas"]))
print("diccionario con copy")
print(copia_superficial)
print(id(copia_superficial["notas"]))
'''
print("copia duda")
print(copia_duda)
'''
print("copia profunda")
print(copia_profunda)
print(id(copia_profunda["notas"]))






name = "Marina Anabella Cardozo"

print(re.findall("[a-z]+",name))

texto = "uno 1 dos 2 tres 3 cuatro 44"

print(re.findall(" ",texto))
print(re.findall("[0-9]",texto))
print(re.findall("[0-9]+",texto))
print(re.findall("[a-z]",texto))
print(re.findall("[a-z]+",texto))
print(re.findall("[a-z]{6}",texto))

texto = "La fecha de inicio es 2023/09/20 y la fecha de finalización es 2023/09/30."


'''
  \s ---> todos los caracteres que representan un espacio  
  \d ---> todos los caracteres que representan los decimales
\w ----> alfa numericos 

'''
print(re.findall("[0-9]{4}/[0-9]{2}/[0-9]{2}",texto))
print(re.findall("\d{4}/\d{2}/\d{2}",texto)) #te retorna una lista con las ocurrencias encontradas

print(re.search("[0-9]{4}/[0-9]{2}/[0-9]{2}",texto))

search_match = re.search("[0-9]{4}/[0-9]{2}/[0-9]{2}",texto) #retorna un obj match

if search_match != None:
    print("Si encontro una fecha:", search_match.group())
    print("Posicion inicio: ", search_match.start())
    print("Posicion fin: ", search_match.end())
'''
ingreso = input("Ingrese edad")

if re.match('[0-9]+',ingreso) != None:
    numero_parseado = int(ingreso)
    print(numero_parseado)
else:
    print("hubo un error")
'''
otro_texto="hola, todo bien?"

print(re.split("\s+",otro_texto))#esto retora una lista, separadas por el patron 

otro_texto_bis = "abc abc ccc ddd abc aaa"

print(re.sub("abc","",otro_texto_bis))
print(re.sub("abc","xyz",otro_texto_bis))
print(re.sub("\s+","",otro_texto_bis))
