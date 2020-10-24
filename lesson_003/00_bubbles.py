# -*- coding: utf-8 -*-

import simple_draw as sd
import time
import random

resolution_x, resolution_y = 1200, 800
sd.resolution = (resolution_x, resolution_y)
buble_color = (sd.COLOR_RED, sd.COLOR_GREEN, sd.COLOR_DARK_PURPLE)


def draw_buble(point, step, color):
    radius = 50
    for i in range(3):
        radius += step
        sd.circle(center_position=point, radius=radius, color=color, width=1)


# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
point = sd.get_point(100, resolution_y - 100)
radius = 50
step = 5
for _ in range(3):
    radius += step
    sd.circle(center_position=point, radius=radius, width=1)

time.sleep(2)

# Написать функцию рисования пузырька, принммающую 3 (или более) параметра: точка рисования, шаг и цвет
point = sd.get_point(resolution_x * .5, resolution_y - 100)
draw_buble(point=point, step=10, color=buble_color[0])

time.sleep(2)

# Нарисовать 10 пузырьков в ряд
for x in range(100, 1001, 100):
    point = sd.get_point(x, resolution_y - 300)
    draw_buble(point=point, step=5, color=buble_color[1])

time.sleep(2)

# Нарисовать три ряда по 10 пузырьков
for x in range(100, 1001, 100):
    for y in range(100, 301, 100):
        point = sd.get_point(x, y)
        draw_buble(point=point, step=5, color=buble_color[2])

time.sleep(2)

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
for _ in range(100):
    point = sd.random_point()
    step = random.randint(3, 20)
    draw_buble(point=point, step=step, color=sd.random_color())

sd.pause()
