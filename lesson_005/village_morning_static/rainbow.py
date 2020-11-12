# -*- coding: utf-8 -*-

import simple_draw as sd

if __name__ == '__main__':
    resolution_x, resolution_y = 1600, 1000
    sd.resolution = (resolution_x, resolution_y)


def rainbow(line_width=20, radius=1500, center_x=400, center_y=-300):
    rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                      sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)
    circle_center = sd.get_point(center_x, center_y)
    for color in rainbow_colors:
        sd.circle(circle_center, radius, color, line_width)
        radius -= line_width


if __name__ == '__main__':
    sd.start_drawing()
    rainbow()
    sd.finish_drawing()
    sd.pause()
