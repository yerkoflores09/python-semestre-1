'''
1. Pedir por consola los precios unitarios (float) y las cantidades (int) de cuatro productos:

a. Martillo
b. Clavos
c. Serrucho
d. Tornillos

2. Calcular y mostrar los subtotales para cada producto y redondearlos a 2 decimales.

3. Imprimir los siguientes resultados, en este orden:

a. Subtotal Martillo | Subtotal Clavos | Subtotal Serrucho | Subtotal Tornillos
b. Suma total de los cuatro subtotales.
c. Valor máximo entre los cuatro subtotales.
d. Valor mínimo entre los cuatro subtotales.
e. Promedio del precio unitario de las herramientas, redondeado a 2 decimales
f. Obtener el IVA (19%) del total de las herramientas ingresadas al sistema.
'''

# 1. Ingresa el precio de los productos, deben ser números flotantes

# a. Martillo
precio_martillo = float(input("Ingrese precio del martillo: "))

# b. Clavos
precio_clavos = float(input("Ingrese precio de los clavos: "))

# c. Serrucho
precio_serrucho = float(input("Ingrese precio del serrucho: "))

# d. Tornillos
precio_tornillos = float(input("Ingrese precio de los tornillos: "))


# Luego ingresa la cantidad de productos, deben ser enteros

# a. Martillo
cantidad_de_martillos = int(input("Ingrese cantidad de martillos: "))

# b. Clavos
cantidad_de_clavos = int(input("Ingrese cantidad de clavos: "))

# c. Serrucho
cantidad_de_serruchos = int(input("Ingrese cantidad de serruchos: "))

# d. Tornillos
cantidad_de_tornillos = int(input("Ingrse cantidad de tornillos: "))

# 2. Calcula los subtotales de cada producto
subtotal_martillo = (precio_martillo * cantidad_de_martillos)
subtotal_clavos = (precio_clavos * cantidad_de_clavos)
subtotal_serrucho = (precio_serrucho * cantidad_de_serruchos)
subtotal_tornillos = (precio_tornillos * cantidad_de_tornillos)

# 3. Ahora imprime y redondea los subtotales a 2 decimales de cada producto 

# a. Luego ponlos en el siguiente orden:

# Primero el subtotal del martillo
print(round(subtotal_martillo,2))

# luego de los clavos
print(round(subtotal_clavos,2))

# despues con el del serrucho 
print(round(subtotal_serrucho,2))

# y luego el de los tornillos
print(round(subtotal_tornillos,2))

# b. Despues suma los cuatro subtotales
suma_total = (subtotal_martillo + subtotal_clavos + subtotal_serrucho + subtotal_tornillos)
print(suma_total)

# c. Ahora pon el valor maximo de los cuatro subtotales
print(max(subtotal_martillo))
print(max(subtotal_clavos))
print(max(subtotal_serrucho))
print(max(subtotal_tornillos))

# d. Despues el valor minimo
print(min(subtotal_martillo))
print(min(subtotal_clavos))
print(min(subtotal_serrucho))
print(min(subtotal_tornillos))

# e. Continua poniendo el promedio del precio unitario de las herramientas, redondeado a 2 decimales
print(round(suma_total,2))

# f. Por ultimo, obten el IVA (%19) del total de las herramientas
IVA_Martillo = (subtotal_clavos)


