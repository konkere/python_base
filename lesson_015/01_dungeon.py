# -*- coding: utf-8 -*-

# Подземелье было выкопано ящеро-подобными монстрами рядом с аномальной рекой, постоянно выходящей из берегов.
# Из-за этого подземелье регулярно затапливается, монстры выживают, но не герои, рискнувшие спуститься к ним в поисках
# приключений.
# Почуяв безнаказанность, ящеры начали совершать набеги на ближайшие деревни. На защиту всех деревень не хватило
# солдат и вас, как известного в этих краях героя, наняли для их спасения.
#
# Карта подземелья представляет собой json-файл под названием rpg.json. Каждая локация в лабиринте описывается объектом,
# в котором находится единственный ключ с названием, соответствующем формату "Location_<N>_tm<T>",
# где N - это номер локации (целое число), а T (вещественное число) - это время,
# которое необходимо для перехода в эту локацию. Например, если игрок заходит в локацию "Location_8_tm30000",
# то он тратит на это 30000 секунд.
# По данному ключу находится список, который содержит в себе строки с описанием монстров а также другие локации.
# Описание монстра представляет собой строку в формате "Mob_exp<K>_tm<M>", где K (целое число) - это количество опыта,
# которое получает игрок, уничтожив данного монстра, а M (вещественное число) - это время,
# которое потратит игрок для уничтожения данного монстра.
# Например, уничтожив монстра "Boss_exp10_tm20", игрок потратит 20 секунд и получит 10 единиц опыта.
# Гарантируется, что в начале пути будет две локации и один монстр
# (то есть в коренном json-объекте содержится список, содержащий два json-объекта, одного монстра и ничего больше).
#
# На прохождение игры игроку дается 123456.0987654321 секунд.
# Цель игры: за отведенное время найти выход ("Hatch")
#
# По мере прохождения вглубь подземелья, оно начинает затапливаться, поэтому
# в каждую локацию можно попасть только один раз,
# и выйти из нее нельзя (то есть двигаться можно только вперед).
#
# Чтобы открыть люк ("Hatch") и выбраться через него на поверхность, нужно иметь не менее 280 очков опыта.
# Если до открытия люка время заканчивается - герой задыхается и умирает, воскрешаясь перед входом в подземелье,
# готовый к следующей попытке (игра начинается заново).
#
# Гарантируется, что искомый путь только один, и будьте аккуратны в рассчетах!
# При неправильном использовании библиотеки decimal человек, играющий с вашим скриптом рискует никогда не найти путь.
#
# Также, при каждом ходе игрока ваш скрипт должен запоминать следущую информацию:
# - текущую локацию
# - текущее количество опыта
# - текущие дату и время (для этого используйте библиотеку datetime)
# После успешного или неуспешного завершения игры вам необходимо записать
# всю собранную информацию в csv файл dungeon.csv.
# Названия столбцов для csv файла: current_location, current_experience, current_date
#
#
# Пример взаимодействия с игроком:
#
# Вы находитесь в Location_0_tm0
# У вас 0 опыта и осталось 123456.0987654321 секунд до наводнения
# Прошло времени: 00:00
#
# Внутри вы видите:
# — Вход в локацию: Location_1_tm1040
# — Вход в локацию: Location_2_tm123456
# Выберите действие:
# 1.Атаковать монстра
# 2.Перейти в другую локацию
# 3.Сдаться и выйти из игры
#
# Вы выбрали переход в локацию Location_2_tm1234567890
#
# Вы находитесь в Location_2_tm1234567890
# У вас 0 опыта и осталось 0.0987654321 секунд до наводнения
# Прошло времени: 20:00
#
# Внутри вы видите:
# — Монстра Mob_exp10_tm10
# — Вход в локацию: Location_3_tm55500
# — Вход в локацию: Location_4_tm66600
# Выберите действие:
# 1.Атаковать монстра
# 2.Перейти в другую локацию
# 3.Сдаться и выйти из игры
#
# Вы выбрали сражаться с монстром
#
# Вы находитесь в Location_2_tm0
# У вас 10 опыта и осталось -9.9012345679 секунд до наводнения
#
# Вы не успели открыть люк!!! НАВОДНЕНИЕ!!! Алярм!
#
# У вас темнеет в глазах... прощай, принцесса...
# Но что это?! Вы воскресли у входа в пещеру... Не зря матушка дала вам оберег :)
# Ну, на этот-то раз у вас все получится! Трепещите, монстры!
# Вы осторожно входите в пещеру... (текст умирания/воскрешения можно придумать свой ;)
#
# Вы находитесь в Location_0_tm0
# У вас 0 опыта и осталось 123456.0987654321 секунд до наводнения
# Прошло уже 0:00:00
# Внутри вы видите:
#  ...
#  ...
#
# и так далее...

import re
import csv
import json
import os.path
from datetime import datetime
from decimal import Decimal, ROUND_HALF_UP

remaining_time = '123456.0987654321'
# если изначально не писать число в виде строки - теряется точность!
field_names = ['current_location', 'current_experience', 'current_date']


def user_choice(max_number):
    while True:
        user_input = input('Выберите действие: ')
        try:
            choice = int(user_input)
        except ValueError:
            continue
        if 0 < choice <= max_number:
            return choice


class Location:

    def __init__(self, data):
        self.re = r'[LH]\w{4,7}_?B?\d*_tm(\d+\.?\d*)'
        self.data = data
        self.name = list(self.data)[0]
        self.time = self.extract_time()
        self.monsters, self.gates = self.in_view()
        self.gates_count = len(self.gates)
        self.monsters_count = len(self.monsters)

    def __str__(self):
        return self.name

    def extract_time(self):
        time = Decimal(re.match(self.re, self.name)[1])
        return time

    def in_view(self):
        monsters = []
        gates = []
        for event in self.data[self.name]:
            if isinstance(event, dict):
                gates.append(Location(event))
            elif isinstance(event, str) and 'Hatch' not in self.name:
                monsters.append(Monster(event))
        return monsters, gates

    def view(self):
        print('Внутри вы видите:')
        for monster in self.monsters:
            print(f'\t— Монстра {monster}')
        for location in self.gates:
            print(f'\t— Вход в локацию: {location}')

    def cremation(self):
        for monster in self.monsters:
            if not monster.alive:
                self.monsters.remove(monster)
        self.monsters_count = len(self.monsters)


class Monster:

    def __init__(self, name, alive=True):
        self.re = r'[BM]\w{2,3}\d*?_exp(\d+)_tm(\d+\.?\d*)'
        self.name = name
        self.exp, self.time = self.extract_exp_time()
        self.alive = alive

    def __str__(self):
        if self.alive:
            return self.name
        else:
            return self.name + ' (труп)'

    def extract_exp_time(self):
        exp = int(re.match(self.re, self.name)[1])
        time = Decimal(re.match(self.re, self.name)[2])
        return exp, time


class Hero:

    def __init__(self, remaining_time):
        self.exp = 0
        self.start_time = Decimal(remaining_time)
        self.remaining_time = Decimal(remaining_time)

    def attack(self, exp, time):
        self.exp += exp
        self.remaining_time -= time

    def move(self, time):
        self.remaining_time -= time

    def resurrect(self):
        self.exp = 0
        self.remaining_time = self.start_time


class Dungeon:

    def __init__(self, remaining_time, locations_data_file, field_names, game_out_file):
        self.hero = Hero(remaining_time=remaining_time)
        self.data_file = locations_data_file
        with open(self.data_file, 'r') as file:
            self.data = json.load(file)
        self.location = Location(data=self.data)
        self.game_info = []
        self.field_names = field_names
        self.game_out_file = game_out_file
        self.main_action_menu = '\t1. Атаковать монстра\n\t2. Перейти в другую локацию\n\t3. Сдаться и выйти из игры'

    def run(self):
        while True:
            self.check_status()
            self.action()

    def action(self):
        self.location.cremation()
        self.location.view()
        print('Выберите действие:')
        print(self.main_action_menu)
        action = user_choice(3)
        if action == 1:
            self.attack()
        elif action == 2:
            self.move()
        elif action == 3:
            self.end('surrender')

    def attack(self):
        if self.location.monsters:
            for number, monster in enumerate(self.location.monsters):
                print(f'{number + 1}. {monster}')
            action = user_choice(self.location.monsters_count)
            monster = self.location.monsters[action - 1]
            monster.alive = False
            self.hero.attack(monster.exp, monster.time)
            self.info_collect()
        else:
            print('Вокруг не видно монстров.')

    def move(self):
        if self.location.gates:
            for number, location in enumerate(self.location.gates):
                print(f'{number + 1}. {location}')
            action = user_choice(self.location.gates_count)
            move_to = self.location.gates[action - 1]
            self.location = move_to
            self.hero.move(move_to.time)
            self.info_collect()
        else:
            print('Сожалею, нет локаций для перехода...')

    def check_status(self):
        remaining_time = '{:f}'.format(self.hero.remaining_time)
        time = self.hero.start_time - self.hero.remaining_time
        time = time.quantize(Decimal('1'), ROUND_HALF_UP)
        time = datetime.utcfromtimestamp(int(time)).strftime('%H:%M:%S')
        print(f'Вы находитесь в {self.location.name}')
        print(f'У вас {self.hero.exp} опыта и осталось {remaining_time} секунд до наводнения')
        print(f'Прошло времени: {time}')
        if ('Hatch' in self.location.name) and (self.hero.exp > 279) and (self.hero.remaining_time > 0):
            self.end('win')
        elif self.hero.remaining_time <= 0:
            print('Вы не успели открыть люк!!! НАВОДНЕНИЕ!!! Алярм!')
            self.end('death')
        elif 'Hatch' in self.location.name:
            print('У вас не хватило сил открыть люк. Вы долго пытались... НАВОДНЕНИЕ!!! Алярм!')
            self.end('death')

    def restart(self):
        self.location = Location(data=self.data)
        self.hero.resurrect()
        self.info_collect()

    def end(self, status):
        if status == 'win':
            print(self.location.data[self.location.name])
            self.info_save()
            exit(0)
        elif status == 'surrender':
            print('Очень жаль. До новых встреч!')
            self.info_save()
            exit(0)
        elif status == 'death':
            print(
                f'У вас темнеет в глазах... прощай, принцесса...\n'
                f'Но что это?! Вы воскресли у входа в пещеру... Не зря матушка дала вам оберег :)\n'
                f'Ну, на этот-то раз у вас все получится! Трепещите, монстры!\n'
                f'Вы осторожно входите в пещеру...\n'
            )
            self.restart()

    def info_collect(self):
        current_date_and_time = str(datetime.now().strftime("%d.%m.%Y %H:%M:%S"))
        self.game_info.append([
            {
                'current_location': self.location.name,
                'current_experience': self.hero.exp,
                'current_date': current_date_and_time
            }
        ])

    def info_save(self):
        if os.path.exists(self.game_out_file):
            os.remove(self.game_out_file)
        with open(self.game_out_file, 'w', newline='') as out_csv:
            writer = csv.DictWriter(out_csv, delimiter=',', fieldnames=self.field_names)
            writer.writeheader()
            for line in self.game_info:
                writer.writerows(line)


if __name__ == '__main__':
    game = Dungeon(
        remaining_time=remaining_time,
        field_names=field_names,
        locations_data_file='rpg.json',
        game_out_file='dungeon.csv'
    )
    game.run()

# Учитывая время и опыт, не забывайте о точности вычислений!

# зачет!
