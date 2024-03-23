# Solicitar al usuario que ingrese 10 números y almacenarlos en una lista
numeros = []
for i in range(10):
    numero = float(input(f"Ingrese el número {i + 1}: "))
    numeros.append(numero)

# Calcular el promedio de la lista
suma_total = sum(numeros)
promedio = suma_total / len(numeros)

# Mostrar el resultado del promedio al usuario
print(f"El promedio de los números ingresados es: {promedio}")