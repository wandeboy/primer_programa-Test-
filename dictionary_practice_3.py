

dict_str = dict()

user_string = input('Tell me something: ')
words = []
word = ''
for letter in user_string:
    if letter != ' ':
        word += letter
    else:
        words.append(word)
        word = ''

words.append(word)

for word in words:
    if not (word in dict_str):
        dict_str[word] = 1
    else:
        dict_str[word] += 1

for word in dict_str:

    print('{}: {} '.format(word, dict_str[word]))



