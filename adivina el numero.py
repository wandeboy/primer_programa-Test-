
from random import randrange

numero_ganador = randrange(15)
win = "false"
print("Adivina un numero del 1 al 15 (5 intentos)")

primer_intento = 0
segundo_intento = 0
tercer_intento = 0
cuarto_intento = 0
quitno_intento = 0

primer_intento = int(input("Primer intento: "))

if primer_intento == numero_ganador:
    win = "true1"

elif win == "false":
    segundo_intento = int(input("Realiza tu segundo intento: "))

if segundo_intento == numero_ganador:
    win = "true2"

elif win == "false":
    tercer_intento = int(input("¡Vamos! La tercera es la vencida: "))

if tercer_intento == numero_ganador:
    win = "true3"

elif win == "false":
    cuarto_intento = int(input("¡conenctrate tu puedes!: "))

if cuarto_intento == numero_ganador:
    win = "true4"

elif win == "false":
    quitno_intento = int(input("vamos tecnicamente ahora tienes mayor probailidades de acertar ¡tu puedes!: "))

if quitno_intento == numero_ganador:
    win = "true5"

elif win == "false":
    print("bueno al menos lo intentaste, pero has perdido")

if win == "false":
    print("¡Vuelve a intentarlo!")
elif win == "true1":
    print("¡Has ganado a la primera!")
elif win == "true2":
    print("¡Exelente has ganado en tu segundo intento!")
elif win == "true3":
    print("¡Buen trabajo! La tercera fue la vencida")
elif win == "true4":
    print("¡lo lograste, has ganado en el cuerto intento!")
elif win == "true5":
    print("al final lo lograste, ¡muy bien!")




