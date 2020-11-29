# -*- coding: utf-8 -*-

from random import randint
from termcolor import cprint

# Доработать практическую часть урока lesson_007/python_snippets/08_practice.py

# Необходимо создать класс кота. У кота есть аттрибуты - сытость и дом (в котором он живет).
# Кот живет с человеком в доме.
# Для кота дом характеризируется - миской для еды и грязью.
# Изначально в доме нет еды для кота и нет грязи.

# Доработать класс человека, добавив методы
#   подобрать кота - у кота появляется дом.
#   купить коту еды - кошачья еда в доме увеличивается на 50, деньги уменьшаются на 50.
#   убраться в доме - степень грязи в доме уменьшается на 100, сытость у человека уменьшается на 20.
# Увеличить кол-во зарабатываемых человеком денег до 150 (он выучил пайтон и устроился на хорошую работу :)

# Кот может есть, спать и драть обои - необходимо реализовать соответствующие методы.
# Когда кот спит - сытость уменьшается на 10
# Когда кот ест - сытость увеличивается на 20, кошачья еда в доме уменьшается на 10.
# Когда кот дерет обои - сытость уменьшается на 10, степень грязи в доме увеличивается на 5
# Если степень сытости < 0, кот умирает.
# Так же надо реализовать метод "действуй" для кота, в котором он принимает решение
# что будет делать сегодня

# Человеку и коту надо вместе прожить 365 дней.


class Man:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None

    def __str__(self):
        return 'Я - {}, сытость {}'.format(
            self.name, self.fullness,
        )

    def eat(self):
        if self.house.food >= 10:
            cprint('{} поел'.format(self.name), color='yellow')
            self.fullness += 10
            self.house.food -= 10
        else:
            self.fullness -= 10
            cprint('{} нет еды. Надо идти в магазин.'.format(self.name), color='red')
            self.shopping()

    def work(self):
        cprint('{} сходил на работу'.format(self.name), color='blue')
        self.house.money += 150
        self.fullness -= 10

    def watch_MTV(self):
        cprint('{} смотрел MTV целый день'.format(self.name), color='green')
        self.fullness -= 10

    def shopping(self):
        if self.house.money >= 50:
            cprint('{} сходил в магазин за едой'.format(self.name), color='magenta')
            self.house.money -= 50
            self.house.food += 50
        else:
            cprint('{} деньги кончились! Придётся идти работать.'.format(self.name), color='red')
            self.work()

    def petshopping(self):
        if self.house.money >= 50:
            cprint('{} сходил в зоомагазин за кошачьим кормом'.format(self.name), color='magenta')
            self.house.money -= 50
            self.house.catfood += 50
        else:
            cprint('{} деньги кончились! Придётся идти работать.'.format(self.name), color='red')
            self.work()

    def houseclean(self):
        cprint('{} убрался в доме'.format(self.name), color='blue')
        if self.house.dirt > 99:
            self.house.dirt -= 100
        else:
            self.house.dirt = 0
        self.fullness -= 20

    def shelter_cat(self, cat):
        # забыли сделать проверку
        # А эта проверка для чего? Задел на будущее? При текущем коде self.house всегда будет True
        if self.house:
            cat.house = self.house
            self.fullness -= 10
            cprint('{} подобрал кота и назвал его — {}'.format(self.name, cat.name), color='cyan')

    def go_to_the_house(self, house):
        self.house = house
        self.fullness -= 10
        cprint('{} въехал в дом'.format(self.name), color='cyan')

    def act(self, people, cats):
        dice = randint(1, 6)
        if self.fullness <= 20:
            self.eat()
        elif self.house.food <= 10 * people:
            self.shopping()
        elif self.house.catfood <= 10 * cats:
            self.petshopping()
        elif self.house.money < 50:
            self.work()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        elif dice == 3:
            self.houseclean()
        else:
            self.watch_MTV()

    def dead(self):
        dead = (self.fullness <= 0)
        if dead:
            cprint('{} умер...'.format(self.name), color='red')
        return dead


class Cat:

    def __init__(self, name):
        self.name = name
        self.fullness = 30
        self.house = None

    def __str__(self):
        return 'Я - {}, сытость {}'.format(
            self.name, self.fullness,
        )

    def eat(self):
        if self.house.catfood >= 10:
            cprint('{} поел'.format(self.name), color='yellow')
            self.fullness += 20
            self.house.catfood -= 10
        else:
            cprint('{} нет кошачьего корма! Хотел поесть, но обиделся и пошёл проказничать.'.format(self.name),
                   color='red')
            self.spoil_things()

    def sleep(self):
        self.fullness -= 10
        cprint('{} спал целый день'.format(self.name), color='magenta')

    def spoil_things(self):
        self.fullness -= 10
        self.house.dirt += 5
        cprint('{} весь день драл обои и портил мебель'.format(self.name), color='green')

    def act(self):
        dice = randint(1, 6)
        if self.fullness < 20:
            self.eat()
        elif dice == 1:
            self.spoil_things()
        elif dice == 2:
            self.eat()
        else:
            self.sleep()

    def dead(self):
        dead = (self.fullness <= 0)
        if dead:
            cprint('{} умер...'.format(self.name), color='red')
        return dead


class House:

    def __init__(self):
        self.food = 50
        self.catfood = 0
        self.money = 0
        self.dirt = 0

    def __str__(self):
        return 'В доме еды осталось {}, кошачьего корма осталось {}, денег осталось {}, грязи накопилось {}'.format(
            self.food, self.catfood, self.money, self.dirt
        )


citizens = [
    Man(name='Бивис'),
    Man(name='Батхед'),
    # Man(name='Кенни'),
]

cat_family = [
    Cat(name='Палач'),
    Cat(name='Нюхач'),
    Cat(name='Котозавр'),
    Cat(name='Гарфилд'),
    # Cat(name='Том'),
    # Cat(name='Васька'),
]

cats_in_house = len(cat_family)
citizens_in_house = len(citizens)
death_in_house = False
my_sweet_home = House()

for citizen in citizens:
    citizen.go_to_the_house(house=my_sweet_home)

for cat in cat_family:
    rnd_citizen = randint(0, citizens_in_house - 1)
    citizens[rnd_citizen].shelter_cat(cat)

for day in range(1, 366):
    print('================ день {} =================='.format(day))
    for citizen in citizens:
        citizen.act(citizens_in_house, cats_in_house)
    for cat in cat_family:
        cat.act()
    print('--- в конце дня ---')
    for citizen in citizens:
        print(citizen)
    for cat in cat_family:
        print(cat)
    print(my_sweet_home)
    # Проверим, все ли пережили этот день
    for citizen in citizens:
        if citizen.dead():
            death_in_house = True
    for cat in cat_family:
        if cat.dead():
            death_in_house = True
    if death_in_house:
        break
if death_in_house:
    cprint('--============= Мы очень старались, но сумели протянуть только {} дн. =============--'.format(day - 1),
           color='green', on_color='on_red')
else:
    cprint('--============= Победа! Мы прожили {} дней! =============--'.format(day),
           color='red', on_color='on_green')



# Усложненное задание (делать по желанию)
# Создать несколько (2-3) котов и подселить их в дом к человеку.
# Им всем вместе так же надо прожить 365 дней.

# (Можно определить критическое количество котов, которое может прокормить человек...)
