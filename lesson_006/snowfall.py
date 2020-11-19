# -*- coding: utf-8 -*-

import simple_draw as sd

snowflakes = []
snowflakes_speed = 10


def make_snowflakes(quantity, resolution_x, resolution_y):
    global snowflakes
    for _ in range(quantity):
        snowflake_x = sd.randint(0, resolution_x)
        snowflake_y = sd.randint(resolution_y - 300, resolution_y)
        snowflake_length = sd.randint(10, 50)
        snowflake = [snowflake_x, snowflake_y, snowflake_length]
        snowflakes.append(snowflake)


def draw_snowflakes(color):
    for snowflake in snowflakes:
        snowflake_point = sd.get_point(snowflake[0], snowflake[1])
        sd.snowflake(snowflake_point, snowflake[2], color)


def fall_snowflakes():
    global snowflakes
    for snowflake in snowflakes:
        snowflake[0] += sd.random_number(-20, 20)
        snowflake[1] -= snowflakes_speed


def check_snowflakes_on_ground():
    global snowflakes
    snowflakes_on_ground = []
    for snowflake in range(len(snowflakes)):
        if snowflakes[snowflake][1] < -50:
            snowflakes_on_ground.append(snowflake)
    return snowflakes_on_ground


def destroy_snowflakes(snowflakes_on_ground):
    global snowflakes
    snowflakes_on_ground.reverse()
    for snowflake in snowflakes_on_ground:
        snowflakes.pop(snowflake)
