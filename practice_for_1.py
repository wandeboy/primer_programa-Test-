
vocals = ['a', 'e', 'i', 'o', 'u', 'á', 'é', 'í', 'ó', 'ú']

vocals_cap = []
for capital in vocals:
    vocals_cap.append(capital.upper())

space = ' '
points = '.'
comma = ','
colon = ':'
semicolon = ';'
question_mark = '?'
question_mark_2 = '¿'
exclamation_mark = '!'
exclamation_mark_2 = '¡'
apostrophe = "'"
quotation_marks = '"'
hyphen = '-'
equal = '='
underscore = '_'
punctuation_marks = [' ', '.', ',', ':', ';', '?', '!', "'", '"', '-', '¿', '¡', '=', '_']
capital_letters = []
n_exception = 0


user_text = input('Put a text here for analysis: ')


for capital_2 in user_text:
    capital_letters.append(capital_2.upper())

print('what do you want to do?')
print('\n')
length_text = input('Count length of the text? [y/n]: ').upper()
number_of_vocals_and_consonants = input('Count number of vocals and consonants? [y/n]: ').upper()
show_vocals = input('Do you want show vocals? [y/n]: ').upper()
number_capital_letters = input('Count the number of capital letters? [y/n]: ').upper()
punctuation_marks = input('Count punctuation marks? [y/n]: ').upper()

n_vocals = 0
n_consonants = 0
n_capital = 0
list_vocals = []
n_space = 0
n_points = 0
n_comma = 0
n_colon = 0
n_semicolon = 0
n_question_mark = 0
n_exclamation_mark = 0
n_apostrophe = 0
n_quotation_marks = 0
n_hyphen = 0
n_equal = 0
n_underscore = 0


for text in user_text:

    if text in punctuation_marks:
        n_exception += 1

    if number_of_vocals_and_consonants == 'Y':
        if text in vocals:
            n_vocals += 1
        elif text in vocals_cap:
            n_vocals += 1
        else:
            n_consonants += 1

    if show_vocals == 'Y':
        if text in vocals:
            list_vocals.append(text)
        elif text in vocals_cap:
            list_vocals.append(text)

    if number_capital_letters == 'Y':
        if text in capital_letters:
            n_capital += 1

    if punctuation_marks == 'Y':
        if text in space:
            n_space += 1
        elif text in points:
            n_points += 1
        elif text in comma:
            n_comma += 1
        elif text in colon:
            n_colon += 1
        elif text in semicolon:
            n_semicolon += 1
        elif text in question_mark:
            n_question_mark += 1
        elif text in exclamation_mark:
            n_exclamation_mark += 1
        elif text in apostrophe:
            n_apostrophe += 1
        elif text in quotation_marks:
            n_quotation_marks += 1
        elif text in hyphen:
            n_hyphen += 1
        elif text in equal:
            n_equal += 1
        elif text in underscore:
            n_underscore += 1
        elif text in question_mark_2:
            n_question_mark += 1
        elif text in exclamation_mark_2:
            n_exclamation_mark += 1

print('\n')

if length_text == 'Y':
    print('Number of words: {} '.format(len(user_text)))

if number_of_vocals_and_consonants == 'Y':
    print('Numbers of vocals: {} '.format(n_vocals))
    print('Numbers of consonants: {} '.format(n_consonants))

if show_vocals == 'Y':
    print('Vocals are: {}'.format(list_vocals))

if number_capital_letters == 'Y':
    print('Number of capital letters: {} '.format(n_capital - n_exception))

if punctuation_marks == 'Y':
    print('numbers of spaces: {} '.format(n_space))
    print('numbers of commas: {} '.format(n_comma))
    print('numbers of points: {} '.format(n_points))
    print('numbers of colons: {} '.format(n_colon))
    print('numbers of exclamation marks: {} '.format(n_exclamation_mark))
    print('numbers of apostrophes: {} '.format(n_apostrophe))
    print('numbers of semicolons: {} '.format(n_semicolon))
    print('numbers of question marks: {} '.format(n_question_mark))
    print('numbers of hyphens: {} '.format(n_hyphen))
    print('numbers of apostrophes: {} '.format(n_apostrophe))
    print('numbers of underscore: {} '.format(n_underscore))
    print('numbers of equals: {} '.format(n_equal))






