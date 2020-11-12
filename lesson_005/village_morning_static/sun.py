# -*- coding: utf-8 -*-

import simple_draw as sd

if __name__ == '__main__':
    resolution_x, resolution_y = 1600, 1000
    sd.resolution = (resolution_x, resolution_y)


def sun(resolution_y=1000, sun_rays=15, sun_ray_lenght=150, sun_radius=80):
    sun_center_x = sun_ray_lenght + 50
    sun_center_y = resolution_y - sun_ray_lenght - 50
    sun_center = sd.get_point(sun_center_x, sun_center_y)
    sd.circle(sun_center, sun_radius, sd.COLOR_YELLOW, width=0)
    for sun_angle in range(0, 360, int(360 / sun_rays)):
        sd.vector(sun_center, sun_angle, sun_ray_lenght, sd.COLOR_YELLOW, width=5)


if __name__ == '__main__':
    sd.start_drawing()
    sun()
    sd.finish_drawing()
    sd.pause()