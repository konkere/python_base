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

import simple_draw as sd
from village_morning_static.rainbow import rainbow
from village_morning_static.house import house
from village_morning_static.tree import tree
from village_morning_static.face import face
from village_morning_static.snow import snow
from village_morning_static.sun import sun

sd.caption = 'Village morning'
resolution_x, resolution_y = 1600, 1000
sd.resolution = (resolution_x, resolution_y)
sd.background_color = sd.COLOR_DARK_BLUE

ground_height = 100
house_shift_x = 300
ground_point_1 = sd.get_point(0, 0)
ground_point_2 = sd.get_point(resolution_x, ground_height)
tree_root = sd.get_point(resolution_x * 4 / 5, ground_height)

sd.start_drawing()
sd.rectangle(ground_point_1, ground_point_2, sd.COLOR_DARK_GREEN)
rainbow()
window_points = house(house_shift_x=house_shift_x)
tree(start_point=tree_root)
face_x = (window_points[0] + window_points[2]) / 2
face_y = (window_points[1] + window_points[3]) / 2
face(face_x, face_y, sd.COLOR_WHITE)
snow(0, house_shift_x, ground_height, 30, 200)
sun(resolution_y=resolution_y)
sd.finish_drawing()
sd.pause()
# Усложненное задание (делать по желанию)
# Анимировать картину.
# Пусть слева идет снегопад, радуга переливается цветами, смайлик моргает, солнце крутит лучами, етс.
# Задержку в анимировании все равно надо ставить, пусть даже 0.01 сек - так библиотека устойчивей работает.

# Анимированную версию сделал отдельно: 04_painting_anim.py