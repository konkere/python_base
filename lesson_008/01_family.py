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
        self.citizens = 0

    def __str__(self):
        return 'В доме еды осталось {}, денег осталось {}, грязи накопилось {}'.format(
            self.food, self.money, self.dirt
        )

    def littering(self):
        self.dirt += 5


class Man:
    total_eaten = 0

    def __init__(self, name):
        self.name = name
        self.fullness = 30
        self.happiness = 100
        self.house = None

    def __str__(self):
        return 'Я — {}, сытость {}, счастье {}'.format(
            self.name, self.fullness, self.happiness
        )

    def eat(self):
        dice_eat = randint(10, 30)
        if self.house.food >= dice_eat:
            cprint('{} кушает {} еды.'.format(self.name, dice_eat), color='yellow')
            self.fullness += dice_eat
            self.house.food -= dice_eat
            Man.total_eaten += dice_eat
        elif 0 < self.house.food < dice_eat:
            cprint('{} кушает {} еды.'.format(self.name, self.house.food), color='yellow')
            self.fullness += self.house.food
            self.house.food = 0
            Man.total_eaten += self.house.food
        else:
            self.fullness -= 10
            cprint('{} не может поесть. Нет еды.'.format(self.name), color='red')

    def very_dirty(self):
        if self.house.dirt > 90:
            self.happiness -= 10
            cprint('В доме очень грязно, {} грустит из-за этого.'.format(self.name), color='red')

    def go_to_the_house(self, house):
        self.house = house
        self.fullness -= 10
        cprint('{} теперь живёт в доме.'.format(self.name), color='cyan')

    def dead(self):
        starvation = (self.fullness <= 0)
        depression = (self.happiness < 10)
        if starvation or depression:
            cprint('{} RIP...'.format(self.name), color='red')
            return True
        return False


class Husband(Man):
    earn_money = 0

    def act(self):
        dice = randint(1, 6)
        if self.fullness <= 20:
            self.eat()
        elif self.house.money < 100 * self.house.citizens:
            self.work()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.gaming()

    def work(self):
        cprint('{} сходил на работу.'.format(self.name), color='blue')
        self.house.money += 150
        self.fullness -= 10
        Husband.earn_money += 150

    def gaming(self):
        cprint('{} играл весь день в плойку.'.format(self.name), color='green')
        self.happiness += 20
        self.fullness -= 10


class Wife(Man):
    bought_fur_coats = 0

    def act(self):
        dice = randint(1, 6)
        if self.fullness <= 20:
            self.eat()
        elif self.house.food <= 30 * self.house.citizens:
            self.shopping()
        elif dice == 1:
            self.eat()
        elif dice == 2:
            self.shopping()
        elif dice == 3:
            self.clean_house()
        else:
            self.buy_fur_coat()

    def shopping(self):
        need_to_buy = 30 * self.house.citizens
        self.fullness -= 10
        if self.house.money >= need_to_buy:
            cprint('{} сходила в магазин за едой, потратив {} денег.'.format(
                self.name, need_to_buy), color='magenta')
            self.house.money -= need_to_buy
            self.house.food += need_to_buy
        elif 0 < self.house.money < need_to_buy:
            cprint('{} сходила в магазин за едой, потратив {} денег.'.format(
                self.name, self.house.money), color='magenta')
            self.house.money -= self.house.money
            self.house.food += self.house.food
        else:
            cprint('Деньги кончились!'.format(self.name), color='red')

    def buy_fur_coat(self):
        self.fullness -= 10
        # TODO как писал ранее на крайние не берем, будет 360 жена купит шубу и на покупку еды уже не будет
        if self.house.money > 350:
            self.happiness += 60
            self.house.money -= 350
            Wife.bought_fur_coats += 1
            cprint('{} купила шубу.'.format(self.name), color='magenta')
        else:
            # TODO не забываем про счастье
            cprint('Не хватило денег на шубу!'.format(self.name), color='red')

    def clean_house(self):
        self.fullness -= 10
        cprint('{} убралась в доме'.format(self.name), color='blue')
        if self.house.dirt >= 100:
            self.house.dirt -= 100
        else:
            self.house.dirt = 0


home = House()
serge = Husband(name='Серёжа')
masha = Wife(name='Маша')

citizens = [serge, masha]

for citizen in citizens:
    citizen.go_to_the_house(house=home)
    home.citizens += 1

death_in_house = False
day_out = 0

for day in range(1, 366):
    cprint('================== День {} =================='.format(day), color='red')
    serge.very_dirty()
    masha.very_dirty()
    serge.act()
    masha.act()
    home.littering()
    cprint(serge, color='cyan')
    cprint(masha, color='cyan')
    cprint(home, color='cyan')
    # Проверим, все ли пережили этот день
    for citizen in citizens:
        if citizen.dead():
            death_in_house = True
    day_out = day
    if death_in_house:
        break

if death_in_house:
    cprint('--============= Мы очень старались, но сумели протянуть только {} дн. =============--'.format(day_out - 1),
           color='green', on_color='on_red')
else:
    cprint('--============= Победа! Мы прожили {} дней! =============--'.format(day_out),
           color='red', on_color='on_green')
cprint('За это время было заработано денег — {}, съедено еды — {}, куплено шуб — {}.'.format(
    Husband.earn_money, Man.total_eaten, Wife.bought_fur_coats), color='green')

# TODO с новыми доработками одни должны жить стабильно 70 на 30 как минимум

# TODO это потом уберите!
exit(0)

######################################################## Часть вторая
#
# После подтверждения учителем первой части надо
# отщепить ветку develop и в ней начать добавлять котов в модель семьи
#
# Кот может:
#   есть,
#   спать,
#   драть обои
#
# Люди могут:
#   гладить кота (растет степень счастья на 5 пунктов)
#
# В доме добавляется:
#   еда для кота (в начале - 30)
#
# У кота есть имя и степень сытости (в начале - 30)
# Любое действие кота, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Еда для кота покупается за деньги: за 10 денег 10 еды.
# Кушает кот максимум по 10 единиц еды, степень сытости растет на 2 пункта за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе кот умрет от голода.
#
# Если кот дерет обои, то грязи становится больше на 5 пунктов


class Cat:

    def __init__(self):
        pass

    def act(self):
        pass

    def eat(self):
        pass

    def sleep(self):
        pass

    def soil(self):
        pass


######################################################## Часть вторая бис
#
# После реализации первой части надо в ветке мастер продолжить работу над семьей - добавить ребенка
#
# Ребенок может:
#   есть,
#   спать,
#
# отличия от взрослых - кушает максимум 10 единиц еды,
# степень счастья  - не меняется, всегда ==100 ;)

class Child:

    def __init__(self):
        pass

    def __str__(self):
        return super().__str__()

    def act(self):
        pass

    def eat(self):
        pass

    def sleep(self):
        pass


# TODO после реализации второй части - отдать на проверку учителем две ветки


######################################################## Часть третья
#
# после подтверждения учителем второй части (обоих веток)
# влить в мастер все коммиты из ветки develop и разрешить все конфликты
# отправить на проверку учителем.


home = House()
serge = Husband(name='Сережа')
masha = Wife(name='Маша')
kolya = Child(name='Коля')
murzik = Cat(name='Мурзик')

for day in range(365):
    cprint('================== День {} =================='.format(day), color='red')
    serge.act()
    masha.act()
    kolya.act()
    murzik.act()
    cprint(serge, color='cyan')
    cprint(masha, color='cyan')
    cprint(kolya, color='cyan')
    cprint(murzik, color='cyan')


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
