'''Escribir por pantalla cada carácter de una cadena introducida por teclado.for
Y contar el número de caracteres'''
cadena=input("Introduce una cadena: ")
numero = 0
for caracter in cadena:
    print(caracter)
    numero+=1
print(f"El numero de caracteres es {numero}")
