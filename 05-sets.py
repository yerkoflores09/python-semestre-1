#creando SETS *{es con llaves}*
colores = {'azul', 'rojo', 'azul', 'verde'}
colorcitos = {'azul', 'naranjo'}

#imprimiendo el set de colores
print(colores)

#agregando metodo ADD
colores.add('blanco')
print(colores)

#eliminando elemento del set
colores.discard('blanco')
print(colores)

#aplicando el metodo DIFERENCE
diferencia = colores.difference(colorcitos)
print(diferencia)
