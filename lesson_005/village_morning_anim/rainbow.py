# -*- coding: utf-8 -*-

import simple_draw as sd


def rainbow(rainbow_colors, line_width=20, radius=1500, center_x=400, center_y=-300):
    circle_center = sd.get_point(center_x, center_y)
    for color in rainbow_colors:
        sd.circle(circle_center, radius, color, line_width)
        radius -= line_width
