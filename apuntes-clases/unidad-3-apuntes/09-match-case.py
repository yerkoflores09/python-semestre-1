print('menu')
print('1. hamburguesa')
print('1. pizza')
print('1. tocomple')

opcion = input('porfavor elije una opcion (1-3): ')

match opcion:
    case '1':
        print('has elejido una hamburguesa. Precio $5000')
    case '2':
        print('has elejido una pipshas. Precio $7500')
    case '3':
        print('has elejido un tocomple. Precio $2500')

#ejemplo: estacion ssegun mes
mes = 4 

match mes:
    case 12 | 1 | 2:
        print('verano')
    case 3 | 4 | 5:
        print('otoño')
    case 6 | 7 | 8:
        print('invierno')
    case 9 | 10 | 11:
        print('primavera')
    case _:
        print('mes invalido')

#patrones compuestos
x = [1,2,3]

match x:
    case [a,b,c]: #desagrupando valores de la lista x
        print(f'elementos de la lista x: {a}, {b}, {c}')

datos = {
    'nombre': 'yerko',
    'edad': 20
    }
match datos:
    case {'nombre': n, 'edad': e}:
        print(f'nombre: {n}, Edad: {e}')