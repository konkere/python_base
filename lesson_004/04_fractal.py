# -*- coding: utf-8 -*-

import simple_draw as sd
import time

# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,

# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длина ветвей" в 0.75 меньшей чем длина только что нарисованной ветви

# 3) Запустить вашу рекурсивную функцию, используя следующие параметры:
# root_point = sd.get_point(300, 30)
# draw_branches(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения

resolution_x = 1200
resolution_y = 800
sd.resolution = (resolution_x, resolution_y)
sd.background_color = sd.COLOR_BLACK
sd.caption = 'Fractal'

stem_angle = 90
branch_angle = 30
branch_length = 150
branch_color = sd.COLOR_GREEN
branch_width = 3


# В задании просили _функцию_ (одну), которая должна рисовать _две_ ветви дерева из начальной точки.
# Но пусть так:
# ---------------------------Вариант 1 часть 1 начало---------------------------
# def draw_branches(start_point=sd.get_point(resolution_x / 2, 0),
#                   angle=branch_angle, length=branch_length, color=branch_color, width=branch_width):
#     sd.vector(start=start_point, angle=stem_angle + angle, length=length, color=color, width=width)
# ---------------------------Вариант 1 часть 1 конец---------------------------

# Или так:
# ---------------------------Вариант 2 начало---------------------------
def draw_branches(start_point=sd.get_point(resolution_x / 2, 0),
                  angle=branch_angle, length=branch_length, color=branch_color, width=branch_width):
    angles = [-angle, angle]
    for angle in angles:
        sd.vector(start=start_point, angle=stem_angle + angle, length=length, color=color, width=width)
# ---------------------------Вариант 2 конец---------------------------


stem_point = sd.vector(start=sd.get_point(resolution_x / 2, 0), angle=stem_angle, length=branch_length,
                       color=sd.COLOR_GREEN, width=branch_width)
draw_branches(start_point=stem_point, angle=30, length=200)
# ---------------------------Вариант 1 часть 2 начало---------------------------
# draw_branches(start_point=stem_point, angle=-30, length=200)
# ---------------------------Вариант 1 часть 2 конец---------------------------

time.sleep(3)
sd.clear_screen()


def draw_branches_v2(start_point=sd.get_point(resolution_x / 2, 0), angle=branch_angle,
                     length=branch_length, color=branch_color, width=branch_width, delta_angle=30):
    if length < 10:
        return
    branch = sd.vector(start=start_point, angle=angle, length=length, color=color, width=width)
    end_point = branch
    length *= .75
    draw_branches_v2(start_point=end_point, angle=angle + delta_angle, length=length, color=color, width=width)
    draw_branches_v2(start_point=end_point, angle=angle - delta_angle, length=length, color=color, width=width)


root_point = sd.get_point(300, 30)
draw_branches_v2(start_point=root_point, angle=90, length=100)

# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

# Пригодятся функции
# sd.random_number()

time.sleep(3)
sd.clear_screen()


def draw_branches_v3(start_point=sd.get_point(resolution_x / 2, 0), angle=branch_angle,
                     length=branch_length, color=branch_color, width=branch_width, delta_angle=30):
    length_1 = length * .75 * sd.random_number(80, 120) / 100
    length_2 = length * .75 * sd.random_number(80, 120) / 100
    angle_1 = angle + round(delta_angle * sd.random_number(60, 140) / 100)
    angle_2 = angle - round(delta_angle * sd.random_number(60, 140) / 100)
    branch = sd.vector(start=start_point, angle=angle, length=length, color=color, width=width)
    end_point = branch
    if length < 10:
        return
    draw_branches_v3(start_point=end_point, angle=angle_1, length=length_1, color=color, width=width)
    draw_branches_v3(start_point=end_point, angle=angle_2, length=length_2, color=color, width=width)


draw_branches_v3(angle=90, width=1)

sd.pause()

# зачет!
