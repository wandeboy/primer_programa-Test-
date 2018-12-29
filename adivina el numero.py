
from random import randrange

numero_ganador = randrange(15)

print("Adivina un numero del 1 al 15 (5 intentos)")

primer_intento = int(input("Primer intento: "))

if primer_intento == numero_ganador:
     print("¡Has ganado a la primera!")
else:
    segundo_intento = int(input("Realiza tu segundo intento: "))

    if segundo_intento == numero_ganador:
        print("¡Exelente has ganado en tu segundo intento!")
    else:
        tercer_intento = int(input("¡Vamos! La tercera es la vencida: "))

        if tercer_intento == numero_ganador:
            print("¡Buen trabajo! La tercera fue la vencida")
        else:
            cuarto_intento = int(input("¡conenctrate tu puedes!: "))

            if cuarto_intento == numero_ganador:
                print("¡lo lograste, has ganado en el cuerto intento!")
            else:
                quitno_intento = int(input("vamos tecnicamente ahora tienes mayor probailidades de acertar, un 1/11, ¡tu puedes!"))

                if quitno_intento == numero_ganador:
                    print("al final lo lograste, ¡muy bien!")
                else:
                    print("bueno al menos lo intentaste, pero has perdido")
