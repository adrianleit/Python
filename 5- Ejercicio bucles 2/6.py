#Realizar una algoritmo que muestre la tabla de multiplicar de un número solicitado por teclado
i=1
tablaMultiplicar = int(input('Introduzca un numero: '))
while i<11:
    print(tablaMultiplicar,'x',i,'=',tablaMultiplicar*i)
    i+=1