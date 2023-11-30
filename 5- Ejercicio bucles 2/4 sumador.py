#Realizar un algoritmo del 1 al 200 y muestre la suma total de los pares
i=1
pares=0
while i<201:
    if i % 2 == 0:
        pares+=i
    i=i+1
print('La suma total de los 200 primeros pares:', pares)
