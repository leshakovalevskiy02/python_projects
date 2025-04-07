from random import randint, choice
from copy import deepcopy

class RetrySelectionPlayerException(Exception):
    """Ошибка, если пользователь укажет недоступную координату"""
    pass


class Ship:
    def __init__(self, length, tp=1, x=None, y=None, pole_size=10):
        """
        self._size - размер игрового поля
        self._length - длина коробля
        self._tp - ориентация коробля
        self._is_move - возможность или невозможность корабля двигаться(True или False)
        self._cells - состояние ячеек корабля, 1 - не попали, 2 - попали
        """
        self._size = pole_size
        self._length = length
        self._tp = tp
        self._is_move = True
        self._cells = [1] * length
        self.set_start_coords(x, y)
        
    def set_start_coords(self, x, y):
        """
        Установка начальных координат, если не указаны, то получение случайных, с учетом размеров поля
        """
        if x is None:
            if self._tp == 1:
                x = randint(0, self._size - self._length)
            else:
                x = randint(0, self._size - 1)
        if y is None:
            if self._tp == 1:
                y = randint(0, self._size - 1)
            else:
                y = randint(0, self._size - self._length)
        self._x = x
        self._y = y
        
    def get_start_coords(self):
        return self._x, self._y
        
    def move(self, go):
        """Перемещение корабля в зависимости от ориентации"""
        if self._is_move:
            if self._tp == 1:
                self._x += go
            else:
                self._y += go
    
    @staticmethod                
    def _get_coords_around_ship(ship):
        """
        Получение координат клеток воды вокруг корабля
        """
        coords = set()
        x, y = ship.get_start_coords()
        if ship._tp == 1:
            x_end = x + ship._length - 1
            for x_coord in range(x, x_end + 1):
                coords.update([(x_coord, y - 1), (x_coord, y + 1)])
            for y_coord in range(y - 1, y + 2):
                coords.update([(x - 1, y_coord),(x_end + 1, y_coord)])
        else:
            y_end = y + ship._length - 1
            for y_coord in range(y, y_end + 1):
                coords.update([(x - 1, y_coord), (x + 1, y_coord)])
            for x_coord in range(x - 1, x + 2):
                coords.update([(x_coord, y - 1),(x_coord, y_end + 1)])
        return coords
        
    def _get_ship_coords(self):
        """Получение координат корабля"""
        coords = set()
        x, y  = self.get_start_coords()
        if self._tp == 1:
            for x_coord in range(x, x + self._length):
                coords.add((x_coord, y))
        else:
            for y_coord in range(y, y + self._length):
                coords.add((x, y_coord))
        return coords
        
    def is_collide(self, ship):
        """Проверка на пересечение 2 кораблей"""
        coords = self._get_coords_around_ship(ship)
        coords2 = ship._get_ship_coords()
        coords3 = self._get_ship_coords()
        
        return coords.union(coords2).intersection(coords3) != set()                   
        
    def is_out_pole(self, size):
        """Проверка выхода коробля за границы поля"""
        if self._tp == 1 and (self._x < 0 or self._x + self._length > size):
            return True
        if self._tp == 2 and (self._y < 0 or self._y + self._length > size):
            return True
        return False
    
    def __getitem__(self, key):
        return self._cells[key]
        
    def __setitem__(self, key, value):
        self._cells[key] = value
        
        
class GamePole:
    def __init__(self, size=10):
        """
        self._size - размер поля
        self._ships - массив, хранящий корабли
        self._array - массив, хранящий состояние клеток, 0 - вода, 1 - неподстреленный корабль
        2 - подстреленный корабль
        """
        self._size = size
        self._ships = []
        self._array = [[0] * size for _ in range(size)]
        
    def _update_pole(self):
        """Изменение массива состояния клеток"""
        self._array[:] = [[0] * self._size for _ in range(self._size)]
        for ship in self._ships:
            coords = ship._get_ship_coords()
            for i, coord in enumerate(sorted(coords)):
                x, y = coord
                self._array[y][x] = ship[i]
        
    def init(self):
        ships = [Ship(4, randint(1, 2), pole_size=self._size), Ship(3, randint(1, 2), pole_size=self._size), Ship(3, randint(1, 2), pole_size=self._size), Ship(2, randint(1, 2), pole_size=self._size), Ship(2, randint(1, 2), pole_size=self._size), Ship(2, randint(1, 2), pole_size=self._size), Ship(1, randint(1, 2), pole_size=self._size), Ship(1, randint(1, 2), pole_size=self._size), Ship(1, randint(1, 2), pole_size=self._size), Ship(1, randint(1, 2), pole_size=self._size)]
        
        i = 0
        count = 0 # Количество попыток составить поле
        while i < len(ships) and count < 1500:
            for added_ship in self._ships:
                if ships[i] is not added_ship and ships[i].is_collide(added_ship):
                    count += 1
                    ships[i] = Ship(ships[i]._length, ships[i]._tp, pole_size=ships[i]._size)
                    break
            else:
                self._ships.append(ships[i])
                i += 1
        if count == 1500:
            print("Не удалось создать игровое поле. Возможно нужно увеличить его размер")
            self._ships[:] = []
        
        self._update_pole()
        
    def get_ships(self):
        return self._ships
        
    def show(self):
        for row in self.get_pole():
            for el in row:
                print(el, end=" ")
            print()
        
    def get_pole(self):
        return tuple(tuple(row) for row in self._array)
    
    def move_ships(self):
        """Передвижение короблей, которые не подстреляны, вверх/вниз, влево/вправо 
        в зависимости от ориентации"""
        for ship in self._ships:
            shifts = [-1, 1]
            while shifts:
                shift = choice(shifts)
                shifts.remove(shift)
                ship.move(shift)
                for another_ship in self._ships:
                    if another_ship is not ship and ship.is_collide(another_ship):
                        ship.move(-shift)
                        break
                else:
                    if ship.is_out_pole(self._size):
                        ship.move(-shift)
                    else:
                        break
        self._update_pole()
        
    
class SeaBattle:
    _instance = None
    _players = 2
    
    def __new__(cls, *args, **kwargs):
        """Создание только 2 экземпяляров поля"""
        if cls._players > 0:
            cls._players -= 1
            cls._instance = super().__new__(cls)
        return cls._instance
        
    def __del__(self):
        type(self)._players += 1
        if self._players == 2:
            type(self)._instance = None 
        
    def __init__(self, name, size=10):
        self.name = name
        self._size = size
        self.player_pole = GamePole(size)
        self.player_pole.init()
        self.player_ships = self.player_pole.get_ships()[:]
        self.all_coords = {(i, j) for i in range(size) for j in range(size)}
        self.player_allowed_coords = self.all_coords.copy()
        self.hit_coords = set()
    
    def shoot_by_enemy_pole(self, enemy_pole, x, y):
        """Логика стрельбы по координате"""
        if x < 0 or x >= self._size or y < 0 or y >= self._size:
            raise IndexError(f"Координаты должны быть внутри поля (от 0 до {self._size - 1})")
        if (x, y) not in self.player_allowed_coords:
            raise RetrySelectionPlayerException("Эту координату вы уже выбирали или эта координата гарантированно вода. Попробуйте другую!!!")
        self.player_allowed_coords.remove((x, y))
        ship_target_flag = False
        for ship in enemy_pole.player_ships:
            for i, coord in enumerate(sorted(ship._get_ship_coords())):
                if coord == (x, y):
                    ship._is_move = False
                    ship[i] = 2
                    ship_target_flag = True
                    self.hit_coords.add(coord)
                    print("Вы попали в корабль")
                    break
            if all([item == 2 for item in ship]):
                enemy_pole.player_ships.remove(ship)
                self.player_allowed_coords.difference_update(ship._get_coords_around_ship(ship))
                print("Ура!!! Вы убили корабль!!!")
            if ship_target_flag:
                enemy_pole.player_pole._update_pole()
                return ship_target_flag
        return ship_target_flag
    
    def show_selected_coords(self):
        for i in range(self._size):
            for j in range(self._size):
                if (j, i) in self.player_allowed_coords:
                    print("□", end=" ")
                elif (j, i) in self.hit_coords:
                    print("✕", end=" ")
                else:
                    print(".", end=" ")
            print()
            
    def move_ships_after_shoot(self, second_player):
        """Движение кораблей противника, после промаха по ним"""
        second_player_pole_copy = deepcopy(second_player.player_pole)
        second_player.player_pole.move_ships()
        new_coords = set()
        for ship in second_player.player_pole.get_ships():
            new_coords.update(ship._get_ship_coords())
        st = new_coords.intersection(self.all_coords - self.player_allowed_coords - self.hit_coords)
        if st != set():
            second_player.player_pole = second_player_pole_copy
        
if __name__ == "__main__":
    # Создание игрового поля и цикл игры
    size = 10
    first_player = SeaBattle(input("Введите имя первого игрока: "), size=size)
    second_player = SeaBattle(input("Введите имя второго игрока: "), size=size)

    while not first_player.player_pole.get_ships():
        first_player = SeaBattle(input("Введите имя первого игрока: "), size=size)
        
    while not second_player.player_pole.get_ships():
        second_player = SeaBattle(input("Введите имя второго игрока: "), size=size)
        
    print(f"Ходит {first_player.name}")
    while first_player.player_ships and second_player.player_ships:
        first_player.show_selected_coords()
        try:
            x, y = map(int, input("Введите координаты поля по оси x и y: ").split())
            result = first_player.shoot_by_enemy_pole(second_player, x, y)
            if result:
                continue
            print("К сожалению, вы промазали:(...Переход хода...")
            first_player.move_ships_after_shoot(second_player)
            first_player, second_player = second_player, first_player
            print(f"Ходит {first_player.name}")
        except ValueError:
            print("Введите 2 числа!!!")
        except Exception as e:
            print(e)
    print(f"Игра окончена. Победил - {first_player.name}")