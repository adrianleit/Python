#Un alumno desea saber cuál será su calificación final en la materia de Algoritmos. 
#Dicha calificación se compone de los siguientes porcentajes:
#•	55% del promedio de sus tres calificaciones parciales.
#•	30% de la calificación del examen final.
#•	15% de la calificación de un trabajo final.

notaTrimestre1 = int(input("Introduzca la calificacion del trimestre 1 "))
notaTrimestre2 = int(input("Introduzca la calificacion del trimestre 2 "))
notaTrimestre3 = int(input("Introduzca la calificacion del trimestre 3 "))
notaExamenFinal = int(input("Introduzca la calificacion del examen final "))
notaTrabajoFinal = int(input("Introduzca la calificacion del trabajo final "))

notaFinal = ((notaTrimestre1+notaTrimestre2+notaTrimestre3)/3*0.55) + notaExamenFinal*0.30 + notaTrabajoFinal*0.15
print("La nota final es:", notaFinal)