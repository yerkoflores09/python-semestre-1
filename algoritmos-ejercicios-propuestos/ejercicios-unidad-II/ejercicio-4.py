# ingresar nombre del producto y precio unitario
nombre_producto = input("ingresa el nombre del producto: ")
precio_unitario = float(input("ingresa el precio unitario: "))

# ingresar cantidad en stock
cantidad = int(input("ingresa la cantidad en stock: "))

# valor total
valor_total = precio_unitario * cantidad

# variable booleana umbral
umbral = valor_total > 100000

# impresion de todos los datos
print(f"Producto: {nombre_producto}, Cantidad: {cantidad}, Valor Total: ${valor_total:.2f}, Umbral: {umbral}")