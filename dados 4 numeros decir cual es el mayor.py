#dados 20 numeros decir cual es el mayor
# Crear una lista de 20 números (reemplaza estos números por los tuyos)
numeros = [5, 10, 3, 8, 15, 12, 7, 20, 25, 18, 11, 30, 21, 9, 13, 16, 17, 4, 1, 6]

# Inicializar una variable para almacenar el número más grande
numero_mas_grande = numeros[0]

# Recorrer la lista para encontrar el número más grande
for numero in numeros:
    if numero > numero_mas_grande:
        numero_mas_grande = numero

# Imprimir el número más grande
print("El número más grande es:", numero_mas_grande)
