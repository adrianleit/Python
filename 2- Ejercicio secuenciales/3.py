#Dados los catetos de un triángulo rectángulo, calcular su hipotenusa..
import math
cateto = int(input("Dime cuanto miden los catetos "))
hipotenusa = math.sqrt((cateto**2) + (cateto**2))
print("La hipotenusa mide ", hipotenusa)
