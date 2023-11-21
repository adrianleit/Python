#8.	Solicitar un número ejemplo 30 y pedir 30 números por teclado contando los positivos y los negativos;
numero=int(input('Introduce un numero'))
positivos=0
negativos=0
for i in range(0,numero):
    numeroIntro=input('Introduce un numero')
    if numeroIntro > 0:
        positivos=positivos+1
    else:
        negativos=negativos+1
print('Positivos:',positivos)
print('Negativos:',negativos)