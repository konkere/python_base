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
# while True:
#     sd.clear_screen()
#     for snowflake_number in range(N):
#         x = snowflakes[snowflake_number][0]
#         y = snowflakes[snowflake_number][1]
#         length = snowflakes[snowflake_number][2]
#         sd.snowflake(center=sd.get_point(x, y), length=length)
#         if y > length:
#             y = snowflakes.pop(snowflake_number)[1] - snowflake_speed
#             snowflakes.insert(snowflake_number, [x, y, length])
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break
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

# Объявляем наш будущий сугроб
# snowdrift = []
#
# while True:
#     # Входим в режим 'не рисовать всё ниженаписанное до команды'
#     sd.start_drawing()
#     # Перебираем все снежинки, которые у нас есть на данный момент
#     for snowflake_number in range(N):
#         # Забираем для каждой из них текущие координаты и длину лучей
#         x = snowflakes[snowflake_number][0]
#         y = snowflakes[snowflake_number][1]
#         length = snowflakes[snowflake_number][2]
#         # Создаём проверку на приближение к нижней границе экрана. Если координата 'y' больше длины лучей данной
#         # снежинки, значит она должна продолжать своё падение
#         if y > length:
#             # Рисуем поверх нашей снежинки бэкграунд, потом меняем координаты
#             # 'х' - со смещением случайным образом чуть в одну из сторон, а 'y' - со смещением на 'скорость падения'
#             # вниз. При этом изымаем [список снежинки] из общего [списка всех снежинок] и ставим на ту же позицию
#             # [список снежинки] с новыми обновлёнными координатами
#             sd.snowflake(center=sd.get_point(x, y), length=length, color=sd.background_color)
#             x = snowflakes[snowflake_number][0] + sd.random_number(-20, 20)
#             y = snowflakes.pop(snowflake_number)[1] - snowflake_speed
#             snowflakes.insert(snowflake_number, [x, y, length])
#         # А тут у нас случай, когда снежинка достигла нижней границы экрана
#         # 'y' стал меньше или равен длине лучей снежинки
#         else:
#             # Если наша снежинка уже занесена в специальный список [сугроба], т.е. уже там лежит какое-то время,
#             # то ничего с ней не делаем, всё хорошо, пусть и дальше лежит
#             if snowflake_number in snowdrift:
#                 pass
#             # А вот если наша снежинка до этого находилась в полёте и только сейчас достигла нижней части экрана,
#             # тогда создаём наверху новую снежинку со случайной координатой 'x'
#             # и случайной длиной лучей (между 10 и 100). Потом добавляем [список новой снежинки]
#             # в общий [список всех снежинок], не забыв поменять N, чтобы в следующем цикле она тоже поучаствовала.
#             # А старую, которая упала, заносим в специальный список [сугроба], чтобы знать, что в следующем цикле
#             # при её проверке уже не нужно создавать новую снежинку
#             else:
#                 x = sd.random_number(0, resolution_x)
#                 y = resolution_y
#                 length = sd.random_number(10, 100)
#                 snowflakes.append([x, y, length])
#                 N += 1
#                 snowdrift.append(snowflake_number)
#         # Ну и рисуем снежинку (даже если она уже лежит в сугробе, иначе падающие снежинки её покорёжат из-за того,
#         # что они каждый раз 'затираются' путём отрисовки поверх цветом бэкграунда
#         sd.snowflake(center=sd.get_point(x, y), length=length)
#     # Отрисовываем всё то, что наваяли в цикле
#     sd.finish_drawing()
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break
# -= Задание 3 (усложненное) =- ---------------------конец------------------------

# -= Задание 3 v2 (усложненное) =- ---------------------начало------------------------
# Предыдущий вариант мне нравится из-за отсутствия артефактов у упавших снежинок. Да, тому сугробу нужно ограничение,
# чтобы количество снежинок в списке_списков не разрасталось бесконечно.
# А этот вариант нравится подрастанием сугроба (поднятием границы).
# Думаю, если их 'идеи' слить вместе, было бы прекрасно. Но опять вернёмся к повышению вложенности.

length_snow = 50

while True:
    sd.start_drawing()
    for i in range(N):
        x = snowflakes[i][0]
        y = snowflakes[i][1]
        length = snowflakes[i][2]
        snowflake_point = sd.get_point(x, y)
        sd.snowflake(snowflake_point, length, color=sd.background_color)
        # тут делаем так
        x += sd.random_number(-20, 20)
        y -= snowflake_speed
        snowflake_point = sd.get_point(x, y)
        sd.snowflake(snowflake_point, length)
        # а тут так
        snowflakes[i] = [x, y, length]
        if y < length_snow:
            snowflakes[i][1] = resolution_y
            length_snow += 1
        elif length_snow > 400:
            length_snow = 400
    sd.finish_drawing()
    sd.sleep(0.1)
    if sd.user_want_exit():
        break
# -= Задание 3 v2 (усложненное) =- ---------------------конец------------------------

sd.pause()

# зачет!
