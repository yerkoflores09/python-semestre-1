#calculadora
suma = 0
termino_impar = 500
termino_par = 456
indice = 1 #distingue si es par o impar

while True:
    if indice % 2 == 1:
        termino = termino_impar
        if termino > 800:
            break
        suma = suma + termino
        termino_impar = termino_impar + 10
    else:
        termino = termino_par
        suma = suma + termino_par
        termino_par = termino_par - 2

    indice = indice + 1

print('la sumatoria da un total de: ', suma)
