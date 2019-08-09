

user_list = []
str_list = []
int_list = []
value = 1
total = 0

user_value = str((input('Give me number or text ["END", for exit]: ')))

while not user_value == 'END':
    if user_value.isdigit():
        user_list.append(int(user_value))
    elif user_value.replace(".", "", 1).isdigit():
            user_list.append(float(user_value))
    else:
        user_list.append(user_value)
    user_value = str((input('Give me number or text ["END", for exit]: ')))

for index in range(len(user_list)):

    if isinstance(user_list[index], (int, float)):
        int_list.append(user_list[index])
    else:
        str_list.append(user_list[index])

print(int_list)
print(str_list)

for index in range(len(int_list)):
    total = value * int_list[index]
    value = total

print('the multiplication between the numbers are: {}'.format(total))

for index in range(len(str_list)):

    print('the numbers in phrases number {} are {}'.format(index + 1, str_list[index].__len__()))

