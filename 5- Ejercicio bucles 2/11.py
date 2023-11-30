'''Algoritmo que muestre la tabla de multiplicar de los números 1,2,3,4 y 5.'''
i = 1
while i <= 5:
    print("Tabla del", i, ":")
    numero = 0

    while numero <=10:
        resultado = i * numero
        print(f"{i} x {numero} = {resultado}")
        numero = numero + 1

    print("--------------")
    i = i + 1