from string import ascii_uppercase as up, ascii_lowercase as low

RUS_LET = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
RUS_LET_UP = RUS_LET.upper()
d = {1: 'русский(от 0 до 32)', 2: 'английский(от 0 до 26)'}
d2 = {1: 'шифровать', 2: 'дешифровать'}


def correct_word(word):
    while True:
        if res_language == 1:
            if not any([c in (low + up + 'ё') for c in word]):
                break
            else:
                word = input('В слове на русском языке не должно быть английских символов и буквы ё.'
                              'Введите другое: ')
        elif res_language == 2:
            if not any([c in (RUS_LET + RUS_LET_UP) for c in word]):
                break
            else:
                word = input('В слове на английском языке не должно быть русских символов.'
                              'Введите другое: ')
    return word


def decode_word(word, low_let, up_let, shift):
    for c in word:
        if c not in (low_let + up_let):
            print(c, end='')
        else:
            if c.isupper():
                if ord(c) - shift < ord(up_let[0]):
                    print(chr(ord(c) - shift + len(low_let)), end='')
                else:
                    print(chr(ord(c) - shift), end='')
            else:
                if ord(c) - shift < ord(low_let[0]):
                    print(chr(ord(c) - shift + len(low_let)), end='')
                else:
                    print(chr(ord(c) - shift), end='')
    print()


def code_word(word, low_let, up_let, shift):
    for c in word:
        if c not in (low_let + up_let):
            print(c, end='')
        else:
            if c.isupper():
                if ord(c) + shift > ord(up_let[-1]):
                    print(chr(ord(c) + shift - len(up_let)), end='')
                else:
                    print(chr(ord(c) + shift), end='')
            else:
                if ord(c) + shift > ord(low_let[-1]):
                    print(chr(ord(c) + shift - len(up_let)), end='')
                else:
                    print(chr(ord(c) + shift), end='')
    print()


def correct_name(n):
    while True:
        if n.strip().isalpha():
            break
        else:
            n = input('В имени разве могут быть цифры или имя без имени? Попробуйте еще раз: ')
    return n.strip()


def correct_step(number):
    while True:
        if number.strip().isdigit():
            if res_language == 1 and 0 <= int(number) <= 32:
                break
            elif res_language == 2 and 0 <= int(number) <= 26:
                break
            else:
                number = input(f'Выберите шаг сдвига: {d[1] if res_language == 1 else d[2]}: ')
        else:
            number = input(f'Выберите шаг сдвига: {d[1] if res_language == 1 else d[2]}: ')
    number = int(number)
    print(f'Вы выбрали вариант {number}')
    return number


def correct_choice(number):
    while number.strip() not in '12':
        if number.strip() in '12':
            break
        else:
            number = input('Увы такого варианта нету. Выберите 1 или 2: ')
    number = int(number.strip())
    print(f'Вы выбрали вариант {number}')
    return number


while True:
    print('Добро пожаловать!')
    name = input('Введите ваше имя: ')
    res_name = correct_name(name)
    print(f'Здравствуйте, {res_name}. Я могу шифровать и дешифровать сообщения на русском или английском языке')
    result = input('Выберите цифру из вариантов (1 - шифровать, 2 - дешифровать) : ')
    res_shifr = correct_choice(result)
    result = input('Выберите цифру из вариантов (1 - русский, 2 - английский) : ')
    res_language = correct_choice(result)
    result = input(f'Выберите шаг сдвига: {d[1] if res_language == 1 else d[2]}: ')
    res_step = correct_step(result)
    word = input(f'Введите слово или фразу, которые нужно {d2[res_shifr]}: ')
    res_word = correct_word(word)
    if res_shifr == 1:
        if res_language == 1:
            code_word(res_word, RUS_LET, RUS_LET_UP, res_step)
        else:
            code_word(res_word, low, up, res_step)
    else:
        if res_language == 1:
            decode_word(res_word, RUS_LET, RUS_LET_UP, res_step)
        else:
            decode_word(res_word, low, up, res_step)
    output = input('Если желаете покинуть программу, просто напишите EXIT и нажмите ENTER. В противном случае она '
                   'автоматически перезапустится ')
    if output.strip().upper() == 'EXIT':
        break
