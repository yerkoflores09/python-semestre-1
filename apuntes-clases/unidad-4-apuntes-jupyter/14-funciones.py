def saludo(nombre):
    print(f'hola, mi nombre es + {nombre}')

saludo('yerko')

#la llamada a la funcion con argumentos posicionales 
def suma(a, b):
    return a + b

#la llamada a la funcion con argumentos posicionales: 2 + a, 3 + b
resultado = suma(2, 3) #el orden si importa 
print(resultado)

#argumentos con valor por defecto
#definición de la función "resta" con parametros por defecto (b = 5)
def resta(a, b=5):
    return a - b

#caso 1: usando solo el argumento obligatorio 'a' (b tomará su valor por defecto: 5)
resultado1 = resta(6) #equivalente a suma (6, 5)
print('resultado 1 (b por defecto):', resultado1) #6 - 5 = 1

#caso 2: pasando ambos argumentos (ignora el valor por defecto de 'b')
resultado2 = resta(4, 4) #a=4, b=4
print('resultado 2 (b personalizado):', resultado2) #4-4 = 0

#argumentos por nombre (KEYWORDS)
def calcular_potencia(base, exponente):
    return base ** exponente

#llamada con argumentos por nombre (el orden no importa)
resultado = calcular_potencia(exponente=3, base=2)
print(resultado)