# -*- coding: utf-8 -*-

import simple_draw as sd
import time

# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Примерный алгоритм внутри функции:
#   # будем рисовать с помощью векторов, каждый следующий - из конечной точки предыдущего
#   текущая_точка = начальная точка
#   для угол_наклона из диапазона от 0 до 360 с шагом XXX
#      # XXX подбирается индивидуально для каждой фигуры
#      составляем вектор из текущая_точка заданной длины с наклоном в угол_наклона
#      рисуем вектор
#      текущая_точка = конечной точке вектора
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg

resolution_x = 1000
resolution_y = 800
sd.resolution = (resolution_x, resolution_y)
sd.caption = 'Shapes'


def triangle_draw(triangle_point, start_angle, side_length, line_width=3):
    point_0 = triangle_point
    angle = round(360/3)
    for vector_angle in range(0, angle * 2, angle):
        vector = sd.get_vector(start_point=triangle_point, angle=vector_angle + start_angle,
                               length=side_length, width=line_width)
        vector.draw()
        triangle_point = vector.end_point
    sd.line(start_point=triangle_point, end_point=point_0, width=line_width)


triangle_draw(sd.get_point(200, 100), 50, 200)


def square_draw(square_point, start_angle, side_length, line_width=3):
    point_0 = square_point
    angle = round(360/4)
    for vector_angle in range(0, angle * 3, angle):
        vector = sd.get_vector(start_point=square_point, angle=vector_angle + start_angle,
                               length=side_length, width=line_width)
        vector.draw()
        square_point = vector.end_point
    sd.line(start_point=square_point, end_point=point_0, width=line_width)


square_draw(sd.get_point(600, 100), 30, 200)


def pentagon_draw(pentagon_point, start_angle, side_length, line_width=3):
    point_0 = pentagon_point
    angle = round(360/5)
    for vector_angle in range(0, angle * 4, angle):
        vector = sd.get_vector(start_point=pentagon_point, angle=vector_angle + start_angle,
                               length=side_length, width=line_width)
        vector.draw()
        pentagon_point = vector.end_point
    sd.line(start_point=pentagon_point, end_point=point_0, width=line_width)


pentagon_draw(sd.get_point(200, 450), 10, 200)


def hexagon_draw(hexagon_point, start_angle, side_length, line_width=3):
    point_0 = hexagon_point
    angle = round(360/6)
    for vector_angle in range(0, angle * 5, angle):
        vector = sd.get_vector(start_point=hexagon_point, angle=vector_angle + start_angle,
                               length=side_length, width=line_width)
        vector.draw()
        hexagon_point = vector.end_point
    sd.line(start_point=hexagon_point, end_point=point_0, width=line_width)


hexagon_draw(sd.get_point(700, 400), 20, 200)

time.sleep(3)
sd.clear_screen()

# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44? Код писать не нужно, просто представь объем работы... и запомни это.

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв в начальной/конечной точках рисуемой фигуры
# (если он есть. подсказка - на последней итерации можно использовать линию от первой точки)


def polygon_draw(polygon_point, start_angle, side_length, sides=3, line_width=3):
    end_to_start_point = polygon_point
    for side in range(sides - 1):
        vector = sd.get_vector(start_point=end_to_start_point, angle=start_angle + 360*side/sides,
                               length=side_length, width=line_width)
        vector.draw()
        end_to_start_point = vector.end_point
    sd.line(end_to_start_point, polygon_point, width=line_width)


def triangle_draw_v2(triangle_point, start_angle, side_length, line_width=3):
    sides = 3
    polygon_draw(triangle_point, start_angle, side_length, sides, line_width=line_width)


triangle_draw_v2(sd.get_point(200, 100), 10, 200)


def square_draw_v2(square_point, start_angle, side_length, line_width=3):
    sides = 4
    polygon_draw(square_point, start_angle, side_length, sides, line_width=line_width)


square_draw_v2(sd.get_point(600, 100), 50, 200)


def pentagon_draw_v2(pentagon_point, start_angle, side_length, line_width=3):
    sides = 5
    polygon_draw(pentagon_point, start_angle, side_length, sides, line_width=line_width)


pentagon_draw_v2(sd.get_point(300, 450), 60, 200)


def hexagon_draw_v2(hexagon_point, start_angle, side_length, line_width=3):
    sides = 6
    polygon_draw(hexagon_point, start_angle, side_length, sides, line_width=line_width)


hexagon_draw_v2(sd.get_point(650, 400), 0, 200)

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!


sd.pause()
