#Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a cuantas horas y minutos corresponde.
#Por ejemplo: 1000 minutos son 16 horas y 40 minutos.
import math
minutos = int(input("Dime el numero de minutos "))
horas = math.trunc(minutos/60)
minutosHoras = minutos%60
print(minutos,"minutos son",horas,"horas y",minutosHoras,"minutos")