

class Atk:
    name = ''
    element_type = ''
    power = int
    physical = None
    accuracy = int
    pp = int

    def __init__(self):
        self.name = self.name
        self.type = self.element_type
        self.power = self.power
        self.accuracy = self.accuracy
        self.pp = self.pp
        self.isphysical = self.physical
        self.isspecial = not self.physical

"""Grass atks"""
class Leafblade(Atk):
    name = 'Leaf Blade'
    element_type = 'grass'
    power = 80
    physical = None
    accuracy = 100
    pp = 15


class MegaDrain(Atk):
    name = 'Mega Drain'
    element_type = 'grass'
    power = 40
    physical = False
    accuracy = 100
    pp = 15


class Magicalleaf(Atk):
    name = 'Magical Leaf'
    element_type = 'grass'
    power = 60
    physical = False
    accuracy = False
    pp = 20


class Razorleaf(Atk):
    name = 'Razor Leaf'
    element_type = 'grass'
    power = 55
    physical = True
    accuracy = 95
    pp = 25

"""Normal atks"""
class Tackle(Atk):
    name = 'Tackle'
    element_type = 'normal'
    power = 50
    physical = True
    accuracy = 95
    pp = 10


class Round(Atk):
    name = 'Round'
    element_type = 'normal'
    power = 60
    physical = False
    accuracy = 100
    pp = 15


class Triattack(Atk):
    name = 'Round'
    element_type = 'normal'
    power = 80
    physical = False
    accuracy = 100
    pp = 10


class Stomp(Atk):
    name = 'Stomp'
    element_type = 'normal'
    power = 65
    physical = True
    accuracy = 100
    pp = 20

"""Steel atks"""
class Mirrorshot(Atk):
    name = 'Mirror Shot'
    element_type = 'steel'
    power = 65
    physical = False
    accuracy = 85
    pp = 10


class Irontail(Atk):
    name = 'Iron Tail'
    element_type = 'steel'
    power = 100
    physical = True
    accuracy = 75
    pp = 15


class Bulletpunch(Atk):
    """priority atk"""
    name = 'Bullet Punch'
    element_type = 'steel'
    power = 40
    physical = True
    accuracy = 100
    pp = 30


class Geargrind(Atk):
    name = 'Gear Grind'
    element_type = 'steel'
    power = 50
    physical = True
    accuracy = 85
    pp = 15


"""bug atks"""
class Xscissor(Atk):
    name = 'X-Scissor'
    element_type = 'bug'
    power = 80
    physical = True
    accuracy = 100
    pp = 15


class Bugbuzz(Atk):
    name = 'Bug Buzz'
    element_type = 'bug'
    power = 90
    physical = False
    accuracy = 100
    pp = 10


class Bugbite(Atk):
    name = 'Bug Bite'
    element_type = 'bug'
    power = 60
    physical = True
    accuracy = 100
    pp = 20


class SilverWind(Atk):
    name = 'Silver Wind'
    element_type = 'bug'
    power = 60
    physical = False
    accuracy = 100
    pp = 5

    """ghost atks"""
class Hex(Atk):
        name = 'Hex'
        element_type = 'ghost'
        power = 65
        physical = False
        accuracy = 100
        pp = 10


class Shadowpunch(Atk):
        name = 'Shadow Punch'
        element_type = 'ghost'
        power = 60
        physical = True
        accuracy = False
        pp = 20


class MoongeistBeam(Atk):
        name = 'Moongeist Beam'
        element_type = 'ghost'
        power = 100
        physical = False
        accuracy = 100
        pp = 5


class Phantomforce(Atk):
        name = 'Phantom Force'
        element_type = 'ghost'
        power = 90
        physical = True
        accuracy = 100
        pp = 10


"""fight atks"""
class Xscissor(Atk):
    name = 'X-Scissor'
    element_type = 'bug'
    power = 80
    physical = True
    accuracy = 100
    pp = 15


class Bugbuzz(Atk):
    name = 'Bug Buzz'
    element_type = 'bug'
    power = 90
    physical = False
    accuracy = 100
    pp = 10


class Bugbite(Atk):
    name = 'Bug Bite'
    element_type = 'bug'
    power = 60
    physical = True
    accuracy = 100
    pp = 20


class SilverWind(Atk):
    name = 'Silver Wind'
    element_type = 'bug'
    power = 60
    physical = False
    accuracy = 100
    pp = 5


"""fight atks"""

class Xscissor(Atk):
    name = 'X-Scissor'
    element_type = 'bug'
    power = 80
    physical = True
    accuracy = 100
    pp = 15


class Bugbuzz(Atk):
    name = 'Bug Buzz'
    element_type = 'bug'
    power = 90
    physical = False
    accuracy = 100
    pp = 10


class Bugbite(Atk):
    name = 'Bug Bite'
    element_type = 'bug'
    power = 60
    physical = True
    accuracy = 100
    pp = 20


class SilverWind(Atk):
    name = 'Silver Wind'
    element_type = 'bug'
    power = 60
    physical = False
    accuracy = 100
    pp = 5


"""fight atks"""
class Xscissor(Atk):
    name = 'X-Scissor'
    element_type = 'bug'
    power = 80
    physical = True
    accuracy = 100
    pp = 15


class Bugbuzz(Atk):
    name = 'Bug Buzz'
    element_type = 'bug'
    power = 90
    physical = False
    accuracy = 100
    pp = 10


class Bugbite(Atk):
    name = 'Bug Bite'
    element_type = 'bug'
    power = 60
    physical = True
    accuracy = 100
    pp = 20


class SilverWind(Atk):
    name = 'Silver Wind'
    element_type = 'bug'
    power = 60
    physical = False
    accuracy = 100
    pp = 5


"""fight atks"""
class Xscissor(Atk):
    name = 'X-Scissor'
    element_type = 'bug'
    power = 80
    physical = True
    accuracy = 100
    pp = 15


class Bugbuzz(Atk):
    name = 'Bug Buzz'
    element_type = 'bug'
    power = 90
    physical = False
    accuracy = 100
    pp = 10


class Bugbite(Atk):
    name = 'Bug Bite'
    element_type = 'bug'
    power = 60
    physical = True
    accuracy = 100
    pp = 20


class SilverWind(Atk):
    name = 'Silver Wind'
    element_type = 'bug'
    power = 60
    physical = False
    accuracy = 100
    pp = 5

