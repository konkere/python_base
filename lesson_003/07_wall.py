# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

resolution_x, resolution_y = 1200, 800
simple_draw.resolution = (resolution_x, resolution_y)
brick_width, brick_height = 100, 50
# TODO чтобы не заводить новую переменную получим ее в заголовке цикла
shift_y = 0
# TODO для получения номера строки и Y используйте enumerate(range(0, 551, 50)), и сразу делайте распаковку
# TODO в цикле мы сразу получим две переменные номер строки и сам Y
for y in range(0, resolution_y, brick_height):
    shift_y += 1
    x = 0

    if shift_y % 2 == 0:
        shift_x = int(x - brick_width / 2)
    else:
        shift_x = x

    for x in range(shift_x, resolution_x, brick_width):
        brick_point_left_bottom = simple_draw.get_point(x, y)
        brick_point_right_top = simple_draw.get_point(x + brick_width, y + brick_height)
        simple_draw.rectangle(brick_point_left_bottom, brick_point_right_top, simple_draw.COLOR_RED, 1)

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
