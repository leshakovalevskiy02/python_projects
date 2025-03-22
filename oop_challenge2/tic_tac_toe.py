class CellFillingError(Exception):
    """Ошибка заполнения клетки уже другим значением"""


class Cell:
    def __init__(self):
        self.value = 0

    def __bool__(self):
        return self.value == 0


class TicTacToe:
    FREE_CELL = 0  # свободная клетка
    HUMAN_X = 1  # крестик (игрок - человек)
    COMPUTER_O = 2  # нолик (игрок - компьютер)

    def __init__(self):
        self.init()

    def init(self):
        self.pole = tuple([tuple([Cell() for j in range(3)]) for i in range(3)])

    def __correct_index(self, ind):
        i, j = ind
        if not 0 <= i <= 2 or not 0 <= j <= 2:
            raise IndexError('некорректно указанные индексы')

    def __getitem__(self, key):
        self.__correct_index(key)
        i, j = key
        return self.pole[i][j].value

    def __setitem__(self, key, value):
        self.__correct_index(key)
        i, j = key
        if self[i, j] != self.FREE_CELL:
            raise CellFillingError("Данная клетка занята, выберите другую")
        self.pole[i][j].value = value

    def show(self):
        for row in self.pole:
            for col in row:
                if col.value == self.FREE_CELL:
                    print(".".rjust(3), end="")
                if col.value == self.HUMAN_X:
                    print("x".rjust(3), end="")
                if col.value == self.COMPUTER_O:
                    print("o".rjust(3), end="")
            print()
        print()

    def go_game(self, value):
        while True:
            try:
                i, j = map(int, input("Введите 2 координаты: ").split())
                self[i, j] = value
            except CellFillingError as c:
                print(c)
            except IndexError as i:
                print(i)
            except ValueError:
                print("Введите правильно 2 координаты(целые числа)")
            else:
                break

    def human_go(self):
        self.go_game(self.HUMAN_X)

    def computer_go(self):
        self.go_game(self.COMPUTER_O)

    def generate_wins_positions(self):
        wins_positions = list(self.pole)
        wins_positions += [el for el in zip(*self.pole)]
        l1, l2 = [], []
        for i in range(3):
            for j in range(3):
                if i == j:
                    l1.append(self.pole[i][i])
                if i == 3 - 1 - j:
                    l2.append(self.pole[i][j])
        wins_positions.append(tuple(l1))
        wins_positions.append(tuple(l2))
        return wins_positions

    @property
    def is_human_win(self):
        wins_pos = self.generate_wins_positions()
        for pos in wins_pos:
            cnt = 0
            for el in pos:
                if el.value == self.HUMAN_X:
                    cnt += 1
            if cnt == 3:
                return True
        return False

    @property
    def is_computer_win(self):
        wins_pos = self.generate_wins_positions()
        for pos in wins_pos:
            cnt = 0
            for el in pos:
                if el.value == self.COMPUTER_O:
                    cnt += 1
            if cnt == 3:
                return True
        return False

    @property
    def is_draw(self):
        wins_pos = self.generate_wins_positions()
        for pos in wins_pos:
            for el in pos:
                if el:
                    return True
        return False

    def __bool__(self):
        return not (self.is_human_win or self.is_computer_win) and self.is_draw


game = TicTacToe()
game.init()
step_game = 0
while game:
    game.show()

    if step_game % 2 == 0:
        game.human_go()
    else:
        game.computer_go()

    step_game += 1

game.show()

if game.is_human_win:
    print("Поздравляем! Вы победили!")
elif game.is_computer_win:
    print("Все получится, со временем")
else:
    print("Ничья.")