mensaje_original = input('Introduce una cadena: ')

 # Lista de vocales a buscar
vocales = ['a', 'e', 'i','o','u']

for letra in range(len(mensaje_original)):
    if mensaje_original[letra].lower() in vocales:
        print('La letra es: ',mensaje_original[letra], 'posicion: ', letra+1)