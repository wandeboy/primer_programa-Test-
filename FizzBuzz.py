

user_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
             16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 70]

two_list = []
three_list = []
five_list = []
seven_list = []

for index in range(len(user_list)):

    if user_list[index] % 2 == 0:
        two_list.append(user_list[index])
    if user_list[index] % 3 == 0:
        three_list.append(user_list[index])
    if user_list[index] % 5 == 0:
        five_list.append(user_list[index])
    if user_list[index] % 7 == 0:
        seven_list.append(user_list[index])
# FizzBuzz
    if user_list[index] % 5 == 0 and user_list[index] % 3 == 0:
        user_list[index] = 'Bazinga'
    elif user_list[index] % 5 == 0:
        user_list[index] = 'Buzz'
    elif user_list[index] % 3 == 0:
        user_list[index] = 'Fizz'

print(two_list)
print(three_list)
print(five_list)
print(seven_list)
print(user_list)

