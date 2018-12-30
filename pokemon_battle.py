
from random import choice, randint

print("\n")
print("welcome to the pokemon battle".center(50, "=").title())
print("\n")
print("Now with your Pikachu you need to defeat your opponent, ")
print("you have two types of attacks (Iron Tail and Thunder Shock).")
print("\n")
print("Choose An Opponent:")
print("Squirtle: HP = 229 / Dmg = 145 / S.Dmg = 122 / Def = 166 / S.Def = 164 ")
print("Charmander: HP = 219 / Dmg = 154 / S.Dmg = 140 / Def = 122 / S.Def = 136 ")
print("Bulbasaur: HP = 231 / Dmg = 147 / S.Dmg = 149 / Def = 134 / S.Def = 166 ")
print("\n")

enemy_pokemon = input("Now choose (Squirtle, Charmander, Bulbasaur): ").upper()

pikachu_life = 211
pikachu_def = 116
pikachu_s_def = 136
enemy_life = 0
enemy_dmg = 0
enemy_s_dmg = 0
enemy_def = 1
enemy_s_def = 1
enemy_attack = "unknown"
enemy_s_attack = "unknown"
dmg = 0

if "BULBASAUR" == enemy_pokemon:
    enemy_life = 231
    enemy_dmg = 147
    enemy_s_dmg = 149
    enemy_def = 134
    enemy_s_def = 166
    enemy_attack = "Tackle"
    enemy_s_attack = "Razor Leaf"

elif "CHARMANDER" == enemy_pokemon:
    enemy_life = 219
    enemy_dmg = 154
    enemy_s_dmg = 140
    enemy_def = 122
    enemy_s_def = 136
    enemy_attack = "Tackle"
    enemy_s_attack = "Flamethrower"

elif "SQUIRTLE" == enemy_pokemon:
    enemy_life = 229
    enemy_dmg = 145
    enemy_s_dmg = 122
    enemy_def = 166
    enemy_s_def = 164
    enemy_attack = "Tackle"
    enemy_s_attack = "Water pulse"

print("your life {}".format(pikachu_life))
print("enemy life {}".format(enemy_life))

while pikachu_life > 0 and enemy_life > 0:
    attack = (input("your turn, choose your attack ([1] Iron Tail or [2] Thunder Shock): "))
    if attack == "1":
        #pikachu Dmg = 160
        print("your pokemon use Iron Tail")
        dmg = (0.01 * 0.5 * randint(50, 120)) * ((((0.2 * 100 + 1) * 160 * randint(90, 100)) / (25 * enemy_s_def))+2)
        enemy_life -= dmg
        print("enemy life {}".format(int(enemy_life)))

    elif attack == "2":
        #picachu S.Dmg = 122
        print("your pokemon use Thunder Shock")
        dmg = (0.01 * 0.5 * randint(50, 120)) * ((((0.2 * 100 + 1) * 122 * randint(90, 100)) / (25 * enemy_s_def))+2)
        enemy_life -= dmg
        print("enemy life {}".format(int(enemy_life)))

    else:
        print("¡miss!")

    if enemy_life > 0:
        random_element = choice((1, 2))

        if random_element == 1:
            print("{} tunr".format(enemy_pokemon).capitalize())
            print("{} use {}".format(enemy_pokemon, enemy_s_attack).capitalize())
            dmg = (0.01 * 0.5 * randint(50, 120)) * ((((0.2 * 100 + 1) * enemy_s_dmg * randint(80, 90)) / (25 * pikachu_s_def))+2)
            pikachu_life -= dmg
            print("Pikachu life {}".format(int(pikachu_life)))
        else:
            print("{} tunr".format(enemy_pokemon).capitalize())
            print("{} use {}".format(enemy_pokemon, enemy_attack).capitalize())
            dmg = (0.01 * 0.5 * randint(50, 120)) * ((((0.2 * 100 + 1) * enemy_dmg * randint(80, 90)) / (25 * pikachu_def))+2)
            pikachu_life -= dmg
            print("Pikachu life {}".format(int(pikachu_life)))

if pikachu_life <= 0:
    print("Your Pokemon is Fainted")
    print("You scurried to a Pokémon Center, protecting the exhausted and fainted Pokémon from further harm...")

if enemy_life <= 0:
    print("Enemy Pokemon is Fainted")
    if enemy_attack == "unknown":
        print("you put your opponent wrong")
    print("¡You Win!")

