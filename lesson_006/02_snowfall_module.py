# -*- coding: utf-8 -*-

import simple_draw as sd
from snowfall import make_snowflakes, draw_snowflakes, fall_snowflakes
from snowfall import check_snowflakes_on_ground, destroy_snowflakes

# На основе кода из lesson_004/05_snowfall.py
# сделать модуль snowfall.py в котором реализовать следующие функции
#  создать_снежинки(N) - создает N снежинок
#  нарисовать_снежинки_цветом(color) - отрисовывает все снежинки цветом color
#  сдвинуть_снежинки() - сдвигает снежинки на один шаг
#  номера_достигших_низа_экрана() - выдает список номеров снежинок, которые вышли за границу экрана
#  удалить_снежинки(номера) - удаляет снежинки с номерами из списка
# снежинки хранить в глобальных переменных модуля snowfall
#
# В текущем модуле реализовать главный цикл падения снежинок,
# обращаясь ТОЛЬКО к функциям модуля snowfall

resolution_x = 1000
resolution_y = 800
sd.resolution = (resolution_x, resolution_y)
sd.caption = 'Snowfall'
snowflakes_quantity = 50
snowflakes_color = sd.COLOR_WHITE

# создать_снежинки(N)
make_snowflakes(snowflakes_quantity, resolution_x, resolution_y)

while True:
    sd.start_drawing()
    #  нарисовать_снежинки_цветом(color=sd.background_color)
    draw_snowflakes(color=sd.background_color)
    #  сдвинуть_снежинки()
    fall_snowflakes()
    #  нарисовать_снежинки_цветом(color)
    draw_snowflakes(color=snowflakes_color)
    #  если есть номера_достигших_низа_экрана() то
    #       удалить_снежинки(номера)
    #       создать_снежинки(count)
    snowflakes_on_ground = check_snowflakes_on_ground()
    # TODO тут можно чекать просто if snowflakes_on_ground:
    # TODO Если что то есть в snowflakes_on_ground то будет True
    if not snowflakes_on_ground == []:
        destroy_snowflakes(snowflakes_on_ground)
        make_snowflakes(len(snowflakes_on_ground), resolution_x, resolution_y + 300)
    sd.finish_drawing()
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()
