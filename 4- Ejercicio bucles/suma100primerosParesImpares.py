#Sumar los 100 primeros numeros
i=0
totalpar=0
totalimpar=0
for i in range(0,101):
    if i%2==1:
        totalimpar=totalimpar+i
    else:
        totalpar=totalpar+i
print("El total de pares es:",totalpar)
print("El total de impares es:",totalimpar)