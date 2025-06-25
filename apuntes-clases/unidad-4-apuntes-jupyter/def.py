def saludo(nombre):
    print(f'hola, mi nombre es + {nombre}')

saludo('yerko')
#la llamada a la funcion con argumentos posicionales 

def suma(a, b):
    return a + b

#la llamada a la funcion con argumentos posicionales: 2 + a, 3 + b
resultado = suma(2, 3) #el orden si importa 
print(resultado)
