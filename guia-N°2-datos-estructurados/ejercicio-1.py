#guia N°2 python, grupo 7, yerko flores barrientos, joaquin mansilla aillapan
# Contar las repeticiones de una palabra en una tupla
#leer parrafo
try:
    parrafo = input('ingresa el parrafo para ejecutar la funcion:\n')
    if parrafo == '':
        raise ValueError('el parrafo no puede estar vacío')

#separar palabras y guardar en listas
    palabras = parrafo.split()

#solicitar al usuario palabra a buscar
    palabra_usuario = input('escribe una palabra para descubrir cuantas veces aparece: ')
    contar_palabras = parrafo.count(palabra_usuario)

#imprimiendo las veces que aparece dicha palabra
    print(f'la palabra: {palabra_usuario} aparece un total de: {contar_palabras}')
except ValueError:
    print('ERROR')