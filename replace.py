

vocals = ['a', 'e', 'i', 'o', 'u', 'á', 'é', 'í', 'ó', 'ú']
vocals_cap = []

for capital in vocals:
    vocals_cap.append(capital.upper())

for index in range((len(vocals_cap))):
    vocals.append(vocals_cap[index])

user_text = str(input('Tell me something: '))

new_text = user_text
txt_true = None
final_txt = ''

for index in range((len(user_text))):
    txt_true = None
    for index_1 in range((len(vocals))):
        edited_word = new_text[index].replace(vocals[index_1], '{}'.format(index + 1))
        if edited_word != new_text[index]:
            final_txt += edited_word
            txt_true = True
    if not txt_true:
        final_txt += edited_word
        txt_true = None

print(final_txt)


'''

vocals = ['a', 'á']
vocals_cap = []
user_text = []

for capital in vocals:
    vocals_cap.append(capital.upper())

for index in range((len(vocals_cap))):
    vocals.append(vocals_cap[index])

user_text = (str(input('Tell me something: ')))

new_text = user_text
final_txt = ''
vaca_true = None

for index in range((len(user_text))):
    vaca_true = None
    for index_1 in range((len(vocals))):
        edited_word = new_text[index].replace(vocals[index_1], 'VACA')
        if edited_word != new_text[index]:
            final_txt += edited_word
            vaca_true = True
    if not vaca_true:
        final_txt += edited_word
        vaca_true = None

print(final_txt)

'''

'''

vocals = ['a', 'e', 'i', 'o', 'u', 'á', 'é', 'í', 'ó', 'ú']
vocals_cap = []

for capital in vocals:
    vocals_cap.append(capital.upper())

for index in range((len(vocals_cap))):
    vocals.append(vocals_cap[index])

user_text = str(input('Tell me something: '))

new_text = user_text

for index in range((len(vocals))):

    edited_text = new_text.replace(vocals[index], 'i')
    new_text = edited_text

print(new_text)

'''

