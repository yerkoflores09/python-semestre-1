#lista compuesta de datos
lista1 = ['yerko', 24, True]

#lista vacia
frutas = []

#lista solo de numeros
n = [1,2,3,4,5]

#lista de solo STRINGS
ramos = ['programacion', 'quimica', 'matematica']
ramos = list(['programacion', 'quimica', 'matematica'])

#imprime la posicion del del primer elemento de la lista (no el caracter)
print(ramos[0])

#funcion COUNT (cuenta la cantidad de concurrencias de un elemento)
print(ramos.count('programacion'))

#creando e iniciando una TUPLA
estudiantes = ('samir', 'matias', 'hector',)

#funcion index en TUPLAS
print(estudiantes.index('hector'))

#creando SETS
colores = {'azul', 'rojo', 'azul', 'verde', 34}
print(colores)

#funcion APPEND
ramos.append('introduccion a la matemática')
print(ramos)

#modificar elementos de la lista
ramos[1] = 'comunicacion' #estoy pasando la posicion del elemento a modificar
print(ramos)

#otra forma de insertar un elemento a la lista (INSERT)
ramos.insert(7, 'algebra')
print(ramos)

#eliminar el ultimo elemento de la lista
ramos.pop()
print(ramos)

#ordenando los elementos de una lista de forma descendente a ascendente
ramos.sort()
print(ramos)

#ordenando elementos de una lista segun su cantidad de carácteres
ramos.sort(key=len) #key es una propiedad del metodo SORT y se pasa un valor que es el metodo LEN
print(ramos)

#ocupando el metodo extend (extendiendo una lista a partir de otra)
ramitos = ['cálculo', 'autómatas']
ramos.extend(ramitos)
print(ramos)
