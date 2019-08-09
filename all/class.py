from datetime import datetime


class Contact:

    def __init__(self, name, number, birthday):
        self.name = name
        self.number = number
        self.birthday = datetime.strptime(birthday, "%d/%m/%Y")

    def age(self):
        today = datetime.today()
        age = (today.year - self.birthday.year - 1)
        if today.month > self.birthday.month:
            age += 1
        elif today.month == self.birthday.month:
            if today.day > self.birthday.day:
                age += 1
            elif today.day == self.birthday.day:
                print('happy birthday dude')
                age += 1
        return age

class Cat:
    def __init__(self, name='Misifus', color='Gris', age=0):
        self.name = name
        self.color = color
        self.age = age


my_cat = Cat(name='Mau', color='amarillo', age=9)
other_cat = Cat()
neighbour_cat = Cat(name='hola', color='blanco', age=3)

cats = [my_cat, other_cat, neighbour_cat]

