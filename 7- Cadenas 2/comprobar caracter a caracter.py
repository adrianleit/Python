#Pide una cadena y un caracter por teclado y muestra cuantas veces aparece el caracter en la cadena
cadena=input('Introduce una cadena: ')
caracter=input('Introduce un caracter: ')
i=0
while i<len(cadena):
    if cadena[i]==caracter:
        print(cadena[i],'esta en la posicion',i )
    i+=1