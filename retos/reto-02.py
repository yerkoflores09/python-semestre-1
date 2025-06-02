#definir inventario
inventario = {
    'manzana' : ('1000', '2000', '3000'),
    'platano' : ('2000', '2000', '4000'),
    'frutilla' : ('2500', '3000', '3500'),
}

#precios unicos
precios_platano = set(inventario['platano'])

#lista tipos_frutas
tipos_frutas = list(inventario.keys())

#calculo del promedio
promedio_platano = sum(precios_platano) / len(precios_platano)

print(inventario)

print(tipos_frutas)
print(promedio_platano)
