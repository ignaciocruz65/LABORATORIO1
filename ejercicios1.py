import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=10, columnspan=2, sticky="nsew")

        self.btn_cargar = customtkinter.CTkButton(master=self, text="Cargar", command=self.btn_cargar_on_click)
        self.btn_cargar.grid(row=3, pady=10, columnspan=2, sticky="nsew")
    
    
    # En el parque de diversiones "Aventuras Extremas", un grupo de amigos ha decidido disfrutar
    # del día probando las diferentes atracciones y luego se reúnen en un restaurante para compartir
    # un delicioso almuerzo. Antes de que llegue la cuenta, deciden crear un programa para calcular
    # y dividir los gastos de manera equitativa. Se pide ingresar los siguientes datos hasta que el
    # usuario lo desee:
    # Para cada amigo:
    # Se conocen los siguientes precios base:

    # El precio unitario de cada plato principal es de $800.
    # El precio unitario de cada bebida es de $200.
    # Una vez ingresados todos los datos, el programa debe calcular e informar lo siguiente:
    # A) El total gastado por el grupo (resultante del costo de los platos principales y las
    # bebidas), y la propina sugerida para el personal del restaurante (esta corresponde al
    # 10% del total gastado).
    # B) Promedio del dinero gastado en “Jugo”, sobre el grupo de amigos en general.
    # C) Los porcentajes de cada tipo de platos pedidos (teniendo en cuenta su cantidad).
    # Ejemplo: [30% pizza, 40% ensaladas, 30% hamburguesas]
    # D) Además, desean premiar al amigo que realizó la mayor CANTIDAD de pedidos en total
    # (platos principales + bebidas) con una entrada gratuita para otra atracción del parque
    # "Aventuras Extremas".
    # E) REALIZAR DOS PUNTO; EL PRIMERO CORRESPONDIENTE AL ÚLTIMO NÚMERO
    # DE SU DNI PERSONAL (Ejemplo 4) Y EL SEGUNDO RESTANDO A 9 EL ÚLTIMO
    # NÚMERO DE SU DNI (Ejemplo 9 - 4 = 5):
    # 0.- Crear una lista nueva, agregar todos los nombres de los amigos que hayan elegido platos
    # principales del tipo "Pizza" y mostrar la lista completa por print.
    # 1.- Crear una lista nueva, agregar todos los nombres de los amigos que hayan elegido
    # platos principales del tipo "Hamburguesa" y mostrar la lista completa por print.
    # 2.- Crear una lista nueva, agregar todos los nombres de los amigos que hayan elegido platos
    # principales del tipo "Ensalada" y mostrar la lista completa por print.
    # 3.- Crear una lista nueva, agregar todos los nombres de los amigos que hayan pedido bebidas
    # del tipo "Refresco" y mostrar la lista completa por print.
    # 4.- Crear una lista nueva, agregar todos los nombres de los amigos que hayan pedido bebidas
    # del tipo "Agua" y mostrar la lista completa por print.

    # 5.- Crear una lista nueva, agregar todos los nombres de los amigos que hayan realizado más
    # de 3 pedidos en total (platos principales + bebidas) y mostrar la lista completa por print.
    # 6.- Crear una lista nueva, agregar todos los nombres de los amigos que hayan realizado más
    # de 5 pedidos en total (platos principales + bebidas) y mostrar la lista completa por print.
    # 7.- Crear una lista nueva, agregar todos los nombres de los amigos que hayan realizado más
    # de 7 pedidos en total (platos principales + bebidas) y mostrar la lista completa por print.
    # 8.- Crear una lista nueva, agregar todos los nombres de los amigos que hayan realizado menos
    # de 3 pedidos en total (platos principales + bebidas) y mostrar la lista completa por print.
    # 9.- Crear una lista nueva, agregar todos los nombres de los amigos que hayan realizado menos
    # de 5 pedidos en total (platos principales + bebidas) y mostrar la lista completa por print.
    lista_de_nombres = ["Juan", "María", "Pedro", "Laura", "Carlos",
    "Ana", "Luis", "Elena", "Miguel", "Sofía"]
    lista_plato_principal = ["Pizza", "Hamburguesa", "Ensalada", "Pizza",
    "Hamburguesa", "Ensalada", "Pizza", "Hamburguesa", "Ensalada", "Pizza"]
    lista_cantidad_de_platos = [2, 1, 3, 2, 2, 4, 3, 1, 1, 3]
    lista_bebidas_elegidas = ["Refresco", "Agua", "Jugo", "Refresco","Agua", "Jugo", "Refresco", "Agua", "Jugo", "Refresco"]
    lista_cantidad_de_bebidas = [2, 1, 5, 3, 2, 5, 1, 2, 1, 3]
    
    pregunta = True
    while pregunta:
        # - Nombre del amigo,

        nombre = input('Nombre del amigo')
        while(nombre == None or not nombre.isalpha()):
            nombre = input('Nombre del amigo nuevamente')

        print(nombre)

        # - Plato principal elegido ("Pizza", "Hamburguesa", "Ensalada").
        platoprincipal = input('Plato principal elegido')
        while(platoprincipal != 'Pizza' and platoprincipal != 'Hamburguesa' and platoprincipal != 'Ensalada'):
            platoprincipal = input('Plato principal elegido')    

        print(platoprincipal)

        # - Cantidad de platos principales pedidos (debe ser al menos 1).

        cantidad_platos = input('Ingrese la cantidad de platos pedidos')
        while(not cantidad_platos.isdigit() or int(cantidad_platos) < 1):
            cantidad_platos = input('Ingrese la cantidad de platos pedidos')    

        print(cantidad_platos)
        # - Bebida elegida ("Refresco", "Agua", "Jugo").

        bebida_elegida = input('ingrese su Bebida')
        while(bebida_elegida != 'Refresco' and bebida_elegida != 'Agua' and bebida_elegida != 'Jugo'):
            bebida_elegida = input('ingrese nuevamente Bebida elegida')    

        print(bebida_elegida)

        # - Cantidad de bebidas pedidas (debe ser al menos 1).

        cantidad_bebidas = input('Ingrese la cantidad de bebidas pedidos')
        while(not cantidad_bebidas.isdigit() or int(cantidad_bebidas) < 1):
            cantidad_bebidas = input('Ingrese la cantidad de bebidas pedidos')  

        # El precio unitario de cada plato principal es de $800.
        precio_plato = 800
        # El precio unitario de cada bebida es de $200.
        precio_bebida = 200
        
        pregunta = question('Desea seguis agregando?')


    # A) El total gastado por el grupo (resultante del costo de los platos principales y las
    # bebidas), y la propina sugerida para el personal del restaurante (esta corresponde al
    # 10% del total gastado).
    len_platos = len(lista_cantidad_de_platos)
    len_bebidas = len(lista_cantidad_de_bebidas)
    iterator_jugos = 0
    len_amigos = len(lista_de_nombres)
    
    for i in range(len_platos):
        cantidad_gastada_platos = len_platos * precio_plato
        
        cantidad_gastada_bebidas = len_bebidas * precio_bebida

    print(cantidad_gastada_bebidas)
    
    #B) Promedio del dinero gastado en “Jugo”, sobre el grupo de amigos en general.
    for i in range(len_bebidas):
        if(lista_bebidas_elegidas[i] == 'Jugo'):
            iterator_jugos += precio_bebida
    accurate_jugos = iterator_jugos / len_bebidas
    print(accurate_jugos)
    #C) Los porcentajes de cada tipo de platos pedidos (teniendo en cuenta su cantidad).
    # Ejemplo: [30% pizza, 40% ensaladas, 30% hamburguesas
    
    iterator_pizza = 0
    iterator_ensalada = 0
    iterator_hamburguesa = 0
    list_platos = []
    for i in range(len_platos):
        
        match(lista_plato_principal[i]):
            case 'Pizza':
                iterator_pizza += 1
                list_platos.append(iterator_pizza)
            case 'Ensalada':
                iterator_ensalada += 1
                list_platos.append(iterator_ensalada)
            case _:
                iterator_hamburguesa += 1
                list_platos.append(iterator_hamburguesa)
        
        
    porcentaje_pizza = iterator_pizza / len(lista_plato_principal) * 100
    porcentaje_ensalada = iterator_ensalada / len(lista_plato_principal) * 100
    porcentaje_hamburguesa = iterator_hamburguesa / len(lista_plato_principal) * 100

    print(porcentaje_ensalada)
    print(porcentaje_pizza)
    print(porcentaje_hamburguesa)
    
    porcentaje = (iterator_hamburguesa / len_amigos) * 100
    print(f"Porcentaje de empleados que no votaron por APPLE y cumplen condiciones: {porcentaje:.2f}%")
    
    
    #D) Además, desean premiar al amigo que realizó la mayor CANTIDAD de pedidos en total
    # (platos principales + bebidas) con una entrada gratuita para otra atracción del parque
    # "Aventuras Extremas".
    
    for i in range(len_amigos):
        pass