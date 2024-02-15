import random

# Definir la palabra secreta
palabras=['alonso','barrichelo','kubica','raikkonen','schumacher','button']
palabra_secreta=random.choice(palabras)

# Crear una lista para rastrear las letras adivinadas
letras_adivinadas = []

intentos_maximos = 6
intentos = 0
#Mientras que intentos sea menor que intentos maximos
while intentos < intentos_maximos:
    #Convertimos las letras a minuscula
    letra = input("Ingresa una letra: ").lower()

    #Comprueba si hemos adivinado las letras en letras_adivinadas y si es asi vuelve a empezar el bucle
    if letra in letras_adivinadas:
        print("Ya adivinaste esta letra antes.")
        continue
    
    #Metemos la ultima letra a letras adivinadas
    letras_adivinadas.append(letra)

    #Si no esta la letra en palabra_secreta, suma 1 intento y saca mensaje
    if letra not in palabra_secreta:
        intentos += 1
        print(f"Letra incorrecta. Te quedan {intentos_maximos - intentos} intentos.")
    else:
        print("¡Adivinaste una letra!")

    #Palabra mostrada es la que se va mostrando en el juego
    palabra_mostrada = ""

    #Para cada letra en palabara secreta,  
    for letra_secreta in palabra_secreta:
        #comprueba que esa letra este en toda la palabra
        if letra_secreta in letras_adivinadas:
            #muestra en que posicion se encuentran
            palabra_mostrada += letra_secreta
        else:
            #sino muestra _ 
            palabra_mostrada += "_ "
    #y despues muestra lo que llevas adivinado
    print(palabra_mostrada)

    #Comprueba que la palabra adivinada es igual a la que hay que adivinar y para el buble
    if palabra_mostrada == palabra_secreta:
        print(f"¡Ganaste! Has adivinado la palabra {palabra_secreta}")
        break
#Si los intentos es igual a el numero maximo, muestra la palabra secreta
if intentos == intentos_maximos:
    print(f"Perdiste. La palabra secreta era: {palabra_secreta}")