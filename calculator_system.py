"""
Перевод чисел из любой системы счисления в 10
Перевод чисел 10 системы в любую систему счисления
"""
from string import ascii_uppercase as up, digits as dig

d = dict(zip(range(10, 37), up))
d.update(dict(zip(up, range(10, 37))))


def correct_10_system(system):
    while True:
        if not system.strip().isdigit():
            system = input('Неккотектные данные!Введите целое число для системы счисления: ')
            continue
        if int(system) not in list(range(2, 37)):
            system = input('Неккоректные данные!Введите систему счисления(целое число от 2 до 36): ')
            continue
        break
    return system


def correct_10_number(number):
    while True:
        if not number.strip().isdigit():
            number = input('Неккотектные данные!Введите целое число: ')
            continue
        break
    return number


def correct_choice(number):
    while True:
        if number.strip() in ("1", "2"):
            break
        else:
            number = input('Увы такого варианта нету. Выберите 1 или 2: ')
    number = int(number.strip())
    print(f'Вы выбрали вариант {number}')
    return number


def correct_number(number, system):
    while True:
        flag = False
        result = all([c in up + dig for c in number.upper()])
        if system.isalpha():
            system = input('Неккоректные данные!Введите систему счисления(целое число от 2 до 36): ')
            continue
        if int(system) not in list(range(2, 37)):
            system = input('Неккоректные данные!Введите систему счисления(целое число от 2 до 36): ')
            continue
        if not result:
            number = input('Неккоректные данные!Число может сожержать только цифры и буквы(a-z): ')
            continue
        if int(system) <= 10:
            while True:
                flag = False
                if any([el.isalpha() for el in number]):
                    number = input('Неккоректные данные!Для системы cчисления меньше 10 число не содержит букв: ')
                    continue
                for elem in number:
                    if int(elem) >= int(system):
                        number = input('Неккоректные данные!Цифры числа не могут превышать систему счисления '
                                      'или равняться ей!Повторите ввод числа: ')
                        break
                else:
                    flag = True
                if flag:
                    break
        else:
            while True:
                flag = False
                for c in number.upper():
                    if ord(c) > ord(d[int(system) - 1]):
                        number = input('Неккоректные данные!Значения числа не могут превышать систему счисле'
                                      'ния!Повторите ввод числа: ')
                        break
                else:
                    flag = True
                if flag:
                    break
        return number, system


def convert_n_to_10(number, system):
    result = 0
    i = 0
    for c in number[::-1]:
        if c in d:
            result += d[c] * int(system) ** i
        else:
            result += int(c) * int(system) ** i
        i += 1
    return result


def convert_10_to_n(number, system):
    result = []
    result_str = ''
    number = int(number)
    while number >= int(system):
        result.append(str(number % int(system)))
        number //= int(system)
    result.append(str(number))
    for c in reversed(result):
        if int(c) in d:
            result_str += d[int(c)]
        else:
            result_str += c
    return result_str


while True:
    print('Калькулятор систем счисления')
    num = input('Выберите один из варинтов(1 - перевод из (2-36)-ричной системы в 10, 2 - '
                'перевод из 10-ричной системы в (2-36)-ричную): ')
    result_num = correct_choice(num)
    if result_num == 1:
        system_number = input('Введите систему счисления из которой будем переводить число: ')
        number = input('Введите число: ')
        result_number, result_system = correct_number(number, system_number)
        print('_' * 101)
        print(f'| Вы выбрали число - {result_number.upper()} и систему счисления - {result_system} '.ljust(100) + '|')
        result = convert_n_to_10(result_number.upper(), result_system)
        print(f'| Число {result_number.upper()} в {result_system} равно {result:_} в 10'.ljust(100) + '|')
        print('-' * 101)
    else:
        system_number = input('Введите систему счисления в которую будем переводить число: ')
        number = input('Введите число: ')
        result_number, result_system = correct_10_number(number), correct_10_system(system_number)
        print('_' * 101)
        print(f'| Вы выбрали число - {result_number} и систему счисления - {result_system} '.ljust(100) + '|')
        result = convert_10_to_n(result_number, result_system)
        print(f'| Число {result_number} в 10 равно {result} в {result_system}'.ljust(100) + '|')
        print('-' * 101)
    output = input('Если желаете покинуть программу, просто напишите EXIT и нажмите ENTER. В противном случае она '
                   'автоматически перезапустится: ')
    if output.strip().upper() == 'EXIT':
        break
    print('_' * 100)