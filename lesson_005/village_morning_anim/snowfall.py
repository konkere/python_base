# -*- coding: utf-8 -*-

import simple_draw as sd


def snowfall(snowflakes, snowflake_speed=10, ground_height=100, resolution_x=1600, resolution_y=1000):
    snowflakes_quantity = len(snowflakes)
    for i in range(snowflakes_quantity):
        x = snowflakes[i][0]
        y = snowflakes[i][1]
        length = snowflakes[i][2]
        x += snowflake_speed
        y -= snowflake_speed
        snowflake_point = sd.get_point(x, y)
        sd.snowflake(snowflake_point, length, color=sd.COLOR_WHITE)
        snowflakes[i] = [x, y, length]
        if y < ground_height:
            snowflakes[i][0] = sd.random_number(-resolution_y, resolution_x)
            snowflakes[i][1] = resolution_y
