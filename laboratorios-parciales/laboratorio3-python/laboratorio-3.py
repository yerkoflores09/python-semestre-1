#creando diccionario
codigo_postal = {
    5700000 : {
        'ciudad': 'castro',
        'temperatura': 11.8,
        'precipitación': 2000
    },
    5770000 : {
        'ciudad': 'chonchi',
        'temperatura': 8.3,
        'precipitación': 2800
    },
    5790000 : {
        'ciudad': 'quellón',
        'temperatura': 10.2,
        'precipitación': 2950
    }
}
print(codigo_postal)

#Agregando nueva clave a cada subdiccionario

try:
    codigo_postal[570000].items = ['clima'][5700000]['temperatura']
    if 10 <= 'clima' <= 15:
        print('la temperatura es templada')
    else:
        print('ola k ase')
except:
    codigo_postal[5700000]['temperatura'] = 'desconocida'

print(codigo_postal)

#Agregar al sub-diccionario de Castro una nueva clave "Meses Más Lluviosos"
clima_chiloe = ['meses mas lluviosos']


#Actualizar el valor de "Ciudad" para la ciudad de Chonchi
codigo_postal[5770000].keys['chonchi'] = ['ciudad de los tres pisos']
print(codigo_postal)

#creando una lista 
lluvias = list(codigo_postal)
print(lluvias)

#print de diccionario completo
print(codigo_postal)

#lista de tuplas
tuple(codigo_postal)
