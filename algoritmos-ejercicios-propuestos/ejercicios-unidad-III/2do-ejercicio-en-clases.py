# solicitar cantidad de estudiantes
while True:
    try:
        n_estudiantes = int(input("Ingresa la cantidad de estudiantes: "))
        if n_estudiantes < 1:
            print("Error: Debe ser un número entero positivo.")
        else:
            break
    except ValueError:
        print("Error: Ingresa un número entero válido.")

# Paso 2: Registrar datos
asignatura = input("Ingresa el nombre de la asignatura: ")
estudiantes = []

for i in range(n_estudiantes):
    print(f"\nregistro del estudiante #{i+1}:")
    nombre = input("nombre del estudiante: ")
    
    # Leer 3 notas (validando rango 0.0-7.0)
    notas = []
    for j in range(3):
        while True:
            try:
                nota = float(input(f"ingresa la nota {j+1} de {nombre}: "))
                if nota < 0.0 or nota > 7.0:
                    print("error: La nota debe estar entre 0.0 y 7.0")
                else:
                    notas.append(nota)
                    break
            except ValueError:
                print("error: Ingrese un número válido.")
    
    promedio = sum(notas) / 3.0
    estudiantes.append((nombre, notas, promedio))

# Paso 3: Encontrar máximos y mínimos
est_max = estudiantes[0]
est_min = estudiantes[0]
for est in estudiantes:
    if est[2] > est_max[2]:
        est_max = est
    if est[2] < est_min[2]:
        est_min = est

# Paso 4: Mostrar resultados
print("\n" + "="*50)
print(f"INFORME DE NOTAS - {asignatura.upper()}")
print("="*50)

for nombre, notas, promedio in estudiantes:
    # Determinar categoría
    if promedio < 4.0:
        categoria = "Bajo"
    elif promedio <= 6.0:
        categoria = "Regular"
    else:
        categoria = "Alto"
    
    # Verificar beca
    beca = "(Becado)" if promedio > 5.0 else ""
    
    print(f"{nombre}:")
    print(f"  Notas: {notas}")
    print(f"  Promedio: {promedio:.2f} - {categoria} {beca}")

# Paso 5: Mostrar estudiantes destacados y con dificultades
print("\n" + "="*50)
print(f"ESTUDIANTE DESTACADO: {est_max[0]} - Promedio: {est_max[2]:.2f}")
print(f"ESTUDIANTE CON DIFICULTADES: {est_min[0]} - Promedio: {est_min[2]:.2f}")
print("="*50)

# Paso 6: Listar reprobados (promedio < 4.0)
reprobados = []
for est in estudiantes:
    if est[2] < 4.0:
        reprobados.append(est)

print("\nESTUDIANTES REPROBADOS (promedio < 4.0):")
if reprobados:
    for nombre, _, promedio in reprobados:
        print(f"- {nombre}: {promedio:.2f}")
else:
    print("¡Ningún estudiante reprobado!")