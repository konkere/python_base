# -*- coding: utf-8 -*-

import simple_draw as sd

# На основе вашего кода из решения lesson_004/01_shapes.py сделать функцию-фабрику,
# которая возвращает функции рисования треугольника, четырехугольника, пятиугольника и т.д.
#
# Функция рисования должна принимать параметры
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Функция-фабрика должна принимать параметр n - количество сторон.

resolution_x = 1000
resolution_y = 800
sd.resolution = (resolution_x, resolution_y)
sd.caption = 'Shapes factory'


def get_polygon(n):
    def polygon_draw(polygon_point, start_angle, side_length, sides=n, line_width=3):
        end_to_start_point = polygon_point
        for side in range(sides - 1):
            vector = sd.get_vector(start_point=end_to_start_point, angle=start_angle + 360 * side / sides,
                                   length=side_length, width=line_width)
            vector.draw()
            end_to_start_point = vector.end_point
        sd.line(end_to_start_point, polygon_point, width=line_width)
    return polygon_draw


draw_triangle = get_polygon(n=3)
draw_triangle(polygon_point=sd.get_point(200, 200), start_angle=13, side_length=100)

draw_square = get_polygon(n=4)
draw_square(polygon_point=sd.get_point(600, 200), start_angle=13, side_length=100)

draw_pentagon = get_polygon(n=5)
draw_pentagon(polygon_point=sd.get_point(200, 500), start_angle=13, side_length=100)

draw_octagon = get_polygon(n=8)
draw_octagon(polygon_point=sd.get_point(600, 500), start_angle=13, side_length=100)


sd.pause()

# зачет!
