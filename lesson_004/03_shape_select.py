# -*- coding: utf-8 -*-

import simple_draw as sd

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg

resolution_x = 800
resolution_y = 800
sd.resolution = (resolution_x, resolution_y)
sd.caption = 'Shape select'

# TODO в объекте данных, можно хранит не только строковое название но и саму функцию чтобы потом ее вызывать

# TODO Примерно новый объект данных может выглядеть вот так:
# TODO colors = {0: ['треугольник', функция_треугольник], 1: ['квадрат', функция_квадрат], и так далее!
shapes_names = ('triangle', 'square', 'pentagon', 'hexagon')
shapes = []
color = sd.COLOR_WHITE
# TODO аналогично
for i, j in enumerate(shapes_names):
    print(i, '->', j)
    shapes.append((i, j))


user_input = input('Выберите фигуру (введите её номер): ')

if user_input.isdecimal():
    shape_number = int(user_input)
    if 0 <= shape_number < 4:
        shape_name = shapes[shape_number][1]
        print('Вы выбрали:', shapes[shape_number][1])
    else:
        print('В списке нет такого номера. Нарисую треугольник.')
        shape_name = 'triangle'
elif user_input == '':
    print('Вы не ввели номер фигуры. Нарисую треугольник.')
    shape_name = 'triangle'
else:
    print('Вы ввели не номер. Нарисую треугольник.')
    shape_name = 'triangle'


# TODO функции объявляем выше основной логики
def polygon_draw(polygon_point, start_angle, side_length, sides=3, color=color, line_width=3):
    end_to_start_point = polygon_point
    for side in range(sides - 1):
        vector = sd.vector(start=end_to_start_point, angle=start_angle + 360*side/sides,
                           length=side_length, width=line_width, color=color)
        end_to_start_point = vector
    sd.line(end_to_start_point, polygon_point, color, width=line_width)


def triangle_draw(triangle_point, start_angle, side_length, color, line_width=3):
    sides = 3
    polygon_draw(triangle_point, start_angle, side_length, sides, color, line_width=line_width)


def square_draw(square_point, start_angle, side_length, color, line_width=3):
    sides = 4
    polygon_draw(square_point, start_angle, side_length, sides, color, line_width=line_width)


def pentagon_draw(pentagon_point, start_angle, side_length, color, line_width=3):
    sides = 5
    polygon_draw(pentagon_point, start_angle, side_length, sides, color, line_width=line_width)


def hexagon_draw(hexagon_point, start_angle, side_length, color, line_width=3):
    sides = 6
    polygon_draw(hexagon_point, start_angle, side_length, sides, color, line_width=line_width)


shape_start_point = sd.get_point(resolution_x / 2 - 100, resolution_y / 2 - 100)
# TODO тогда тут если мы по ключу выберем нужную нам функцию! Важно! не ее название, а именно функцию.
# TODO то нам останется подставить нужные параметры и вызвать ее тут используя ()
# TODO тогда не придется писать такую вложенность!

# TODO это будем делать в главной логике где получили функцию
if shape_name == 'triangle':
    triangle_draw(shape_start_point, 0, 200, color)
elif shape_name == 'square':
    square_draw(shape_start_point, 0, 200, color)
elif shape_name == 'pentagon':
    pentagon_draw(shape_start_point, 0, 200, color)
elif shape_name == 'hexagon':
    hexagon_draw(shape_start_point, 0, 200, color)

sd.pause()
