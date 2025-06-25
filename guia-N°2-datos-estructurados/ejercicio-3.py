#tienda de ropa deportiva
ventas = {
    'kakarotto': [250000, 300000, 350000, 350000, 100000],
    'vegetita': [90000, 400000, 100000, 150000, 350000],
    'songohanda': [350000, 450000, 100000, 70000, 400000]
}

sueldo = 529000

for nombre, dias in ventas.items():
    total_semana = sum(dias)
    promedio = total_semana / len(dias)

    if total_semana > 1500000:
        bono = sueldo * 0.20
    elif total_semana > 1000000:
        bono = sueldo * 0.10
    elif total_semana > 500000:
        bono = sueldo * 0.05
    else:
        bono = 0

    sueldo_total = sueldo + bono

# impriendo el reporte
    print(f'Vendedor: {nombre}') #estos print debe ir dentro del for para que imprima a todos los vendedores
    print(f'Ventas semanales: ${total_semana}')
    print(f'Promedio diario: ${promedio}')
    print(f'Bono: ${bono}')
    print(f'Sueldo a pagar: ${sueldo_total}\n')
