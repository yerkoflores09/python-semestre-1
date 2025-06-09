#apuntes del ppt
edad = 19

if edad > 18: #siempre van dos puntos
    print('eres mayor de edad')
else :
    print('eres menor de edad')

#elif 3ra opcion
edad1 = 66

if edad1 > 18 and edad1 < 65:
    print('eres mayor de edad')
elif edad1 > 65:
    print('eres un adulto mayor')
else:
    print('eres menor de edad')

#una sola linea
edad2 = 17

print('usted puede votar' if edad2 >= 18 else 'usted no puede votar')

#guia de Condicionales
#añadiendo colorama al codigo
from colorama import init, Fore
init()

#condicional IF
print(Fore.CYAN + 'utilizando IF y ELSE')

licencia = False
edad3 = 19
automovil = False

print(Fore.YELLOW + 'utilizando 3er condicional IF')
if edad3 >= 18:
    print('')