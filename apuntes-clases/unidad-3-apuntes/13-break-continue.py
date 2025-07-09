while True:
    parametro = input('>')
    if parametro == 'salir': #doble igual, estamos asignando
        break
    else:
        print(parametro)

# continue
n = 0
while n <= 50:
    n += 1
    if n == 40:
        continue
    print(n)