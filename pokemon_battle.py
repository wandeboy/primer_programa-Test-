

print("\n")
print("welcome to the pokemon battle".center(50, "=").title())
print("\n")
print("Now with your Pikachu you need to defeat your opponent, ")
print("you have two types of attacks (Iron Tail and Thunder Shock).")
print("\n")
print("Choose An Opponent:")
print("Squirtle: HP = 80 /Attack Water Gun 11 dmg")
print("Charmander: HP = 100 /Attack Flamethrower 9 dmg")
print("Bulbasaur: HP = 120 /Attack Vine Whip = 9 dmg")
print("\n")

enemy_pokemon = input("Now choose (Squirtle, Charmander, Bulbasaur): ").upper()

pikachu_life = 100
enemy_life = 0
enemy_dmg = 0
enemy_attack = "unknown"

if "BULBASAUR" == enemy_pokemon:
    enemy_life = 120
    enemy_dmg = 9
    enemy_attack = "Vine Whip"

elif "CHARMANDER" == enemy_pokemon:
    enemy_life = 100
    enemy_dmg = 9
    enemy_attack = "Flamethrower"

elif "SQUIRTLE" == enemy_pokemon:
    enemy_life = 80
    enemy_dmg = 11
    enemy_attack = "Water Gun"

print("your life {}".format(pikachu_life))
print("enemy life {}".format(enemy_life))

while pikachu_life > 0 and enemy_life > 0:
    attack = (input("your turn, choose your attack ([1] Iron Tail or [2] Thunder Shock): "))
    if attack == "1":
        print("your pokemon use Iron Tail")
        enemy_life -= 10
        print("enemy life {}".format(enemy_life))

    elif attack == "2":
        print("your pokemon use Thunder Shock")
        enemy_life -= 12
        print("enemy life {}".format(enemy_life))

    else:
        print("¡miss!")

    if enemy_life > 0:
        print("{} tunr".format(enemy_pokemon).capitalize())

        print("{} use {}".format(enemy_pokemon, enemy_attack).capitalize())

        pikachu_life -= enemy_dmg

        print("Pikachu life {}".format(pikachu_life))

if pikachu_life <= 0:
    print("Your Pokemon is Fainted")
    print("You scurried to a Pokémon Center, protecting the exhausted and fainted Pokémon from further harm...")

if enemy_life <= 0:
    print("Enemy Pokemon is Fainted")
    print("¡You Win!")

