
from random import randrange

guess_number = "unknown"
choose = "unknown"

print("\n")
print("Welcome to the guess the number".title().center(50, "="))
print("\n")
print("Choose the difficulty")
print("Beginner [0]")
print("Easy [1]")
print("Medium [2]")
print("Hard [3]")
print("Hardcore [4]")
print("The Lucky is Smiling you? [5]")
print("\n")

while choose != 0 and choose != 1 and choose != 2 and choose != 3 and choose != 4 and choose != 5:

    choose = int(input("Choose one: "))

    if choose == 0:
        difficult_min = 2
        difficult_max = 5
    elif choose == 1:
        difficult_min = 3
        difficult_max = 12
    elif choose == 2:
        difficult_min = 5
        difficult_max = 20
    elif choose == 3:
        difficult_min = 8
        difficult_max = 25
    elif choose == 4:
        difficult_min = 18
        difficult_max = 35
    elif choose == 5:
        difficult_min = 30
        difficult_max = 50
    else:
        print("Tell me in numbers (0, 1, 2, 3, 4, 5)")

print("\n")

print("Now choose who will guesses")
print("Okay, you didn't see the next part")

winner_number = int(input("You will think a number and put in here ==> "))

print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")

print("the number is between {} and {}".format(winner_number - randrange(difficult_min, difficult_max),
                                               winner_number + randrange(difficult_min, difficult_max)))

while winner_number != guess_number:
    guess_number = int(input("Now try to guess: "))

print("¡Good Golly!")
print("You Guessed")
