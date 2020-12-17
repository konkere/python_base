# -*- coding: utf-8 -*-
from termcolor import cprint
from random import randint

######################################################## Часть первая
#
# Создать модель жизни небольшой семьи.
#
# Каждый день участники жизни могут делать только одно действие.
# Все вместе они должны прожить год и не умереть.
#
# Муж может:
#   есть,
#   играть в WoT,
#   ходить на работу,
# Жена может:
#   есть,
#   покупать продукты,
#   покупать шубу,
#   убираться в доме,

# Все они живут в одном доме, дом характеризуется:
#   кол-во денег в тумбочке (в начале - 100)
#   кол-во еды в холодильнике (в начале - 50)
#   кол-во грязи (в начале - 0)
#
# У людей есть имя, степень сытости (в начале - 30) и степень счастья (в начале - 100).
#
# Любое действие, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Кушают взрослые максимум по 30 единиц еды, степень сытости растет на 1 пункт за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе чел умрет от голода.
#
# Деньги в тумбочку добавляет муж, после работы - 150 единиц за раз.
# Еда стоит 10 денег 10 единиц еды. Шуба стоит 350 единиц.
#
# Грязь добавляется каждый день по 5 пунктов, за одну уборку жена может убирать до 100 единиц грязи.
# Если в доме грязи больше 90 - у людей падает степень счастья каждый день на 10 пунктов,
# Степень счастья растет: у мужа от игры в WoT (на 20), у жены от покупки шубы (на 60, но шуба дорогая)
# Степень счастья не должна падать ниже 10, иначе чел умирает от депрессии.
#
# Подвести итоги жизни за год: сколько было заработано денег, сколько сьедено еды, сколько куплено шуб.


class House:

    def __init__(self):
        self.money = 100
        self.food = 50
        self.dirt = 0
        self.adult_citizens = 0
        self.children = 0
        self.cats = 0
        self.catfood = 30

    def littering(self):
        self.dirt += 5


class Man:
    total_eaten = 0

    def __init__(self, name):
        self.name = name
        self.fullness = 30
        self.happiness = 100
        self.house = None
        self.to_eat = [10, 30]

    def eat(self):
        dice_eat = randint(*self.to_eat)
        if self.house.food >= dice_eat:
            self.fullness += dice_eat
            self.house.food -= dice_eat
            Man.total_eaten += dice_eat
        elif 0 < self.house.food < dice_eat:
            self.fullness += self.house.food
            self.house.food = 0
            Man.total_eaten += self.house.food
        else:
            self.fullness -= 10

    def pet_the_cat(self):
        self.happiness += 5
        self.fullness -= 10

    def very_dirty(self):
        if self.house.dirt > 90:
            self.happiness -= 10

    def go_to_the_house(self, house):
        self.house = house
        self.fullness -= 10

    def shelter_cat(self, cat):
        if self.house:
            cat.house = self.house
            # self.fullness -= 10

    def dead(self):
        starvation = (self.fullness <= 0)
        depression = (self.happiness < 10)
        if starvation or depression:
            return True
        return False


class Husband(Man):
    earn_money = 0

    def __init__(self, salary, name):
        super().__init__(name)
        self.salary = salary

    def act(self):
        dice = randint(1, 6)
        if self.fullness <= 20:
            self.eat()
        elif self.house.money < 30 * self.house.adult_citizens + 10 * (self.house.children + self.house.cats):
            self.work()
        elif self.house.catfood < 10 * self.house.cats:
            self.petshopping()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        elif dice == 3:
            self.pet_the_cat()
        else:
            self.gaming()

    def work(self):
        self.house.money += self.salary
        self.fullness -= 10
        Husband.earn_money += self.salary

    def gaming(self):
        self.happiness += 20
        self.fullness -= 10

    def petshopping(self):
        if self.house.money >= 10 * self.house.cats:
            self.fullness -= 10
            self.house.money -= 10 * self.house.cats
            self.house.catfood += 10 * self.house.cats
        else:
            self.work()


class Wife(Man):
    bought_fur_coats = 0

    def act(self):
        dice = randint(1, 6)
        if self.fullness <= 20:
            self.eat()
        elif self.house.food <= 30 * self.house.adult_citizens + 10 * self.house.children:
            self.shopping()
        elif self.house.dirt > 90:
            self.clean_house()
        elif dice == 1:
            self.eat()
        elif dice == 2:
            self.shopping()
        elif dice == 3:
            self.clean_house()
        elif dice == 4:
            self.pet_the_cat()
        else:
            self.buy_fur_coat()

    def shopping(self):
        need_to_buy = 30 * self.house.adult_citizens + 10 * self.house.children
        self.happiness += 10
        self.fullness -= 10
        if self.house.money >= need_to_buy:
            self.house.money -= need_to_buy
            self.house.food += need_to_buy
        elif 0 < self.house.money < need_to_buy:
            self.house.money -= self.house.money
            self.house.food += self.house.food

    def buy_fur_coat(self):
        self.fullness -= 10
        if self.house.money >= 350 + self.house.adult_citizens * 30 + self.house.children * 10:
            self.happiness += 60
            self.house.money -= 350
            Wife.bought_fur_coats += 1
        else:
            self.happiness -= 10

    def clean_house(self):
        self.fullness -= 10
        if self.house.dirt >= 100:
            self.house.dirt -= 100
        else:
            self.house.dirt = 0


class Child(Man):

    def __init__(self, name):
        super().__init__(name=name)
        self.to_eat = [1, 10]

    def act(self):
        dice = randint(1, 2)
        if self.fullness <= 10:
            self.eat()
        elif dice == 1:
            self.sleep()
        elif dice == 2:
            self.eat()

    def sleep(self):
        self.fullness -= 10


class Cat:
    total_eaten = 0

    def __init__(self, name):
        self.name = name
        self.fullness = 30
        self.house = None

    def eat(self):
        dice_eat = randint(1, 10)
        if self.house.catfood >= dice_eat:
            self.fullness += dice_eat * 2
            self.house.catfood -= dice_eat
            Cat.total_eaten += dice_eat
        elif 0 < self.house.catfood < dice_eat:
            self.fullness += self.house.catfood * 2
            self.house.catfood = 0
            Cat.total_eaten += self.house.catfood
        else:
            self.spoil_things()

    def sleep(self):
        self.fullness -= 10

    def spoil_things(self):
        self.fullness -= 10
        self.house.dirt += 5

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
        return self.fullness <= 0


class Simulation:

    def __init__(self, money_incidents, food_incidents, salary):
        self.home = House()
        self.cat_family = []
        self.salary = salary
        self.adult_citizens = [
            Husband(name='Серёжа', salary=self.salary),
            Wife(name='Маша'),
        ]
        self.children = [
            Child(name='Коля'),
        ]
        self.citizens = self.adult_citizens + self.children
        self.death_in_house = False
        self.day_out = 0
        self.days_for_half_money = self.uniq_days_generate(money_incidents)
        self.days_for_half_food = self.uniq_days_generate(food_incidents)

    def purge_life(self, money_incidents, food_incidents, salary):
        self.salary = salary
        self.home.money = 100
        self.home.food = 50
        self.home.dirt = 0
        self.home.catfood = 30
        self.home.adult_citizens = 0
        self.home.children = 0
        self.home.cats = 0
        self.death_in_house = False
        self.day_out = 0
        self.days_for_half_money = self.uniq_days_generate(money_incidents)
        self.days_for_half_food = self.uniq_days_generate(food_incidents)
        for citizen in self.citizens:
            citizen.fullness = 30
            citizen.happiness = 100

    def cats_generate(self, cats):
        cats_family = []
        for cat in range(cats):
            cats_family.append(Cat(cat))
        return cats_family

    def uniq_days_generate(self, quantity):
        days = []
        if quantity == 0:
            return days
        while quantity > len(days):
            day = randint(1, 365)
            if day not in days:
                days.append(day)
        return days

    def incident_half_money(self, day):
        if day in self.days_for_half_money:
            self.home.money = int(self.home.money / 2)

    def incident_half_food(self, day):
        if day in self.days_for_half_food:
            self.home.food = int(self.home.food / 2)

    def housewarming(self):
        for citizen in self.adult_citizens:
            citizen.go_to_the_house(house=self.home)
            self.home.adult_citizens += 1
        for citizen in self.children:
            citizen.go_to_the_house(house=self.home)
            self.home.children += 1
        for cat in self.cat_family:
            rnd_citizen = randint(0, self.home.adult_citizens - 1)
            self.adult_citizens[rnd_citizen].shelter_cat(cat)
            self.home.cats += 1

    def experiment(self):
        for cats in range(30, 0, -1):
            survival = 0
            for _ in range(3):
                self.purge_life(money_incidents, food_incidents, self.salary)
                self.cat_family = self.cats_generate(cats)
                self.housewarming()
                if self.survive_one_year():
                    survival += 1
                    if survival == 2:
                        return cats
        return 0

    def survive_one_year(self):
        for day in range(1, 366):
            self.incident_half_money(day)
            self.incident_half_food(day)
            for citizen in self.adult_citizens:
                citizen.very_dirty()
            for citizen in self.citizens:
                citizen.act()
            for cat in self.cat_family:
                cat.act()
            self.home.littering()
            for citizen in self.citizens:
                if citizen.dead():
                    self.death_in_house = True
            for cat in self.cat_family:
                if cat.dead():
                    self.death_in_house = True
            self.day_out = day
            if self.death_in_house:
                return False
        return not self.death_in_house


for food_incidents in range(6):
    for money_incidents in range(6):
        cprint('----- Инцидентов за год с пропажей денег: {}, еды: {} -----'.format(money_incidents, food_incidents),
               color='red', on_color='on_green')
        for salary in range(50, 401, 50):
            life = Simulation(money_incidents, food_incidents, salary)
            max_cats = life.experiment()
            print('При зарплате {} получилось прокормить {} котов'.format(salary, max_cats))


# Усложненное задание (делать по желанию)
#
# Сделать из семьи любителей котов - пусть котов будет 3, или даже 5-10.
# Коты должны выжить вместе с семьей!
#
# Определить максимальное число котов, которое может прокормить эта семья при значениях зарплаты от 50 до 400.
# Для сглаживание случайностей моделирование за год делать 3 раза, если 2 из 3х выжили - считаем что выжили.
#
# Дополнительно вносить некий хаос в жизнь семьи
# - N раз в год вдруг пропадает половина еды из холодильника (коты?)
# - K раз в год пропадает половина денег из тумбочки (муж? жена? коты?!?!)
# Промоделировать - как часто могут случаться фейлы что бы это не повлияло на жизнь героев?
#   (N от 1 до 5, K от 1 до 5 - нужно вычислит максимумы N и K при котором семья гарантированно выживает)
#
# в итоге должен получится приблизительно такой код экспериментов
# for food_incidents in range(6):
#   for money_incidents in range(6):
#       life = Simulation(money_incidents, food_incidents)
#       for salary in range(50, 401, 50):
#           max_cats = life.experiment(salary)
#           print(f'При зарплате {salary} максимально можно прокормить {max_cats} котов')
