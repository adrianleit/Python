'''Algoritmo que pida caracteres 20 e imprima 'VOCAL' si son vocales y 
'NO VOCAL' en caso contrario, el programa termina cuando se introduce un espacio.'''
contador=0
vocal="aeiouAEIOU"
while contador < 20:
    caracter =input('Introduce un caracter: ')
    if caracter in vocal:
        print('Es una vocal')
    else:
        print('No es una vocal')
    contador+=1