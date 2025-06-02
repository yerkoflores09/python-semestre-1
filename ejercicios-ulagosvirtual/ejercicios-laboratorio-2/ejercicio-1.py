# coversor de Celsius a Fahrenheit y a kelvin
celsius = float(input("Introduce la temperatura en grados Celsius: "))

fahrenheit = (celsius * 9/5) + 32
kelvin = celsius + 273.15

print(f"La temperatura ingresada fue: {round(celsius, 2)} °C")
print(f"La temperatura en Fahrenheit es: {round(fahrenheit, 2)} °F")
print(f"La temperatura en Kelvin es: {round(kelvin, 2)} °K")