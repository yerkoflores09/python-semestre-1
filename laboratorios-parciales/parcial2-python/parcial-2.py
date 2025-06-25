#diccionario de la veterinaria
gatitos = {
    101: {
        'nombre': 'luna',
        'peso': 1.2,
        'edad': 3,
        'tamaño': 30
    },
    102: {
        'nombre': 'michi',
        'peso': 0.8,
        'edad': 2,
        'tamaño': 25
    },
    103: {
        'nombre': 'pepito',
        'peso': 2.5,
        'edad': 5,
        'tamaño': 35
    }
}
print(gatitos)

#añadir nueva clave
clasificacion_peso = gatitos[101]['peso']
if clasificacion_peso:
    gatitos[101]['peso'] < 1 
    print('bajo peso')
elif gatitos[101]['peso']:
    gatitos[101] >= 1 and gatitos[101] <= 4
    print('peso normal')
elif  gatitos[101]['peso']:
    gatitos[101] >= 4
    print('sobre peso')

clasificacion_peso = gatitos[102]['peso']
if clasificacion_peso:
    gatitos[102]['peso'] < 1 
    print('bajo peso')
elif gatitos[102]['peso']:
    gatitos[102] >= 1 and gatitos[102] <= 4
    print('peso normal')
elif  gatitos[102]['peso']:
    gatitos[102] >= 4
    print('sobre peso')

clasificacion_peso = gatitos[103]['peso']
if clasificacion_peso:
    gatitos[103]['peso'] < 1 
    print('bajo peso')
elif gatitos[103]['peso']:
    gatitos[103] >= 1 and gatitos[103] <= 4
    print('peso normal')
elif  gatitos[103]['peso']:
    gatitos[103] >= 4
    print('sobre peso')

print(gatitos)

#creando otro bucle
try:
    gatitos[101]['categoria-etaria']


except:
    print('edad desconocida')


#lista de tuplas
lista_tuplas = list(gatitos[101], gatitos[101]['peso'])
print(lista_tuplas.append())

#datos de nuevos gatitos
