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

# TODO чтобы не писать вот так, запишем через for _ in range(N): сократим пару 10-ок строк
# TODO Для начало сформирует нужный нам список списков, объявим его до цикла
# TODO Используя цикл фор _ in range(N): в нем
# TODO x,y,length будем получать используя допустим x = sd.random_number(100,1200), y = sd.random_number(500, 600),
#  length = sd.random_number(10,100)
# TODO Создадим один общий список списков и назовем его параметры_снежинок.добавить([x,y,length])
snowflake_x = []
snowflake_y = []
snowflake_length = []
snowflake_speed = 10
for _ in range(N):
    snowflake_x.append(sd.random_number(0, resolution_x))
    snowflake_y.append(sd.random_number(resolution_y - 300, resolution_y))
    snowflake_length.append(sd.random_number(10, 100))

# -= Задание 1 =- ---------------------начало------------------------
while True:
    sd.clear_screen()
    for i in range(N):
        # TODO тут подкорректировать!
        x = snowflake_x[i]
        y = snowflake_y[i]
        sd.snowflake(center=sd.get_point(x, y), length=snowflake_length[i])
        if y > snowflake_length[i]:
            # TODO списку по индексу снежинки присваиваем сразу 600 - верхняя граница чтобы она от туда падала!
            y = snowflake_y.pop(i) - snowflake_speed
            snowflake_y.insert(i, y)
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
#     for i in range(N):
#         x = snowflake_x[i]
#         y = snowflake_y[i]
#         if y > snowflake_length[i]:
#             sd.snowflake(center=sd.get_point(x, y), length=snowflake_length[i], color=sd.background_color)
#             y = snowflake_y.pop(i) - snowflake_speed
#             snowflake_y.insert(i, y)
#         sd.snowflake(center=sd.get_point(x, y), length=snowflake_length[i])
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
snowdrift = []

while True:
    sd.start_drawing()
    for i in range(N):
        x = snowflake_x[i]
        y = snowflake_y[i]
        if y > snowflake_length[i]:
            sd.snowflake(center=sd.get_point(x, y), length=snowflake_length[i], color=sd.background_color)
            y = snowflake_y.pop(i) - snowflake_speed
            snowflake_y.insert(i, y)
            x = snowflake_x.pop(i) + sd.random_number(-20, 20)
            snowflake_x.insert(i, x)
        else:
            if i in snowdrift:
                pass
            else:
                snowflake_x.append(sd.random_number(0, resolution_x))
                snowflake_y.append(sd.random_number(resolution_y - 300, resolution_y))
                snowflake_length.append(sd.random_number(10, 100))
                N += 1
                snowdrift.append(i)
        sd.snowflake(center=sd.get_point(x, y), length=snowflake_length[i])
    sd.finish_drawing()
    sd.sleep(0.1)
    if sd.user_want_exit():
        break
# -= Задание 3 (усложненное) =- ---------------------конец------------------------

sd.pause()
