

add = 1
subtraction = 2
multiplication = 3
division = 4
result = "Error"
operation = 0

print("\n")
print("Calculator Test".center(50, "="))
print("\n")
print("Which operation you want to do?")
print("Add [1] ")
print("Subtraction [2] ")
print("Multiplication [3] ")
print("Division [4] ")
print("\n")

while operation != 1 and operation != 2 and operation != 3 and operation != 4:
    operation = float(input("Choose one: "))

first_number = float(input("Give me the first number: "))
second_number = float(input("Give me the second number: "))

if operation == 1:
    result = first_number + second_number
elif operation == 2:
    result = first_number - second_number
elif operation == 3:
    result = first_number * second_number
elif operation == 4 and second_number == 0.0 and first_number == 0:
    print("Infinite")
    result = "¡Whoa!"
elif operation == 4 and second_number == 0.0:
    print("Watch out")
elif operation == 4:
    result = first_number / second_number


print("Your result is {}".format(result))
