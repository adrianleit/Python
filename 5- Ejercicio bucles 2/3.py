#Realizar un algoritmo del 1 al 200 y muestre el número de pares e impares
i=1
pares=0
impares=0
while i<201:
    if i % 2 == 0:
        pares+=1
    else:
        impares+=1
    i=i+1
print('Pares:', pares)
print('Impares', impares)