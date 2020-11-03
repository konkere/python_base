# -*- coding: utf-8 -*-

import simple_draw as sd

resolution_x = 800
resolution_y = 600
sd.resolution = (resolution_x, resolution_y)
sd.caption = 'Snowfall'

# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длин лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

N = 20

# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()

snowflakes = []
snowflake_speed = 10

for _ in range(N):
    x = sd.random_number(0, resolution_x)
    y = sd.random_number(resolution_y - 200, resolution_y)
    length = sd.random_number(10, 100)
    snowflakes.append([x, y, length])

# -= Задание 1 =- ---------------------начало------------------------
while True:
    sd.clear_screen()
    for snowflake_number in range(N):
        x = snowflakes[snowflake_number][0]
        y = snowflakes[snowflake_number][1]
        length = snowflakes[snowflake_number][2]
        sd.snowflake(center=sd.get_point(x, y), length=length)
        if y > length:
            # TODO списку по индексу снежинки присваиваем сразу 600 - верхняя граница чтобы она оттуда падала!
            # Я вот эту тудушку не очень понял. Это же не про "нарисовать сверху новую снежинку, когда предыдущая упала"
            # Тут просто отрисовывается падение: "если 'y' не близок к нулю, то уменьшать его"
            # Это наверное было про 3-ю часть?
            y = snowflakes.pop(snowflake_number)[1] - snowflake_speed
            snowflakes.insert(snowflake_number, [x, y, length])
    sd.sleep(0.1)
    if sd.user_want_exit():
        break
# -= Задание 1 =- ---------------------конец------------------------

# Примерный алгоритм отрисовки снежинок
#   навсегда
#     очистка экрана
#     для индекс, координата_х из списка координат снежинок
#       получить координата_у по индексу
#       изменить координата_у и запомнить её в списке по индексу
#       создать точку отрисовки снежинки по координатам
#       нарисовать снежинку белым цветом в этой точке
#     немного поспать
#     если пользователь хочет выйти
#       прервать цикл


# TODO Часть 2 (делается после зачета первой части)
# Да ): Но я не удержался и сейчас её тоже пофиксил в соответсвии с текущим видом части 1
#
# Ускорить отрисовку снегопада
# - убрать clear_screen() из цикла: полная очистка всего экрана - долгая операция.
# - использовать хак для стирания старого положения снежинки:
#       отрисуем её заново на старом месте, но цветом фона (sd.background_color) и она исчезнет!
# - использовать функции sd.start_drawing() и sd.finish_drawing()
#       для начала/окончания отрисовки кадра анимации
# - между start_drawing и finish_drawing библиотека sd ничего не выводит на экран,
#       а сохраняет нарисованное в промежуточном буфере, за счет чего достигается ускорение анимации
# - в момент вызова finish_drawing все нарисованное в буфере разом покажется на экране
#
# Примерный алгоритм ускоренной отрисовки снежинок
#   навсегда
#     начать рисование кадра
#     для индекс, координата_х из списка координат снежинок
#       получить координата_у по индексу
#       создать точку отрисовки снежинки
#       нарисовать снежинку цветом фона
#       изменить координата_у и запомнить её в списке по индексу
#       создать новую точку отрисовки снежинки
#       нарисовать снежинку на новом месте белым цветом
#     закончить рисование кадра
#     немного поспать
#     если пользователь хочет выйти
#       прервать цикл

# -= Задание 2 =- ---------------------начало------------------------
# while True:
#     sd.start_drawing()
#     for snowflake_number in range(N):
#         x = snowflakes[snowflake_number][0]
#         y = snowflakes[snowflake_number][1]
#         length = snowflakes[snowflake_number][2]
#         if y > length:
#             sd.snowflake(center=sd.get_point(x, y), length=length, color=sd.background_color)
#             y = snowflakes.pop(snowflake_number)[1] - snowflake_speed
#             snowflakes.insert(snowflake_number, [x, y, length])
#         sd.snowflake(center=sd.get_point(x, y), length=length)
#     sd.finish_drawing()
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break
# -= Задание 2 =- ---------------------конец------------------------

# Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg

# -= Задание 3 (усложненное) =- ---------------------начало------------------------
# Тоже причесал

# snowdrift = []
#
# while True:
#     sd.start_drawing()
#     for snowflake_number in range(N):
#         x = snowflakes[snowflake_number][0]
#         y = snowflakes[snowflake_number][1]
#         length = snowflakes[snowflake_number][2]
#         if y > length:
#             sd.snowflake(center=sd.get_point(x, y), length=length, color=sd.background_color)
#             x = snowflakes[snowflake_number][0] + sd.random_number(-20, 20)
#             y = snowflakes.pop(snowflake_number)[1] - snowflake_speed
#             snowflakes.insert(snowflake_number, [x, y, length])
#         else:
#             if snowflake_number in snowdrift:
#                 pass
#             else:
#                 x = sd.random_number(0, resolution_x)
#                 y = resolution_y
#                 length = sd.random_number(10, 100)
#                 snowflakes.append([x, y, length])
#                 N += 1
#                 snowdrift.append(snowflake_number)
#         sd.snowflake(center=sd.get_point(x, y), length=length)
#     sd.finish_drawing()
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break
# -= Задание 3 (усложненное) =- ---------------------конец------------------------

sd.pause()
