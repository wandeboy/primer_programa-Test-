

def max_between_three(first, second, third):

    number = []
    number.append(float(first))
    number.append(float(second))
    number.append(float(third))
    max_number = max(number)
    return max_number


def number_in_range(number, minimum, maximum):

    if minimum <= number <= maximum:
        return True
    else:
        return False


def pair(numbers):

    return_list = []
    for number in numbers:
        if number % 2 == 0:
                return_list.append(number)

    return return_list


def underlines(string):

    print(string)
    final_underline = ''
    for repeat in range(len(string)):
        final_underline += '-'
    print(final_underline)



