# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

simple_draw.background_color = (178, 34, 34)
resolution_x, resolution_y = 1200, 800
simple_draw.resolution = (resolution_x, resolution_y)
brick_width, brick_height = 100, 50

for shift_y, y in enumerate(range(0, resolution_y, brick_height)):
    if shift_y % 2 == 0:
        # можно так
        shift_x = 50
    else:
        shift_x = 0

    for x in range(shift_x, resolution_x, brick_width):
        brick_point_left_bottom = simple_draw.get_point(x, y)
        brick_point_right_top = simple_draw.get_point(x + brick_width, y + brick_height)
        simple_draw.rectangle(brick_point_left_bottom, brick_point_right_top, simple_draw.COLOR_WHITE, 1)

# Подсказки:
#  Для отрисовки кирпича использовать функцию rectangle
#  Алгоритм должен получиться приблизительно такой:
#
#   цикл по координате Y
#       вычисляем сдвиг ряда кирпичей
#       цикл координате X
#           вычисляем правый нижний и левый верхний углы кирпича
#           рисуем кирпич

simple_draw.pause()

# зачет!
