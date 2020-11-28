# -*- coding: utf-8 -*-

import simple_draw as sd

# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку

resolution_x = 1000
resolution_y = 800
sd.resolution = (resolution_x, resolution_y)
speed = 10


class Snowflake:
    # TODO предлагаю ничего не принимать на вход
    def __init__(self, x, y, length):
        # TODO сделать код самодостаточным, определять рендомные значения в момент инициализации экземпляра класса
        # TODO не используя переменные из глобального скоупа
        self.x = x
        self.y = y
        self.length = length
        self.color = sd.COLOR_WHITE

    def clear_previous_picture(self):
        snowlake_center = sd.get_point(self.x, self.y)
        sd.snowflake(center=snowlake_center, length=self.length, color=sd.background_color)

    def move(self):
        # TODO тут использовать метод, может_падать, если может то двигать икс и игрик
        # TODO от куда у нас в классе появилось speed?
        self.y -= speed

    def draw(self):
        snowlake_center = sd.get_point(self.x, self.y)
        sd.snowflake(center=snowlake_center, length=self.length, color=self.color)

    def can_fall(self):
        # TODO напрашивается запись return self.y > 50
        if self.y > 50:
            return True


flake = Snowflake(int(resolution_x / 2), resolution_y - 100, 50)

while True:
    flake.clear_previous_picture()
    flake.move()
    flake.draw()
    if not flake.can_fall():
        break
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

# TODO вторую часть перенесите сюда уже доработанную по ТУДУ выше

# шаг 2: создать снегопад - список объектов Снежинка в отдельном списке, обработку примерно так:
# flakes = get_flakes(count=N)  # создать список снежинок
# while True:
#     for flake in flakes:
#         flake.clear_previous_picture()
#         flake.move()
#         flake.draw()
#     fallen_flakes = get_fallen_flakes()  # подчитать сколько снежинок уже упало
#     if fallen_flakes:
#         append_flakes(count=fallen_flakes)  # добавить еще сверху
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break

sd.pause()
