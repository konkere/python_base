# -*- coding: utf-8 -*-

import simple_draw as sd

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

sd.resolution = (1000, 800)
sd.caption = 'Shapes'


def triangle_draw(triangle_point, start_angle, side_length, line_width = 3):
    vector1 = sd.get_vector(start_point=triangle_point, angle=start_angle,
                            length=side_length, width=line_width)
    vector1.draw()
    vector2 = sd.get_vector(start_point=vector1.end_point, angle=(start_angle + 360/3),
                            length=side_length, width=line_width)
    vector2.draw()
    vector3 = sd.get_vector(start_point=vector2.end_point, angle=(start_angle + 360*2/3),
                            length=side_length, width=line_width)
    vector3.draw()


triangle_draw(sd.get_point(200, 100), 50, 200)


def square_draw(square_point, start_angle, side_length, line_width = 3):
    vector1 = sd.get_vector(start_point=square_point, angle=start_angle,
                            length=side_length, width=line_width)
    vector1.draw()
    vector2 = sd.get_vector(start_point=vector1.end_point, angle=(start_angle + 360/4),
                            length=side_length, width=line_width)
    vector2.draw()
    vector3 = sd.get_vector(start_point=vector2.end_point, angle=(start_angle + 360*2/4),
                            length=side_length, width=line_width)
    vector3.draw()
    vector4 = sd.get_vector(start_point=vector3.end_point, angle=(start_angle + 360*3/4),
                            length=side_length, width=line_width)
    vector4.draw()


square_draw(sd.get_point(600, 100), 30, 200)


def pentagon_draw(pentagon_point, start_angle, side_length, line_width = 3):
    vector1 = sd.get_vector(start_point=pentagon_point, angle=start_angle,
                            length=side_length, width=line_width)
    vector1.draw()
    vector2 = sd.get_vector(start_point=vector1.end_point, angle=(start_angle + 360/5),
                            length=side_length, width=line_width)
    vector2.draw()
    vector3 = sd.get_vector(start_point=vector2.end_point, angle=(start_angle + 360*2/5),
                            length=side_length, width=line_width)
    vector3.draw()
    vector4 = sd.get_vector(start_point=vector3.end_point, angle=(start_angle + 360*3/5),
                            length=side_length, width=line_width)
    vector4.draw()
    # vector5 = sd.get_vector(start_point=vector4.end_point, angle=(start_angle + 360*4/5),
    #                         length=side_length, width=line_width)
    # vector5.draw()
    # sd.line(vector5.end_point, pentagon_point, width=line_width)
    # \/ Вместо последнего вектора и фикса к нему, которые образуют излом
    sd.line(vector4.end_point, pentagon_point, width=3)


pentagon_draw(sd.get_point(200, 450), 10, 200)


def hexagon_draw(hexagon_point, start_angle, side_length, line_width = 3):
    vector1 = sd.get_vector(start_point=hexagon_point, angle=start_angle,
                            length=side_length, width=line_width)
    vector1.draw()
    vector2 = sd.get_vector(start_point=vector1.end_point, angle=(start_angle + 360/6),
                            length=side_length, width=line_width)
    vector2.draw()
    vector3 = sd.get_vector(start_point=vector2.end_point, angle=(start_angle + 360*2/6),
                            length=side_length, width=line_width)
    vector3.draw()
    vector4 = sd.get_vector(start_point=vector3.end_point, angle=(start_angle + 360*3/6),
                            length=side_length, width=line_width)
    vector4.draw()
    vector5 = sd.get_vector(start_point=vector4.end_point, angle=(start_angle + 360*4/6),
                            length=side_length, width=line_width)
    vector5.draw()
    # vector6 = sd.get_vector(start_point=vector5.end_point, angle=(start_angle + 360*5/6),
    #                         length=side_length, width=line_width)
    # vector6.draw()
    # sd.line(vector6.end_point, hexagon_point, width=line_width)
    # \/ Вместо последнего вектора и фикса к нему, которые образуют излом
    sd.line(vector5.end_point, hexagon_point, width=line_width)


hexagon_draw(sd.get_point(700, 400), 20, 200)

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

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!


sd.pause()
