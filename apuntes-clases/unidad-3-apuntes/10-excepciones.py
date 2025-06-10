entrada = input('ingrese un valor entero: ') #valor ingresado es un str

try:
    numero = int(entrada)
    print(f'numero ingresado: {numero}')
except ValueError:
    print('error de valor: el valor ingrasado no es entero')
except Exception as e: #errores genericos e inesperados
    print(f'error inesperado: {e}')
else:
    print('conversión fue exitosa!')
finally: #acción de limpieza: cerrar el archivo si fue abierto
    print('finalización del bloque')
