#strings 
productos = ['smartphone', 'laptop', 'tablet', 'smartwatch']
precios = [300, 800, 150, 200]
stock = {
    'smartphone': 20,
    'laptop': 8,
    'tablet': 10,
    'smartwatch': 5
}

#precio minimo y maximo
max_precio = max(precios)
min_precio = min(precios)


#producto más caro y más barato
prod_max = productos[precios.index(max_precio)]
prod_min = productos[precios.index(min_precio)]

print(f'el articulo más caro es: {prod_max} con un valor de {max_precio}')
print(f'el articulo más caro es: {prod_min} con un valor de {min_precio}\n\n')

#categorias
for prod, precio in zip(productos, precios):
    if precio < 200:
        categoria = 'producto económico'
    elif precio <= 200 and precio <= 500:
        categoria = 'producto estandar'
    else:
        categoria = 'producto premium'
    print(f'{prod}: ${precio} -> {categoria}\n')

#articulos con bajo stock
for prod, cantidad in stock.items():
    if cantidad < 10:
        print(f'{prod}: {cantidad} unidades')
