# -*- coding: utf-8 -*-

import simple_draw as sd

if __name__ == '__main__':
    resolution_x, resolution_y = 1600, 1000
    sd.resolution = (resolution_x, resolution_y)


def tree(start_point=sd.get_point(0, 0), angle=90,
         length=100, color=sd.COLOR_DARK_YELLOW, width=3, delta_angle=30):
    length_1 = length * .75 * sd.random_number(80, 120) / 100
    length_2 = length * .75 * sd.random_number(80, 120) / 100
    angle_1 = angle + round(delta_angle * sd.random_number(60, 140) / 100)
    angle_2 = angle - round(delta_angle * sd.random_number(60, 140) / 100)
    branch = sd.vector(start=start_point, angle=angle, length=length, color=color, width=width)
    end_point = branch
    if 30 <= length < 40:
        color = sd.COLOR_GREEN
        width = 2
    elif 3 <= length < 30:
        color = sd.COLOR_GREEN
        width = 1
    elif length < 3:
        return
    tree(start_point=end_point, angle=angle_1, length=length_1, color=color, width=width)
    tree(start_point=end_point, angle=angle_2, length=length_2, color=color, width=width)


if __name__ == '__main__':
    sd.start_drawing()
    tree()
    sd.finish_drawing()
    sd.pause()
