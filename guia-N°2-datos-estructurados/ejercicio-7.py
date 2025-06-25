#factorial de un número
numero = int(input('ingresa un número entero: '))

if numero < 0:
    print('no se puede para numeros negativos')
else:
    factorial = 1
    for i in range(1, numero + 1):
        factorial = factorial * i

    print(f'{numero}! = {factorial}')
