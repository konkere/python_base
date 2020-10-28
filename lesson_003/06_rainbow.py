# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
resolution_x, resolution_y = 1200, 800
sd.resolution = (resolution_x, resolution_y)
line_numbers = 7
line_width = 4
line_step = 5
point_start_x, point_start_y = 50, 50
point_end_x, point_end_y = 350, 450
point_start = sd.get_point(point_start_x, point_start_y)
point_end = sd.get_point(point_end_x, point_end_y)

# TODO нейминг, переменной i - это у нас цвет, так и назовите ее color
for i in rainbow_colors:
    sd.line(point_start, point_end, i, line_width)
    point_start_x += line_step
    point_start_y -= line_step
    point_end_x += line_step
    point_end_y -= line_step
    point_start = sd.get_point(point_start_x, point_start_y)
    point_end = sd.get_point(point_end_x, point_end_y)
# Подсказка: цикл нужно делать сразу по тьюплу с цветами радуги.


# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво
circle_line_width = 30
circle_line_step = 30
circle_radius = 1000
circle_center_x, circle_center_y = resolution_x, resolution_y * (-.5)
circle_center = sd.get_point(circle_center_x, circle_center_y)
# TODO нейминг, переменной i - это у нас цвет, так и назовите ее color
for i in rainbow_colors:
    sd.circle(circle_center, circle_radius, i, circle_line_width)
    circle_radius -= circle_line_step

sd.pause()
