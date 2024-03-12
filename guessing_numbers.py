guess = 0
tries = 0

while guess != 6 and tries < 5:
    guess = int(input("Adivina el número: "))
    tries += 1
    if guess == 6:
        print("¡Lo conseguiste!")
    elif tries >= 5:
        print("Lo siento, has agotado tus intentos.")
    else:
        print("¡Inténtalo de nuevo!")

"""
Desglosemos este código en partes:

guess = 0 y tries = 0: estas son tus variables iniciales. guess se utiliza para almacenar cada intento de adivinación del usuario, y tries lleva la cuenta de cuántos intentos ha realizado.

while guess != 6 and tries < 5:: este es el inicio de tu bucle while. El código en este bucle se ejecutará mientras la suposición del usuario (guess) no sea igual a 6 y el número de intentos (tries) sea menor que cinco.

guess = int(input("Adivina el número: ")): esto recoge la entrada del usuario, la convierte en un número entero y la almacena en guess.

tries += 1: esto incrementa la cuenta de tries en uno cada vez que se pasa por el bucle.

if guess == 6:: esta es una declaración condicional que comprueba si el usuario ha adivinado correctamente el número. Si es así, imprime "¡Lo conseguiste!".

elif tries >= 5:: este es el segundo control. elif es una contracción de "else if". Entonces, si la suposición del usuario no es 6 (el primer if), comprueba si el número de intentos es igual o superior a 5. Si es así, imprime "Lo siento, has agotado tus intentos."

else: print("¡Inténtalo de nuevo!"): este es el último recurso del control. Si ninguno de los anteriores es cierto (el if y el elif), entonces imprime "¡Inténtalo de nuevo!"
"""
