import random
from string import digits as dg, ascii_lowercase as low, ascii_uppercase as up, punctuation as pnct


def correct_len_and_cnt(param):
    while True:
        if param.isdigit() and int(param) > 0:
            break
        param = input('А может быть все-таки введем натуральное число: ')
    return int(param)


def correct_input(answ: str):
    return answ.lower().strip() == "y"


def generate_password(cnt: int, length: int, chrs):
    if len(chrs) < length:
        print("Не могу сгенерировать пароль. Количество указанных вами символов меньше заданной длины пароля")
        return
    for _ in range(cnt):
        psw = "".join(random.sample(chrs, length))
        yield psw


ambiguous = "il1Lo0OI"
chars = ""
answer = "y"

while answer.lower().strip() == "y":
    cnt_password = input("Введите количество паролей для генерации: ")
    correct_cnt_passwords = correct_len_and_cnt(cnt_password)
    len_password = input("Введите длину паролей для генерации: ")
    correct_ln_password = correct_len_and_cnt(len_password)
    dig_on = input('Включать ли цифры 0123456789? (y - если да, иначе нет): ')
    if correct_input(dig_on):
        chars += dg
    upp_let_on = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? (y - если да, иначе нет): ')
    if correct_input(upp_let_on):
        chars += up
    low_let_on = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? (y - если да, иначе нет): ')
    if correct_input(low_let_on):
        chars += low
    char_on = input("Включать ли символы !\"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~ (y - если да, иначе нет): ")
    if correct_input(char_on):
        chars += pnct
    exc_on = input('Исключать ли неоднозначные символы il1Lo0OI? (y - если да, иначе нет): ')
    if exc_on:
        chars = "".join(set(chars) - set("il1Lo0OI"))
    print("-" * 50)
    print("Генерация паролей............")
    res = generate_password(correct_cnt_passwords, correct_ln_password, chars)
    for el in res:
        print(el)
    print("-" * 50)
    answer = input("Хотите сгенерировать пароли еще, y - да, иначе - нет: ")
