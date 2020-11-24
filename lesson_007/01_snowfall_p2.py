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

    def __init__(self, number):
        self.number = number
        self.x = sd.randint(0, resolution_x)
        self.y = sd.randint(0, resolution_y)
        self.length = sd.randint(10, 50)
        self.color = sd.COLOR_WHITE

    def clear_previous_picture(self):
        snowlake_center = sd.get_point(self.x, self.y)
        sd.snowflake(center=snowlake_center, length=self.length, color=sd.background_color)

    def move(self):
        self.reincarnation()
        self.x += sd.randint(-20, 20)
        self.y -= speed

    def draw(self):
        snowlake_center = sd.get_point(self.x, self.y)
        sd.snowflake(center=snowlake_center, length=self.length, color=self.color)

    def reincarnation(self):
        if self.y < -50:
            self.x = sd.randint(0, resolution_x)
            self.y = sd.randint(resolution_y, resolution_y + 50)
            self.length = sd.randint(10, 50)


def get_snowflakes(count):
    flakes = []
    for flake in range(count):
        flakes.append(Snowflake(flake))
    return flakes


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

snowflakes = get_snowflakes(count=100)

while True:
    sd.start_drawing()
    for snowflake in snowflakes:
        snowflake.clear_previous_picture()
        snowflake.move()
        snowflake.draw()
    sd.finish_drawing()
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

# В лекциях столько раз повторялось, что не надо гнаться за преждеждевременной оптимизацией.
# Вот оно запомнилось и отлижилось.
# А если ближе к сути, мне показалось, что в нашем случае правильнее будет не использовать конструкцию
# с вычислением упавших снежинок и занесением их в отдельный список, а ввести метод с "созданием"
# снежинок вместо упавших (путём их перегенерации).
# Аргументы за этот вариант: несколько действий мы заменяем одним. Количество падающих снежинок после начальной
# генерации у нас не меняется. В предложенном варианте нам надо получить список упавших, их количество, добавить
# столько же новых и удалить из общего списка упавшие (это же там подразумевается? Если нет, то список будет
# расти бесконечно?). Вместо этого мы помещаем упавшую снежинку наверх экрана, заново выдавая ей
# рандомный икс и размер. При этом делаем так, чтобы класс сам за этим и следил.
# Если я не ухватил ухватил суть задания и из-за этого в своей реализации опустил то, что как раз и требовалось
# отработать на пракике, то... что ж, будем переделывать (:
