# -*- coding: utf-8 -*-
import simple_draw as sd

# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg

resolution_x = 1000
resolution_y = 800
sd.resolution = (resolution_x, resolution_y)
sd.caption = 'Global color'

colors = {'red': sd.COLOR_RED, 'orange': sd.COLOR_ORANGE, 'yellow': sd.COLOR_YELLOW, 'green': sd.COLOR_GREEN,
          'cyan': sd.COLOR_CYAN, 'blue': sd.COLOR_BLUE, 'purple': sd.COLOR_PURPLE}

color_names = []
# TODO нейминг переменных пишите развернуто по j - не понятно что там внутри
for i, j in enumerate(colors):
    print(i, '->', j)
    color_names.append((i, j))
user_input = input('Выберите цвет (введите его номер): ')

if user_input.isdecimal():
    color_number = int(user_input)
    if 0 <= color_number < 7:
        color_name = color_names[color_number]
        print('Вы выбрали:', color_name[1])
        color = colors[color_name[1]]
    else:
        print('В списке нет такого номера. Буду рисовать жёлтым.')
        color = sd.COLOR_YELLOW
elif user_input == '':
    print('Вы не ввели номер цвета. Буду рисовать оранжевым.')
    color = sd.COLOR_ORANGE
else:
    print('Вы ввели не номер. Буду рисовать красным.')
    color = sd.COLOR_RED


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


triangle_draw(sd.get_point(200, 100), 10, 200, color)


def square_draw(square_point, start_angle, side_length, color, line_width=3):
    sides = 4
    polygon_draw(square_point, start_angle, side_length, sides, color, line_width=line_width)


square_draw(sd.get_point(600, 100), 50, 200, color)


def pentagon_draw(pentagon_point, start_angle, side_length, color, line_width=3):
    sides = 5
    polygon_draw(pentagon_point, start_angle, side_length, sides, color, line_width=line_width)


pentagon_draw(sd.get_point(300, 450), 60, 200, color)


def hexagon_draw(hexagon_point, start_angle, side_length, color, line_width=3):
    sides = 6
    polygon_draw(hexagon_point, start_angle, side_length, sides, color, line_width=line_width)


hexagon_draw(sd.get_point(650, 400), 0, 200, color)

sd.pause()
