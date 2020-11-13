# -*- coding: utf-8 -*-

import simple_draw as sd


def sun(rotate_angle=0, color=sd.COLOR_YELLOW, resolution_y=1000, sun_rays=15, sun_ray_lenght=150, sun_radius=80):
    sun_center_x = sun_ray_lenght + 50
    sun_center_y = resolution_y - sun_ray_lenght - 50
    sun_center = sd.get_point(sun_center_x, sun_center_y)
    sd.circle(sun_center, sun_radius, color, width=0)
    for sun_angle in range(rotate_angle, rotate_angle + 360, int(360 / sun_rays)):
        sd.vector(sun_center, sun_angle, sun_ray_lenght, color, width=5)
