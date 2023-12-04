'''Dado un párrafo, buscar las comas comprobar que hay un blanco detrás, 
y ponerlo comprobar que después de un punto, se escribe en mayúsculas.
Primero ponemos las comas y luego comprobamos los puntos.cle
'''

cadena_1 = input("Introduce una cadena: ")
nueva_cadena = ""

'''Para caracter de la cadena, si cumple que la cadena no esta en el final, que el caracter es una coma
y que el siguiente caracter despues de la coma es distinto de la coma, entoces se mete un espacio
sino se mete el caracter a la nueva cadena'''
for i in range(len(cadena_1)):
    caracter = cadena_1[i]

    if caracter == ',' and i + 1 < len(cadena_1) and cadena_1[i + 1] != ' ':
        nueva_cadena += caracter + ' '
    else:
        nueva_cadena += caracter

'''Convertir la letra siguiente a mayúsculas después de un punto'''

resultado_final = ""
despues_de_punto = False

'''Comprueba por cada caracter en la cadena si despues_de_punto=true y si el caracter es minuscula'''
for char in nueva_cadena:
    if despues_de_punto and char.islower():
        resultado_final += ' ' + char.upper()
    else:
        resultado_final += char
    '''Comprueba si el caracter es un punto y si es asi, boolean = true'''
    despues_de_punto = (char == '.')

print(resultado_final)