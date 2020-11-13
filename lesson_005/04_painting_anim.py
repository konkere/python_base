# -*- coding: utf-8 -*-

# Создать пакет, в который скопировать функции отрисовки из предыдущего урока
#  - радуги
#  - стены
#  - дерева
#  - смайлика
#  - снежинок
# Функции по модулям разместить по тематике. Название пакета и модулей - по смыслу.
# Создать модуль с функцией отрисовки кирпичного дома с широким окном и крышей.

# С помощью созданного пакета нарисовать эпохальное полотно "Утро в деревне".
# На картине должны быть:
#  - кирпичный дом, в окошке - смайлик.
#  - слева от дома - сугроб (предположим что это ранняя весна)
#  - справа от дома - дерево (можно несколько)
#  - справа в небе - радуга, слева - солнце (весна же!)
# пример см. lesson_005/results/04_painting.jpg
# Приправить своей фантазией по вкусу (коты? коровы? люди? трактор? что придумается)

# Усложненное задание (делать по желанию)
# Анимировать картину.
# Пусть слева идет снегопад, радуга переливается цветами, смайлик моргает, солнце крутит лучами, етс.
# Задержку в анимировании все равно надо ставить, пусть даже 0.01 сек - так библиотека устойчивей работает.

import simple_draw as sd
from village_morning_static.house import house
from village_morning_static.tree import tree
from village_morning_anim.rainbow import rainbow
from village_morning_anim.sun import sun
from village_morning_anim.face import face
from village_morning_anim.snowfall import snowfall

sd.caption = 'Village morning (anim)'
resolution_x, resolution_y = 1600, 1000
sd.resolution = (resolution_x, resolution_y)
sd.background_color = sd.COLOR_DARK_BLUE

ground_height = 100
house_shift_x = 300
ground_point_1 = sd.get_point(0, 0)
ground_point_2 = sd.get_point(resolution_x, ground_height)
tree_root = sd.get_point(resolution_x * 4 / 5, ground_height)
rainbow_colors = [sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE]
sun_angle = 0
eye_blink = 0
snowflakes = []
snowflakes_quantity = 50

for _ in range(snowflakes_quantity):
    x = sd.random_number(0 - resolution_y, house_shift_x - resolution_y)
    y = sd.random_number(resolution_y - 200, resolution_y)
    length = sd.random_number(5, 15)
    snowflakes.append([x, y, length])

# Static draw
sd.start_drawing()
window_returns = house(house_shift_x=house_shift_x)
face_x = (window_returns[0] + window_returns[2]) / 2
face_y = (window_returns[1] + window_returns[3]) / 2
window_color = window_returns[4]
tree(start_point=tree_root)
sd.finish_drawing()

# Anim draw
while True:
    sd.start_drawing()
    rainbow(rainbow_colors=rainbow_colors)
    rainbow_colors.insert(0, rainbow_colors.pop(6))
    sun(color=sd.background_color, rotate_angle=sun_angle)
    if sun_angle > 360:
        sun_angle -= 350
    else:
        sun_angle += 10
    sun(rotate_angle=sun_angle)
    face(face_x, face_y, window_color, eye_blink)
    eye_blink = sd.random_number(0, 4)
    face(face_x, face_y, sd.COLOR_WHITE, eye_blink)
    snowfall(snowflakes=snowflakes, ground_height=ground_height, house_shift_x=house_shift_x)
    sd.rectangle(ground_point_1, ground_point_2, sd.COLOR_DARK_GREEN)
    sd.sleep(0.1)
    sd.finish_drawing()
    if sd.user_want_exit():
        break

sd.pause()

