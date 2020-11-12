# -*- coding: utf-8 -*-

import simple_draw as sd

if __name__ == '__main__':
    resolution_x, resolution_y = 1600, 1000
    sd.resolution = (resolution_x, resolution_y)


def bricks(start_x, start_y, width, height, brick_width):
    brick_height = int(brick_width / 2)
    for shift_y, y in enumerate(range(start_y, start_y + height, brick_height)):
        if shift_y % 2 == 0:
            shift_x = brick_height
        else:
            shift_x = 0
        for x in range(start_x + shift_x, start_x + width - shift_x, brick_width):
            brick_point_left_bottom = sd.get_point(x, y)
            brick_point_right_top = sd.get_point(x + brick_width, y + brick_height)
            sd.rectangle(brick_point_left_bottom, brick_point_right_top, sd.COLOR_WHITE, 1)


def house(ground_height=100, house_shift_x=300, house_height=300, house_width=600, brick_width=40):
    brick_color = (178, 34, 34)
    # каркас дома
    house_frame_point_left_bottom = sd.get_point(house_shift_x, ground_height)
    house_frame_point_right_top = sd.get_point(house_shift_x + house_width, ground_height + house_height)
    sd.rectangle(house_frame_point_left_bottom, house_frame_point_right_top, brick_color, 0)
    sd.rectangle(house_frame_point_left_bottom, house_frame_point_right_top, sd.COLOR_WHITE, 1)
    # труба
    pipe_x1 = int(house_shift_x + house_width * 0.1)
    pipe_y1 = int(ground_height + house_height)
    pipe_x2 = int(house_shift_x + house_width * 0.1 + brick_width * 3)
    pipe_y2 = int(ground_height + house_height + brick_width * 3)
    pipe_frame_point_left_bottom = sd.get_point(pipe_x1, pipe_y1)
    pipe_frame_point_right_top = sd.get_point(pipe_x2, pipe_y2)
    sd.rectangle(pipe_frame_point_left_bottom, pipe_frame_point_right_top, brick_color, 0)
    bricks(pipe_x1, pipe_y1, pipe_x2 - pipe_x1, pipe_y2 - pipe_y1, brick_width)
    sd.rectangle(pipe_frame_point_left_bottom, pipe_frame_point_right_top, sd.COLOR_WHITE, 1)
    # крыша
    roof_point_left = sd.get_point(house_shift_x * 0.95, ground_height + house_height)
    roof_point_right = sd.get_point(house_shift_x * 1.05 + house_width, ground_height + house_height)
    roof_point_top = sd.get_point(house_shift_x + house_width / 2, ground_height + house_height * 4 / 3)
    roof = [roof_point_left, roof_point_right, roof_point_top]
    sd.polygon(roof, (169, 169, 169), width=0)
    sd.polygon(roof, sd.COLOR_WHITE, width=1)
    # кирпичная стена
    bricks(house_shift_x, ground_height, house_width, house_height, brick_width)
    # окно
    window_x_1 =house_shift_x + house_width / 4
    window_y_1 = ground_height + house_height / 3
    window_x_2 = house_shift_x + house_width / 2
    window_y_2 = ground_height + house_height * 2 / 3
    window_point_left_bottom = sd.get_point(window_x_1, window_y_1)
    window_point_right_top = sd.get_point(window_x_2, window_y_2)
    sd.rectangle(window_point_left_bottom, window_point_right_top, sd.COLOR_BLACK, width=0)
    sd.rectangle(window_point_left_bottom, window_point_right_top, sd.COLOR_WHITE, width=1)
    # дверь
    door_point_left_bottom = sd.get_point(house_shift_x + house_width * 0.8, ground_height)
    door_point_right_top = sd.get_point(house_shift_x + house_width, ground_height + house_height * 0.8)
    sd.rectangle(door_point_left_bottom, door_point_right_top, (51, 51, 51), width=0)
    sd.rectangle(door_point_left_bottom, door_point_right_top, sd.COLOR_WHITE, width=1)
    doorhandle_point = sd.get_point(house_shift_x + house_width * 0.85, ground_height + house_height / 2)
    sd.circle(doorhandle_point, radius=8, color=sd.COLOR_BLACK, width=0)
    return window_x_1, window_y_1, window_x_2, window_y_2


if __name__ == '__main__':
    sd.start_drawing()
    house()
    sd.finish_drawing()
    sd.pause()