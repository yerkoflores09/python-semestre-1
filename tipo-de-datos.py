#inicializando variables numericas
edad = 30
estatura = 1.80
peso = 80
complejo = 2 + 9j
complejo2 = complex(1, 4)

#impresion de numeros complejos
print(complejo)
print(complejo2)

#operacion aritmetica
imc = peso / (estatura ** 2)
print(f"su imc es: {imc}")

# formato de salida del resultado (utilizando F-STRINGS y :.2f)
print("su imc es: {:.2f}". format (imc))

# 04 - datos tipo strings (cadenas de texto)
carrera = "ingenieria civil en informatica"
asigantura = "programacion"
descripcion = '''Esta es una asignatura de primer semestre'''

#impresion de caracteres en una cadena de texto
print(carrera[0]) #imprime el primer caracter de la cadena
print(carrera[-2]) #imprime el ultimo caracter de la cadena

print("hola" * 4)
#print("hola" / 2)

#utilizando el intervalo de una cadena
print(asigantura[0:6])

#aplicando el metodo split (genera un arreglo de cadenas)
print(descripcion.split())

# arreglo numerico
v = [1, 2, 3, 4, 5]