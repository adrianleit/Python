import random

# Definir la palabra secreta
palabras=['alonso','barrichelo','kubica','raikkonen','schumacher','button']
palabra_secreta=random.choice(palabras)

# Crear una lista para rastrear las letras adivinadas
letras_adivinadas = []

intentos_maximos = 6
intentos = 0

while intentos < intentos_maximos:
    letra = input("Ingresa una letra: ").lower()

    if letra in letras_adivinadas:
        print("Ya adivinaste esta letra antes.")
        continue

    letras_adivinadas.append(letra)

    if letra not in palabra_secreta:
        intentos += 1
        print(f"Letra incorrecta. Te quedan {intentos_maximos - intentos} intentos.")
    else:
        print("¡Adivinaste una letra!")

    palabra_mostrada = ""
    for letra_secreta in palabra_secreta:
        if letra_secreta in letras_adivinadas:
            palabra_mostrada += letra_secreta
        else:
            palabra_mostrada += "_ "
    print(palabra_mostrada)

    if palabra_mostrada == palabra_secreta:
        print(f"¡Ganaste! Has adivinado la palabra {palabra_secreta}")
        break

if intentos == intentos_maximos:
    print(f"Perdiste. La palabra secreta era: {palabra_secreta}")