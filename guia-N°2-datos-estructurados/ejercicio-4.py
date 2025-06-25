#algoritmo de nicomaco de gerasa
n = int(input('ingresa hasta que número deseas ver esta propiedad: '))

primer_impar = 1

for num in range(1, n + 1):
    suma_impares = 0
    inicio = primer_impar

    for i in range(num):
        suma_impares = suma_impares + primer_impar
        primer_impar = primer_impar + 2 #este es el siguiente numero impar

    print(f'{num}^3 = sumando {num} impares empazando en {inicio}:')
    print(" ", " + ".join(str(inicio + 2 * j) for j in range(num)), f"= {suma_impares}")
    print(f'{num}^3 = {num ** 3}\n')
