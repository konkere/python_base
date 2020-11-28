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
            cprint('{} нет еды'.format(self.name), color='red')

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
            # TODO информируем а то консоль будет пустой
            # Пустой не будет, он же работать пойдёт, если денег не хватает.
            cprint('{} деньги кончились! Придётся идти работать.'.format(self.name), color='red')
            self.work()

    def houseclean(self):
        cprint('{} убрался в доме'.format(self.name), color='blue')
        if self.house.dirt > 99:
            self.house.dirt -= 100
        else:
            self.house.dirt = 0
        self.fullness -= 20

    def shelter_cat(self, cats, max_cats):
        if cats < max_cats:
            pickup_cat = cat_family[cats]
            pickup_cat.house = self.house
            pickup_cat.fullness -= 10
            cprint('{} подобрал кота и назвал его — {}'.format(self.name, pickup_cat.name), color='cyan')
            cats += 1
            return cats

    def go_to_the_house(self, house):
        self.house = house
        self.fullness -= 10
        cprint('{} въехал в дом'.format(self.name), color='cyan')

    def act(self, people, cats, max_cats):
        dice = randint(1, 6)
        if self.fullness <= 20:
            self.eat()
        elif self.house.food < 10 * people:
            self.shopping()
        elif cats > 0 and self.house.catfood < 10 * cats:
            self.petshopping()
        elif self.house.money < 50:
            self.work()
        elif self.house.dirt >= 200:
            self.houseclean()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        elif cats < max_cats and dice == 3:
            cats=self.shelter_cat(cats, max_cats)
        elif self.house.dirt > 0 and dice == 4:
            self.houseclean()
        else:
            self.watch_MTV()
        return cats

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
    # Cat(name='Васька')
]

cats_in_house = 0
max_cats_in_house = len(cat_family)
citizens_in_house = len(citizens)

my_sweet_home = House()
for citisen in citizens:
    citisen.go_to_the_house(house=my_sweet_home)

# TODO заселяем котов также как людей через цикл
# Всех? За раз? В первый же день? Это же как-то совсем не правдоподобно.

for day in range(1, 366):
    print('================ день {} =================='.format(day))
    for citisen in citizens:
        if not citisen.dead():
            cats_in_house = citisen.act(citizens_in_house, cats_in_house, max_cats_in_house)
    for cat in cat_family:
        # TODO эта проверка должна уйти
        # Если не будем вселять всех котов за раз, то придётся проверять, в доме ли они уже.
        if cat.house and not cat.dead():
            cat.act()
    print('--- в конце дня ---')
    for citisen in citizens:
        print(citisen)
    for cat in cat_family:
        if cat.house:
            print(cat)
    print(my_sweet_home)

# Усложненное задание (делать по желанию)
# Создать несколько (2-3) котов и подселить их в дом к человеку.
# Им всем вместе так же надо прожить 365 дней.

# (Можно определить критическое количество котов, которое может прокормить человек...)
