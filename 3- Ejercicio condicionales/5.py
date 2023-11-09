#Crea un programa que pida al usuario dos números y muestre su división 
## si el segundo no es cero, o un mensaje de aviso en caso contrario 
numero1=int(input("Introduzca un numero "))
numero2=int(input("Introduzca otro numero "))
if (numero2==0):
    print("No se puede dividir entre ", numero2 )
else:
    print(numero1/numero2)