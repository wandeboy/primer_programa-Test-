
user_list = []
user_number = ''
user_limit = 0
number_average = 0

print('What do you want to do?')
print('Get the maximum [MAX]')
print('Get the minimum [MIN]')
print('Get the average [AVG]')
print('Get the lengthy [LEN]')
process = input('Which one?: ').upper()

while not process == 'MAX' and process == 'MIN' and process == 'AVG' and process == 'LEN':
    process = input('Which one [MIN] [MAX] [AVG]?: ').upper()

if process == 'MAX':

    user_limit = int(input('How many number will you put?: '))

    while len(user_list) < user_limit:
        while not user_number.isdigit():
            user_number = input('Choose a number: ')
            if not user_number.isdigit():
                print('do not put letters')
        user_list.append(user_number)
        print('Number Add!')
        user_number = ''

    max_number = user_list[0]

    for number in user_list:

        if number > max_number:
            max_number = number

    print('The min number is {}'.format(max_number))

elif process == 'MIN':

    user_limit = int(input('How many number will you put?: '))

    while len(user_list) < user_limit:
        while not user_number.isdigit():
            user_number = input('Choose a number: ')
            if not user_number.isdigit():
                print('do not put letters')
        user_list.append(user_number)
        print('Number Add!')
        user_number = ''

    min_number = user_list[0]

    for number in user_list:

        if number < min_number:
            min_number = number

    print('The min number is {}'.format(min_number))

elif process == 'AVG':

    user_limit = int(input('How many number will you put?: '))

    while len(user_list) < user_limit:
        while not user_number.isdigit():
            user_number = input('Choose a number: ')
            if not user_number.isdigit():
                print('do not put letters')
        user_list.append(float(user_number))
        print('Number Add!')
        user_number = ''

    for number_list in user_list:
        number_average += number_list

    print('The average is {}'.format(number_average / user_limit))

elif process == 'LEN':
    user_number = input('determine a number ["END" for exit]: ')
    count = 0

    while not user_number == 'END':
        # it's the same of len()
        user_list.append(user_number)
        user_number = input('determine a number ["END" for exit]: ')

    for element in user_list:
        count += 1

    print('The lengthy of list is {}'.format(count))
