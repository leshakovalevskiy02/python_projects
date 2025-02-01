import random


def correct_range(par):
    range_n = input(f"Введите {par} границу диапазона: ")
    while True:
        if range_n.isdigit():
            break
        range_n = input('А может быть все-таки введем целое число: ')
    range_n = int(range_n)
    return range_n


def is_valid(number: str, lf, r):
    return number.isdigit() and lf <= int(number) <= r


def correct_input(lf, r):
    number = input(f"Введите целое число от {lf} до {r}: ")
    while True:
        if is_valid(number, lf, r):
            break
        print(f'А может быть все-таки введем целое число от {lf} до {r}? ')
        number = input(f"Введите целое число от {lf} до {r}: ")
    number = int(number)
    return number


def correct_ending(count):
    if count % 10 == 1 and count % 100 != 11:
        return "ка"
    elif count % 10 in (2, 3, 4) and count % 100 not in (12, 13, 14):
        return "ки"
    else:
        return "ок"


answer = "y"
while answer.lower().strip() == "y":
    print('Добро пожаловать в числовую угадайку')
    lst = ("первую", "вторую")
    range_l = correct_range(lst[0])
    range_r = correct_range(lst[1])
    if range_l > range_r:
        range_l, range_r = range_r, range_l
    print(f"Левая граница диапазона - {range_l}, правая граница диапазона - {range_r}")

    correct_number = random.randint(range_l, range_r)
    num = correct_input(range_l, range_r)
    cnt = 1

    while num != correct_number:
        cnt += 1
        print(f"Вы ввели число - {num}")
        if num > correct_number:
            print("Ваше число больше загаданного, попробуйте еще разок")
            num = correct_input(range_l, range_r)
        elif num < correct_number:
            print('Ваше число меньше загаданного, попробуйте еще разок')
            num = correct_input(range_l, range_r)

    print(f'Вы угадали, поздравляем! Было потачено - {cnt} {"попыт" + correct_ending(cnt)}')
    print("Спасибо, что играли в числовую угадайку. Еще увидимся...")
    print("_" * 50)
    answer = input("Нажмите \"y\" и нажмите ENTER, если хотите сыграть снова: ")