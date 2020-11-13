# -*- coding: utf-8 -*-

import simple_draw as sd


def snowfall(snowflakes, snowflake_speed=10, ground_height=100, house_shift_x = 100):
    snowflakes_quantity = len(snowflakes)
    for i in range(snowflakes_quantity):
        x = snowflakes[i][0]
        y = snowflakes[i][1]
        length = snowflakes[i][2]
        snowflake_point = sd.get_point(x, y)
        sd.snowflake(snowflake_point, length, color=sd.COLOR_DARK_BLUE)
        x += snowflake_speed
        y -= snowflake_speed
        snowflake_point = sd.get_point(x, y)
        sd.snowflake(snowflake_point, length, color=sd.COLOR_WHITE)
        snowflakes[i] = [x, y, length]
        if y < ground_height:
            snowflakes[i][0] = sd.random_number(0 - house_shift_x, 0)
            snowflakes[i][1] = house_shift_x
