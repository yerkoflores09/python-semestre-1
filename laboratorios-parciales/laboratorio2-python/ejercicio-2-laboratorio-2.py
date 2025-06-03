#Integrantes: Yerko Flores Barrientos
print('aplicación para detectar el plagio con Inteligencia Artificial en papers científicos.')

#1. Ingresar por terminal un resumen en formato string
resumen = input('Ingresa el resumen del texto, no debe tener más de 50 carácteres: ')[:50]

#2. Variable booleana
print(f'¿el resumen del texto contiene mas de 50 carácteres?: ', bool(resumen))

#3. Mostrando la informacion
print(f'''la longitud total del informe es: {resumen.count('')}
El resumen del texto en mayúsculas: {resumen.upper()}
El resumen del texto en minúsculas: {resumen.lower()}
El numero de veces que aparece la vocal "e": {resumen.count('e')}
Los primeros 15 carácteres del texto son: {resumen.format(15)}
Los últimos 15 carácteres del texto son: 
Y por ultimo el resumen del texto: {resumen.split()}
''')