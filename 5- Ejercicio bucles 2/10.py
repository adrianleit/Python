'''Escribe un programa que, dados dos números, uno real (base) y un entero positivo (exponente), 
saque por pantalla el resultado de la potencia. No se puede utilizar el operador de potencia'''
base=int(input('Escriba la base de la potencia: '))
exponente=int(input('Escribe el exponente de la potencia: '))
i=0
total=1
while i<exponente:
    total=total*base
    i+=1
print("Resultado", total)