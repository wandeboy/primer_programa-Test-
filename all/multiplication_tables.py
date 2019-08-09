

print('Hello to the multiplication tables'.center(50, '='))

user_number = int(input('Choose the table: '))
start = int(input('Choose the start: '))
end = int(input('Choose the end: '))
steps = int(input('Determines the space between two numbers: '))

for multiple in range(start, end + 1,  steps):
    print('{} x {} = {}'.format(multiple, user_number, multiple * user_number))

