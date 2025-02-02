import random


def is_valid_name(n: str) -> bool:
    return len(n) != 0


def set_correct_name() -> str:
    name = input('Введите ваше имя: ')
    while True:
        if is_valid_name(name):
            break
        name = input('Вы ничего не ввели...Попробуйте еще раз: ')
    return name


def is_valid_question(q: str) -> bool:
    return len(q) != 0


def set_correct_question() -> str:
    q = input('Введите ваш вопрос: ')
    while True:
        if is_valid_question(q):
            break
        q = input('Вы не задали вопрос,попробуйте еще раз: ')
    return q


answers = ['Бесспорно', 'Предрешено', 'Никаких сомнений', 'Определенно да', 'Может быть уверен в этом',
           'Мне кажется-да', 'Вероятнее всего', 'Хорошие перспективы', 'Знаки говорят-да', 'Да',
           'Пока неясно,попробуй снова', 'Спроси позже', 'Лучше не рассказывать', 'Сейчас нельзя предсказать',
           'Сконцентрируйся и спроси опять', 'Даже не думай', 'Мой ответ-нет', 'По моим данным-нет',
           'Перспективы не очень хорошие', 'Весьма сомнительно']

print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.')
correct_name = set_correct_name()
print(f'Привет {correct_name.strip()}!')

while True:
    question = set_correct_question()
    print(f"Вы задали вопрос - {question.strip()}")
    print(f"Ответ магического шара - {random.choice(answers)}")
    s = input('Хотите задать еще вопрос: введите "y", и нажмите ENTER если хотите: ')
    if s.lower().strip() != 'y':
        print('Возвращайся если возникнут вопросы!!!')
        break
