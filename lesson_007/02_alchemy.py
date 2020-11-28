# -*- coding: utf-8 -*-

# Создать прототип игры Алхимия: при соединении двух элементов получается новый.
# Реализовать следующие элементы: Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
# Каждый элемент организовать как отдельный класс.
# Таблица преобразований:

#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава

# Сложение элементов реализовывать через __add__
# Если результат не определен - то возвращать None
# Вывод элемента на консоль реализовывать через __str__
#
# Примеры преобразований:
#   print(Water(), '+', Air(), '=', Water() + Air())
#   print(Fire(), '+', Air(), '=', Fire() + Air())

class Water:

    def __str__(self):
        return 'Вода'

    def __add__(self, extra_element):
        if isinstance(extra_element, Air):
            return Storm()
        elif isinstance(extra_element, Fire):
            return Steam()
        elif isinstance(extra_element, Earth):
            return Dirt()
        elif isinstance(extra_element, Melange):
            return PrespiceMass()


class Air:

    def __str__(self):
        return 'Воздух'

    def __add__(self, extra_element):
        if isinstance(extra_element, Water):
            return Storm()
        elif isinstance(extra_element, Fire):
            return Lightning()
        elif isinstance(extra_element, Earth):
            return Dust()
        elif isinstance(extra_element, Melange):
            return SpiceGas()


class Fire:

    def __str__(self):
        return 'Огонь'

    def __add__(self, extra_element):
        if isinstance(extra_element, Air):
            return Lightning()
        elif isinstance(extra_element, Water):
            return Steam()
        elif isinstance(extra_element, Earth):
            return Lava()
        elif isinstance(extra_element, Melange):
            return None


class Earth:

    def __str__(self):
        return 'Земля'

    def __add__(self, extra_element):
        if isinstance(extra_element, Air):
            return Dust()
        elif isinstance(extra_element, Fire):
            return Lava()
        elif isinstance(extra_element, Water):
            return Dirt()
        elif isinstance(extra_element, Melange):
            return None


#     \/  https://bit.ly/MelangeDune
class Melange:

    def __str__(self):
        return 'Пряность'

    def __add__(self, extra_element):
        if isinstance(extra_element, Air):
            return SpiceGas()
        elif isinstance(extra_element, Fire):
            return None
        elif isinstance(extra_element, Earth):
            return None
        elif isinstance(extra_element, Water):
            return PrespiceMass()


class Storm:

    def __str__(self):
        return 'Шторм'


class Steam:

    def __str__(self):
        return 'Пар'


class Dirt:

    def __str__(self):
        return 'Грязь'


class Lightning:

    def __str__(self):
        return 'Молния'


class Dust:

    def __str__(self):
        return 'Пыль'


class Lava:

    def __str__(self):
        return 'Лава'


class SpiceGas:

    def __str__(self):
        return 'Пряный газ'


class PrespiceMass:

    def __str__(self):
        return 'Премеланжевая масса'


def user_choice(welcome_txt):
    while True:
        choice_element = input('Введите номер {} элемента: '.format(welcome_txt))
        if choice_element.isdigit() and 0 < int(choice_element) < 6:
            verify_choice_element = int(choice_element) - 1
            return verify_choice_element


first_element = second_element = None

basic_elements = [
    Water(),
    Air(),
    Fire(),
    Earth(),
    Melange(),
]

print('Выбери элемент из списка:')
for number, element in enumerate(basic_elements, start=1):
    print('[{0}] → {1}'.format(number, element))

first_element = user_choice('1-го')
second_element = user_choice('2-го')

print(basic_elements[first_element], '+', basic_elements[second_element], '=',
      basic_elements[first_element] + basic_elements[second_element])

# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.
