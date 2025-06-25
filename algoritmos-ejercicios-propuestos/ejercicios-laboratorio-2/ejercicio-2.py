#algoritmo de operaciones mixtas
entero = int(input('ingresa un numero entero: '))
flotante = float(input('ingresa un numero decimal: '))
complejo = complex(input('ingresa un numero complejo: '))

potencia_compleja = (complejo ** entero)
suma_mixta = (complejo + flotante)
producto_mixto = (complejo * entero)
modulo_potencia = abs(potencia_compleja)

print(f'resultados de las operaciones:')
print(f'potencia compleja: {potencia_compleja}')
print(f'suma mixta: {suma_mixta}')
print(f'producto mixto: {producto_mixto}')
print(f'modulo de potencia: {round(modulo_potencia, 3)}')