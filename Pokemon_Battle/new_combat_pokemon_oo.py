from time import sleep
from random import randint
from Pokemon_Battle import poke_class


AMOUNT_OF_POKEMON_AVAILABLE = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


def ask_until_option_expected(options, string):
    selected_action = ""

    while not selected_action.isdigit() or (selected_action.isdigit() and int(selected_action) not in options):
        selected_action = input(string)

    return int(selected_action)


def choose_your_pokemon(options):
    print('Now Choose your pokemon:')
    print('1 - Charmander')
    print('2 - Bulbasaur')
    print('3 - Squirtle')
    print('4 - Pickachu')
    print('5 - Zorua')
    print('6 - Gastly')
    print('7 - Pidgay')
    print('8 - Ekans')
    print('9 - Cubone')
    print('10 - Geodude')
    print('11 - Abra')
    print('12 - Eevee')
    print('13 - Clefairy')
    print('14 - Machop')
    print('15 - Aron')
    print('16 - Caterpie')

    choice = ask_until_option_expected(options, 'What pokemon you choose?:')
    user_pokemon = ''

    if choice == 1:
        user_pokemon = name_pokemon(poke_class.Charmander(name='Charmander'), 'Charmander', choice)
    elif choice == 2:
        user_pokemon = name_pokemon(poke_class.Bulbasaur(name='Bulbasaur'), 'Bulbasaur', choice)
    elif choice == 3:
        user_pokemon = name_pokemon(poke_class.Squirtle(name='Squirtle'), 'Squirtle', choice)
    elif choice == 4:
        user_pokemon = name_pokemon(poke_class.Pickachu(name='Pickachu'), 'Pickachu', choice)
    elif choice == 5:
        user_pokemon = name_pokemon(poke_class.Zorua(name='Zorua'), 'Zorua', choice)
    elif choice == 6:
        user_pokemon = name_pokemon(poke_class.Gastly(name='Gastly'), 'Gastly', choice)
    elif choice == 7:
        user_pokemon = name_pokemon(poke_class.Pidgay(name='Pidgay'), 'Pidgay', choice)
    elif choice == 8:
        user_pokemon = name_pokemon(poke_class.Ekans(name='Ekans'), 'Ekans', choice)
    elif choice == 9:
        user_pokemon = name_pokemon(poke_class.Cubone(name='Cubone'), 'Cubone', choice)
    elif choice == 10:
        user_pokemon = name_pokemon(poke_class.Geodude(name='Geodude'), 'Geodude', choice)
    elif choice == 11:
        user_pokemon = name_pokemon(poke_class.Abra(name='Abra'), 'Abra', choice)
    elif choice == 12:
        user_pokemon = name_pokemon(poke_class.Eevee(name='Eevee'), 'Eevee', choice)
    elif choice == 13:
        user_pokemon = name_pokemon(poke_class.Clefairy(name='Clefairy'), 'Clefairy', choice)
    elif choice == 14:
        user_pokemon = name_pokemon(poke_class.Machop(name='Machop'), 'Machop', choice)
    elif choice == 15:
        user_pokemon = name_pokemon(poke_class.Aron(name='Aron'), 'Aron', choice)
    elif choice == 16:
        user_pokemon = name_pokemon(poke_class.Caterpie(name='Caterpie'), 'Caterpie', choice)

    return user_pokemon


def name_pokemon(class_pokemon, pokemon, choice):
    pokemon_name = input('How do you want to name your {}?: '.format(pokemon))
    user_pokemon = ''
    if pokemon_name == '':
        user_pokemon = class_pokemon
    else:
        if choice == 1:
            user_pokemon = poke_class.Charmander(name=pokemon_name)
        elif choice == 2:
            user_pokemon = poke_class.Bulbasaur(name=pokemon_name)
        elif choice == 3:
            user_pokemon = poke_class.Squirtle(name=pokemon_name)
        elif choice == 4:
            user_pokemon = poke_class.Pickachu(name=pokemon_name)
        elif choice == 5:
            user_pokemon = poke_class.Zorua(name=pokemon_name)
        elif choice == 6:
            user_pokemon = poke_class.Gastly(name=pokemon_name)
        elif choice == 7:
            user_pokemon = poke_class.Pidgay(name=pokemon_name)
        elif choice == 8:
            user_pokemon = poke_class.Ekans(name=pokemon_name)
        elif choice == 9:
            user_pokemon = poke_class.Cubone(name=pokemon_name)
        elif choice == 10:
            user_pokemon = poke_class.Geodude(name=pokemon_name)
        elif choice == 11:
            user_pokemon = poke_class.Abra(name=pokemon_name)
        elif choice == 12:
            user_pokemon = poke_class.Eevee(name=pokemon_name)
        elif choice == 13:
            user_pokemon = poke_class.Clefairy(name=pokemon_name)
        elif choice == 14:
            user_pokemon = poke_class.Machop(name=pokemon_name)
        elif choice == 15:
            user_pokemon = poke_class.Aron(name=pokemon_name)
        elif choice == 16:
            user_pokemon = poke_class.Caterpie(name=pokemon_name)

    return user_pokemon


def choose_enemy_pokemon(options):
    choice = randint(options[0], options[-1])
    enemy_pokemon = 'ERROR'

    if choice == 1:
        enemy_pokemon = poke_class.Charmander(name='Charmander')
    elif choice == 2:
        enemy_pokemon = poke_class.Bulbasaur(name='Bulbasaur')
    elif choice == 3:
        enemy_pokemon = poke_class.Squirtle(name='Squirtle')
    elif choice == 4:
        enemy_pokemon = poke_class.Pickachu(name='Pickachu')
    elif choice == 5:
        enemy_pokemon = poke_class.Zorua(name='Zorua')
    elif choice == 6:
        enemy_pokemon = poke_class.Gastly(name='Gastly')
    elif choice == 7:
        enemy_pokemon = poke_class.Pidgay(name='Pidgay')
    elif choice == 8:
        enemy_pokemon = poke_class.Ekans(name='Ekans')
    elif choice == 9:
        enemy_pokemon = poke_class.Cubone(name='Cubone')
    elif choice == 10:
        enemy_pokemon = poke_class.Geodude(name='Geodude')
    elif choice == 11:
        enemy_pokemon = poke_class.Abra(name='Abra')
    elif choice == 12:
        enemy_pokemon = poke_class.Eevee(name='Eevee')
    elif choice == 13:
        enemy_pokemon = poke_class.Clefairy(name='Clefairy')
    elif choice == 14:
        enemy_pokemon = poke_class.Machop(name='Machop')
    elif choice == 15:
        enemy_pokemon = poke_class.Aron(name='Aron')
    elif choice == 16:
        enemy_pokemon = poke_class.Caterpie(name='Caterpie')

    return enemy_pokemon


def user_turn(user_pokemon, enemy_pokemon):
    is_user_turn = True
    print("Is your turn".center(50, "=").title())
    sleep(1)
    user_pokemon.attack(enemy_pokemon, is_user_turn)
    sleep(1)


def enemy_turn(user_pokemon, enemy_pokemon):
    is_user_turn = False
    print("Enemy turn".center(50, "=").title())
    choice_enemy_attack = randint(1, 4)
    enemy_pokemon.attack(user_pokemon, is_user_turn, choice_enemy_attack)
    sleep(1)


def main():
    print("\n")
    print("welcome to the pokemon battle".center(50, "=").title())
    print("\n")

    user_pokemon = choose_your_pokemon(AMOUNT_OF_POKEMON_AVAILABLE)
    enemy_pokemon = choose_enemy_pokemon(AMOUNT_OF_POKEMON_AVAILABLE)

    print('{} wild has appeared'.format(enemy_pokemon.name).center(50, "=").title())
    sleep(1)
    while not user_pokemon.life <= 0 or enemy_pokemon.life <= 0:
        user_turn(user_pokemon, enemy_pokemon)
        enemy_turn(user_pokemon, enemy_pokemon)

    if user_pokemon.life <= 0:
        print('').center(50, "=").title()
        print('Your Pokemon is Fainted').center(50, "=").title()
        print("You scurried to a Pokemon Center, protecting the exhausted and fainted Pokemon from further harm...")\
            .center(50, "=").title()
        print('').center(50, "=").title()

    elif enemy_pokemon.life <= 0:
        print('').center(50, "=").title()
        print('Enemy Pokemon is Fainted').center(50, "=").title()
        print("You Win!").center(50, "=").title()
        print('').center(50, "=").title()


if __name__ == "__main__":
    main()
