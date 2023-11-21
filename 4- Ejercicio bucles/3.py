#3.	Mostrar la tabla de multiplicar de un número que se introduce por teclado
tablaMultiplicar= int(input('Introduce la tabla de multiplicar que quieres: '))
i=1
while i<=10:
    print(tablaMultiplicar,'x',i,'=', tablaMultiplicar*i)
    i+=1