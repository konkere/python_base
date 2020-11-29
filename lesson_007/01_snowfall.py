# -*- coding: utf-8 -*-

import simple_draw as sd

# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку

resolution_x = 1000
resolution_y = 800
sd.resolution = (resolution_x, resolution_y)
flakes = []


class Snowflake:
    # TODO сделайте их параметрами класса, а не экземпляра.

    def __init__(self):
        # TODO ответ выше
        # Мне всё равно понадобятся значения размера экрана для генерации.
        # Может их стоит передавать при создании объекта? Если нет, то получится вот так:
        self.x = sd.randint(0, resolution_x)
        self.y = sd.randint(resolution_y, resolution_y + 200)
        self.length = sd.randint(10, 50)
        self.color = sd.COLOR_WHITE
        self.speed = 10

    def clear_previous_picture(self):
        snowlake_center = sd.get_point(self.x, self.y)
        sd.snowflake(center=snowlake_center, length=self.length, color=sd.background_color)

    def move(self):
        if self.can_fall():
            self.x += sd.randint(-20, 20)
            self.y -= self.speed

    def draw(self):
        snowlake_center = sd.get_point(self.x, self.y)
        sd.snowflake(center=snowlake_center, length=self.length, color=self.color)

    def can_fall(self):
        return self.y > 0


def get_snowflakes(count):
    global flakes
    for _ in range(count):
        flakes.append(Snowflake())


def get_fallen_flakes():
    global flakes
    count = 0
    for flake in flakes:
        if not flake.can_fall():
            flake.clear_previous_picture()
            flakes.remove(flake)
            count += 1
    return count


# get_snowflakes(count=1)


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


get_snowflakes(count=50)

while True:
    sd.start_drawing()
    for flake in flakes:
        flake.clear_previous_picture()
        flake.move()
        flake.draw()
    sd.finish_drawing()
    fallen_flakes = get_fallen_flakes()
    if fallen_flakes:
        get_snowflakes(fallen_flakes)
    sd.sleep(0.1)
    if sd.user_want_exit():
        break
