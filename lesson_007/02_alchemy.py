# -*- coding: utf-8 -*-

# Создать прототип игры Алхимия: при соединении двух элементов получается новый.
# Реализовать следующие элементы: Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
# Каждый элемент организовать как отдельный класс.
# Таблица преобразований:

# TODO у нас должно быть на много больше классов-элементов
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
        if extra_element is element_air:
            return 'Шторм'
        elif extra_element is element_fire:
            return 'Пар'
        elif extra_element is element_earth:
            return 'Грязь'
        elif extra_element is element_melange:
            return 'Премеланжевая масса'


class Air:

    def __str__(self):
        return 'Воздух'

    def __add__(self, extra_element):
        # TODO поробуйте переписать логику так чтобы воспользоваться функцией isinstance()
        if extra_element is element_water:
            # TODO а возвращать не строку а сам класс Шторм() в котором будет определен метод str
            return 'Шторм'
        elif extra_element is element_fire:
            return 'Молния'
        elif extra_element is element_earth:
            return 'Пыль'
        elif extra_element is element_melange:
            return 'Пряный газ'


class Fire:

    def __str__(self):
        return 'Огонь'

    def __add__(self, extra_element):
        if extra_element is element_air:
            return 'Молния'
        elif extra_element is element_water:
            return 'Пар'
        elif extra_element is element_earth:
            return 'Лава'
        elif extra_element is element_melange:
            return None


class Earth:

    def __str__(self):
        return 'Земля'

    def __add__(self, extra_element):
        if extra_element is element_air:
            return 'Пыль'
        elif extra_element is element_fire:
            return 'Лава'
        elif extra_element is element_water:
            return 'Грязь'
        elif extra_element is element_melange:
            return None


#     \/  https://bit.ly/MelangeDune
class Melange:

    def __str__(self):
        return 'Пряность'

    def __add__(self, extra_element):
        if extra_element is element_air:
            return 'Пряный газ'
        elif extra_element is element_fire:
            return None
        elif extra_element is element_earth:
            return None
        elif extra_element is element_water:
            return 'Премеланжевая масса'


def user_choice(welcome_txt):
    while True:
        choice_element = input('Введите номер {} элемента: '.format(welcome_txt))
        if choice_element.isdigit() and 0 < int(choice_element) < 6:
            verify_choice_element = int(choice_element) - 1
            return verify_choice_element


first_element = second_element = None


element_water = Water()
element_air = Air()
element_fire = Fire()
element_earth = Earth()
element_melange = Melange()

elements = [
    element_water,
    element_air,
    element_fire,
    element_earth,
    element_melange
]

print('Выбери элемент из списка:')
for number, element in enumerate(elements, start=1):
    print('[{0}] → {1}'.format(number, element))

first_element = user_choice('1-го')
second_element = user_choice('2-го')

print(elements[first_element], '+', elements[second_element], '=',
      elements[first_element] + elements[second_element])

# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.
