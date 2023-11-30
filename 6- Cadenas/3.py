'''Realizar un programa que comprueba si una cadena leída por teclado comienza 
por una subcadena introducida por teclado ejercicio 2'''
cadena=input("Introduce una cadena: ")
numero = 0
for caracter in cadena:
    print(caracter)
    numero+=1
print(f"El numero de caracteres es {numero}")
print(cadena.lower().startswith("h"))