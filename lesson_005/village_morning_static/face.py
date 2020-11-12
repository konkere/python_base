# -*- coding: utf-8 -*-

import simple_draw as sd

if __name__ == '__main__':
    resolution_x, resolution_y = 1600, 1000
    sd.resolution = (resolution_x, resolution_y)


def face(x, y, color):
    smile_center = sd.get_point(x, y)
    smile_eye_right = sd.get_point(x - 15, y + 10)
    smile_eye_left = sd.get_point(x + 15, y + 10)
    smile_nose_point1 = sd.get_point(x, y + 5)
    smile_nose_point2 = sd.get_point(x - 5, y - 10)
    smile_nose_point3 = sd.get_point(x + 5, y - 10)
    smile_nose = [smile_nose_point1, smile_nose_point2, smile_nose_point3]
    smile_mouth_point1 = sd.get_point(x - 20, y - 20)
    smile_mouth_point2 = sd.get_point(x + 20, y - 20)
    sd.circle(smile_center, 40, color, 3)
    sd.circle(smile_eye_left, 5, color, 3)
    sd.circle(smile_eye_right, 5, color, 3)
    sd.lines(smile_nose, color, width=3)
    sd.line(smile_mouth_point1, smile_mouth_point2, color, 3)


if __name__ == '__main__':
    sd.start_drawing()
    face(100, 100, sd.COLOR_RED)
    sd.finish_drawing()
    sd.pause()
