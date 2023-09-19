# La división de higiene está trabajando en un control de stock para productos
# sanitarios. Debemos realizar la carga de 5 (cinco) productos de prevención de
# contagio, de cada una debe obtener los siguientes datos:
# 1. El tipo (validar "barbijo", "jabón" o "alcohol")
# 2. El precio: (validar entre 100 y 300)
# 3. La cantidad de unidades ( no puede ser 0 ni negativo y no debe superar las
# 1000 unidades)
# 4. La marca y el Fabricante.
# Se debe informar lo siguient e:
# A. Del más caro de los barbijos, la cantidad de unidades y el fabricante.
# B. Del ítem con más unidades, el fabricante.
# C. Cuántas unidades de jabones hay en total.


list_producto = []
list_prices = []
list_amount = []
list_brands = []
list_maker = []
accumualator_jabon = 0
cantidad_barbijo = None
fabricante_barbijo = None
barbijo_mas_caro = None
item_mayor = None
item_nombre = None
item_fabricante = None


for i in range(5):
    product = input('Ingrese el tipo de stock')
    while(product != 'Barbijo' and product != 'Jabon' and product != 'Alcohol'):
        product = input('Reingrese el tipo de stock')
    list_producto.append(product)
    
    price = input('Ingrese el precio')
    while(int(price) < 100 or int(price) > 300):
        price = input('Reingrese el precio')
    list_prices.append(price)
    
    amount = input('Ingrese la cantidad que desea')
    while(not amount.isdigit() or int(amount) < 1 or int(amount) > 1000):
        amount = input('Cantidad no valida, maximo 1000')
    list_amount.append(amount)
    
    brand = input('Ingrese la marca')
    while(not brand.isalpha()):
        brand = input('Reingrese la marca')
    list_brands.append(brand)
    
    
    maker = input('Ingrese el fabricante')
    while(not maker.isalpha()):
        maker = input('Reingrese la fabricante')
    list_maker.append(maker)
    
    # A. Del más caro de los barbijos, la cantidad de unidades y el fabricante.
    
    if(list_producto[i] == 'Barbijo'):
        if(barbijo_mas_caro == None or barbijo_mas_caro < list_prices[i]):
            barbijo_mas_caro = list_prices[i]
            cantidad_barbijo = list_amount[i]
            fabricante_barbijo = list_maker[i]

    # B. Del ítem con más unidades, el fabricante.
    
    if(item_mayor == None or item_mayor < list_amount[i]):
        item_mayor = list_amount[i]
        item_nombre = list_producto[i]
        item_fabricante = list_maker[i]
    
    # C. Cuántas unidades de jabones hay en total.
    
    
    if(list_producto[i] == 'Jabon'):
        accumualator_jabon += int(list_amount[i])

print(f'EL barbijo mas caro es {barbijo_mas_caro} con cantidad {cantidad_barbijo} y fabricante {fabricante_barbijo}')
print(f'EL item con mas u {item_mayor} es el  {item_nombre} y fabricante {item_fabricante}')
print(f'La cantidad de jabones en total es {accumualator_jabon}')