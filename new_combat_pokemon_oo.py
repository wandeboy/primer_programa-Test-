
from random import randint


def ask_until_option_expected(options, string):
    selected_action = ""

    while not selected_action.isdigit() or (selected_action.isdigit() and int(selected_action) not in options):
        selected_action = input(string)

    return int(selected_action)


class Atk:
    def __init__(self, name='tackle', element_type='normal', power=30, physical=True, special=False):
        self.name = name
        self.type = element_type
        self.power = power
        self.isphysical = physical
        self.isspecial = special


class Pokemon:
    BASE_LIFE = 0
    ATK = 0
    DEF = 0
    SP_ATK = 0
    SP_DEF = 0
    atk1 = Atk()
    atk2 = Atk()
    atk3 = Atk()
    atk4 = Atk()
    SPEED = 0
    LVL = 50
    ELEMENT_TYPE = ''

    def __init__(self, name):
        self.name = name
        self.life = self.BASE_LIFE
        self.speed = self.SPEED
        self.type = self.ELEMENT_TYPE

    def attack(self, enemy_pokemon):
        print('Yours Attacks:'.center(50, '='))
        print('1 - {}'.format(self.atk1.name))
        print('2 - {}'.format(self.atk2.name))
        print('3 - {}'.format(self.atk3.name))
        print('4 - {}'.format(self.atk4.name))

        choice = ask_until_option_expected(['1', '2', '3', '4'], 'Which one should we use?')

        if choice == 1:
            bonus = self.bonus_type_atk_vs_type_selfpokemon(self.atk1)
            effectiveness = self.effectiveness(self.atk1, enemy_pokemon)
            enemy_pokemon.takedmg(self.atk1, bonus, effectiveness, enemy_pokemon)
        elif choice == 2:
            bonus = self.bonus_type_atk_vs_type_selfpokemon(self.atk2)
            effectiveness = self.effectiveness(self.atk2, enemy_pokemon)
            enemy_pokemon.takedmg(self.atk2, bonus, effectiveness, enemy_pokemon)
        elif choice == 3:
            bonus = self.bonus_type_atk_vs_type_selfpokemon(self.atk3)
            effectiveness = self.effectiveness(self.atk3, enemy_pokemon)
            enemy_pokemon.takedmg(self.atk3, bonus, effectiveness, enemy_pokemon)
        elif choice == 4:
            bonus = self.bonus_type_atk_vs_type_selfpokemon(self.atk4)
            effectiveness = self.effectiveness(self.atk4, enemy_pokemon)
            enemy_pokemon.takedmg(self.atk4, bonus, effectiveness, enemy_pokemon)

    def bonus_type_atk_vs_type_selfpokemon(self, atk):
        if atk.type == self.type:
            return 1.5
        else:
            return 1

    def effectiveness(self, atk, enemy_pokemon):
        return 1

    def takedmg(self, atk, bonus, effectiveness, enemy_pokemon):
        """ Dmg=0.01×B×E×V×((0.2×N+1)×A×P25×D+2)
        N = Nivel del Pokémon que ataca.
        A = Cantidad de ataque o ataque especial del Pokémon. Si el ataque que utiliza el Pokémon es físico se toma la
        cantidad de ataque y si es especial se toma la cantidad de ataque especial.
        P = Poder del ataque, el potencial del ataque.
        D = Cantidad de defensa del Pokémon rival. Si el ataque que hemos utilizado es físico cogeremos la cantidad de
        defensa del Pokémon rival, si el ataque que hemos utilizado es especial, se coge la cantidad de defensa especial
         del Pokémon rival.
        B = Bonificación. Si el ataque es del mismo tipo que el Pokémon que lo lanza toma un valor de 1.5, si el ataque
        es de un tipo diferente al del Pokémon que lo lanza toma un valor de 1.
        E = Efectividad. Puede tomar los valores de 0, 0.25, 0.5, 1, 2 y 4.
        V = Variación. Es una variable que comprende todos los valores discretos entre 85 y 100 (ambos incluidos)."""
        if atk.isphysical:
            dmg = 0.01 * bonus * effectiveness * randint(85, 100) * (
                        ((0.2 * self.LVL + 1) * self.ATK * atk.power) / (25 * enemy_pokemon.DEF + 2))
        else:
            dmg = 0.01 * bonus * effectiveness * randint(85, 100) * (
                        ((0.2 * self.LVL + 1) * self.SP_ATK * atk.power) / (25 * enemy_pokemon.SP_DEF + 2))

        print('{} used: {}'.format(self.name, atk.name))
        self.life -= dmg
        print('{} did {} damage'.format(atk.name, dmg))

    def show_life(self):
        print('Life of {}: {}'.format(self.name, self.life))



class Charmander(Pokemon):
    BASE_LIFE = 0
    ATK = 0
    DEF = 0
    SP_ATK = 0
    SP_DEF = 0
    SPEED = 0
    LVL = 50
    TYPE_ATK_1 = ''
    TYPE_ATK_2 = ''
    TYPE_ATK_3 = ''
    TYPE_ATK_4 = ''
    TYPE = ''


class Bulbasaur(Pokemon):
    BASE_LIFE = 0
    ATK = 0
    DEF = 0
    SP_ATK = 0
    SP_DEF = 0
    SPEED = 0
    LVL = 50
    TYPE = 'FIRE'


class Squirtle(Pokemon):
    BASE_LIFE = 0
    ATK = 0
    DEF = 0
    SP_ATK = 0
    SP_DEF = 0
    SPEED = 0
    LVL = 50
    TYPE = 'FIRE'


class Pickachu(Pokemon):
    BASE_LIFE = 0
    ATK = 0
    DEF = 0
    SP_ATK = 0
    SP_DEF = 0
    SPEED = 0
    LVL = 50
    TYPE = 'FIRE'


class Zorua(Pokemon):
    BASE_LIFE = 0
    ATK = 0
    DEF = 0
    SP_ATK = 0
    SP_DEF = 0
    SPEED = 0
    LVL = 50
    TYPE = 'FIRE'


class Gastly(Pokemon):
    BASE_LIFE = 0
    ATK = 0
    DEF = 0
    SP_ATK = 0
    SP_DEF = 0
    SPEED = 0
    LVL = 50
    TYPE = 'FIRE'


class Pidgay(Pokemon):
    BASE_LIFE = 0
    ATK = 0
    DEF = 0
    SP_ATK = 0
    SP_DEF = 0
    SPEED = 0
    LVL = 50
    TYPE = 'FIRE'


class Ekans(Pokemon):
    BASE_LIFE = 0
    ATK = 0
    DEF = 0
    SP_ATK = 0
    SP_DEF = 0
    SPEED = 0
    LVL = 50
    TYPE = 'FIRE'


class Cubone(Pokemon):
    BASE_LIFE = 0
    ATK = 0
    DEF = 0
    SP_ATK = 0
    SP_DEF = 0
    SPEED = 0
    LVL = 50
    TYPE = 'FIRE'


class Geodude(Pokemon):
    BASE_LIFE = 0
    ATK = 0
    DEF = 0
    SP_ATK = 0
    SP_DEF = 0
    SPEED = 0
    LVL = 50
    TYPE = 'FIRE'

class Abra(Pokemon):
    BASE_LIFE = 0
    ATK = 0
    DEF = 0
    SP_ATK = 0
    SP_DEF = 0
    SPEED = 0
    LVL = 50
    TYPE = 'FIRE'


class Eevee(Pokemon):
    BASE_LIFE = 0
    ATK = 0
    DEF = 0
    SP_ATK = 0
    SP_DEF = 0
    SPEED = 0
    LVL = 50
    TYPE = 'FIRE'


class Jigglypuff(Pokemon):
    BASE_LIFE = 0
    ATK = 0
    DEF = 0
    SP_ATK = 0
    SP_DEF = 0
    SPEED = 0
    LVL = 50
    TYPE = 'FIRE'


class Machop(Pokemon):
    BASE_LIFE = 0
    ATK = 0
    DEF = 0
    SP_ATK = 0
    SP_DEF = 0
    SPEED = 0
    LVL = 50
    TYPE = 'FIRE'


class Aron(Pokemon):
    BASE_LIFE = 0
    ATK = 0
    DEF = 0
    SP_ATK = 0
    SP_DEF = 0
    SPEED = 0
    LVL = 50
    TYPE = 'FIRE'


class Caterpie(Pokemon):
    BASE_LIFE = 0
    ATK = 0
    DEF = 0
    SP_ATK = 0
    SP_DEF = 0
    SPEED = 0
    LVL = 50
    TYPE = 'FIRE'
