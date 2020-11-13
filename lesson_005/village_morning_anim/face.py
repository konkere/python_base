# -*- coding: utf-8 -*-

import simple_draw as sd


def face(x, y, color, eye_blink):
    smile_center = sd.get_point(x, y)
    if eye_blink == 1:
        smile_eye_right = sd.get_point(x - 20, y + 10)
        smile_eye_left = sd.get_point(x + 20, y + 10)
        sd.vector(smile_eye_left, 180, 10, color, 3)
        sd.vector(smile_eye_right, 0, 10, color, 3)
    else:
        smile_eye_right = sd.get_point(x - 15, y + 10)
        smile_eye_left = sd.get_point(x + 15, y + 10)
        sd.circle(smile_eye_left, 5, color, 3)
        sd.circle(smile_eye_right, 5, color, 3)
    smile_nose_point1 = sd.get_point(x, y + 5)
    smile_nose_point2 = sd.get_point(x - 5, y - 10)
    smile_nose_point3 = sd.get_point(x + 5, y - 10)
    smile_nose = [smile_nose_point1, smile_nose_point2, smile_nose_point3]
    smile_mouth_point1 = sd.get_point(x - 20, y - 20)
    smile_mouth_point2 = sd.get_point(x + 20, y - 20)
    sd.circle(smile_center, 40, color, 3)
    sd.lines(smile_nose, color, width=3)
    sd.line(smile_mouth_point1, smile_mouth_point2, color, 3)

