# -*- coding: utf-8 -*-

# (определение функций)
import random
import simple_draw

# Написать функцию отрисовки смайлика по заданным координатам
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.

resolution_x, resolution_y = 1200, 800
simple_draw.resolution = (resolution_x, resolution_y)


def smile(x, y, color):
    smile_center = simple_draw.get_point(x, y)
    smile_eye_right = simple_draw.get_point(x - 15, y + 10)
    smile_eye_left = simple_draw.get_point(x + 15, y + 10)
    smile_nose_point1 = simple_draw.get_point(x, y + 5)
    smile_nose_point2 = simple_draw.get_point(x - 5, y - 10)
    smile_nose_point3 = simple_draw.get_point(x + 5, y - 10)
    smile_nose = [smile_nose_point1, smile_nose_point2, smile_nose_point3]
    smile_mouth_point1 = simple_draw.get_point(x - 20, y - 20)
    smile_mouth_point2 = simple_draw.get_point(x + 20, y - 20)
    simple_draw.circle(smile_center, 50, color, 3)
    simple_draw.circle(smile_eye_left, 5, color, 3)
    simple_draw.circle(smile_eye_right, 5, color, 3)
    simple_draw.lines(smile_nose, color, width=3)
    simple_draw.line(smile_mouth_point1, smile_mouth_point2, color, 3)


for _ in range(10):
    smile(random.randint(50, resolution_x - 50), random.randint(50, resolution_y - 50), simple_draw.random_color())

simple_draw.pause()

# зачет!
