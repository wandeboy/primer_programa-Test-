

phonebook = dict("")

print('What do you want to do?')
action = input('Add Date [A] / Consult Date [C] / Exit [E]: ').upper()

while not action == 'E':

    if action == 'A' or action == 'ADD' or action == 'ADD DATE':
        name = input("what's the name?")
        number = input("what's the Date?")
        phonebook[name] = number
        action = ''
    elif action == 'C' or action == 'CONSULT' or action == 'CONSULT Date':
        name = input("what's the name?")
        for consult in phonebook:
            if consult == name:
                print(phonebook[name])
        action = ''
    elif action == 'E' or action == 'EXIT':
        print('Bye')
    else:
        print('\n')
        print('Do you want to do something else?')
        action = input('Add Date [A] / Consult Date [C] / Exit [E]: ').upper()


