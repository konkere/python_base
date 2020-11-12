# -*- coding: utf-8 -*-

import simple_draw as sd

if __name__ == '__main__':
    resolution_x, resolution_y = 1600, 1000
    sd.resolution = (resolution_x, resolution_y)


def snow(start_x=0, end_x=300, ground=100, height=50, quantity=100):
    for _ in range(quantity):
        x = sd.random_number(start_x, end_x)
        y = sd.random_number(ground, ground + height)
        length = sd.random_number(3, 10)
        sd.snowflake(center=sd.get_point(x, y), length=length)


if __name__ == '__main__':
    sd.start_drawing()
    snow()
    sd.finish_drawing()
    sd.pause()