'''Realizar un algoritmo que pida  10 números  El programa debe 
informar de cuantos números introducidos son mayores que 0, menores que 0 e iguales a 0.'''
i=0
mayor=0
menor=0
igual=0
while i<10:
    numero=int(input('Introduce un numero: '))
    if numero == 0:
        igual+=1
    else:
        if numero>0:
            mayor+=1
        else:
            menor+=1
    i+=1
print('Hay', mayor, 'numeros mayores que 0')
print('Hay', menor, 'numeros menores que 0')
print('Hay', igual, 'numeros 0')
