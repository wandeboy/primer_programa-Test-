
import datetime
import random

AVERAGE_LIFESPAN_FEMALE = 83.4
AVERAGE_LIFESPAN_MALE = 77.4
SMOKER_PENALTY = 10
DRINKER_PENALTY = 10
SEDENTARY_PENALTY = 7


def yes_not_sometimes(message):
    answer = None
    while answer != 'Y' and answer != 'N' and answer != 'S'\
            and answer != 'YES' and answer != 'NO' and answer != 'SOMETIMES':
        print(message + ' [Y / N / S]')
        answer = input('yes / no / sometimes: ').upper()
    return answer


print('\n')
print('Knowing the day of your death'.center(50, '='))
user_birthday = input('When is your birthday? [dd/mm/yyyy]: ')
user_birthday = datetime.datetime.strptime(user_birthday, "%d/%m/%Y")
female_male = ''
average_lifespan = 0

while female_male != 'Y' and female_male != 'N':
    female_male = input('Are you male? [Y/N]: ').upper()

    if female_male == 'Y':
        average_lifespan = random.randint(int(AVERAGE_LIFESPAN_MALE/1.7), int(AVERAGE_LIFESPAN_MALE*1.15))
    elif female_male == 'N':
        average_lifespan = random.randint(int(AVERAGE_LIFESPAN_FEMALE/1.7), int(AVERAGE_LIFESPAN_FEMALE*1.15))

smoke = yes_not_sometimes('Do You smoke?')
drinker = yes_not_sometimes('Do you drink?')
sports = yes_not_sometimes('Do you do sports frequently?')

life_penalty = 0

if smoke == 'YES' or smoke == 'Y':
    life_penalty += SMOKER_PENALTY
elif smoke == 'SOMETIMES' or smoke == 'S':
    life_penalty += SMOKER_PENALTY / 2
if drinker == 'YES' or drinker == 'Y':
    life_penalty += DRINKER_PENALTY
elif drinker == 'SOMETIMES' or drinker == 'S':
    life_penalty += DRINKER_PENALTY / 2
if sports == 'NO' or sports == 'N':
    life_penalty += SEDENTARY_PENALTY
elif sports == 'SOMETIMES' or sports == 'S':
    life_penalty += SEDENTARY_PENALTY / 2


lifespan = average_lifespan - life_penalty
death_day = user_birthday + datetime.timedelta(days=lifespan*365)
day_to_death = death_day - datetime.datetime.now()

print('Your death date is {}, you have {} days left'.format(death_day.strftime('%d/%m/%Y'), day_to_death.days))
print('enjoy them')
