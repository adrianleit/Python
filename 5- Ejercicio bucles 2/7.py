'''Crea una aplicación que permita adivinar un número. 
La aplicación genera un número aleatorio del 1 al 100. 
A continuación, va pidiendo números y va respondiendo si el 
número a adivinar es mayor o menor que el introducido, 
además de los intentos que te quedan (tienes 10 intentos para acertarlo). 
El programa termina cuando se acierta el número 
(además te dice en cuantos intentos lo has acertado), 
si se llega al límite de intentos te muestra el número que había generado.'''

import random
aleatorio=random.randint(1,100)
intentos=10
i=0
while i<intentos:
    numero=int(input('Introduce un numero: '))
    if aleatorio == numero:
        print('Lo has adivinado en',i,'intentos, el numero era', aleatorio)
        break
    else:
        if aleatorio>numero:
           print('El numero es mas grande') 
        else:
            print('El numero es mas pequeño')
    i+=1
    if i == intentos:
        print('No te quedan mas intentos, el numero era:', aleatorio)
