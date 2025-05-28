#creando DICCIONARIO
paciente = {
    'nombre' : 'Carlos',
    'apellido' : 'Santana',
    'edad' : 50,
    'ciudad' : 'puerto montt',
    'comuna' : {'alerce'},
    'consultas' : [15, 20, 40],
    'diagnóstico' : ('resfrío'),
    'info extra' : {
        'tipo_de_sangre' : 'A+',
        'hemograma' : 'sin datos'
    }
}

#otra forma de declarar DICCIONARIO
medico = dict(
    nombre = 'Samir',
    apellido = 'Arana',
    edad = 20,
    especialidad = 'neurólogo'
)

#impresion de DICCIONARIOS
print(paciente)
print(medico)

#consultando un elemento a traves de la clave del diccionario
print(medico['nombre'])

#eliminando una clave del DICCIONARIO (metodo DEL)
del(paciente['nombre'])
print(paciente)
