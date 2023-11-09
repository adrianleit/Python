#Algoritmo que pida dos números e indique si el primero es mayor que el segundo.
numero1=input("Introduzca un numero ")
numero2=input("Introduzca otro numero ")
if (numero1==numero2):
    print("Ambos numeros son iguales",numero1 )
else:
    if(numero1>numero2):
        print(numero1, "es mayor que", numero2)
    else:
        print(numero2, "es mayor que", numero1)
