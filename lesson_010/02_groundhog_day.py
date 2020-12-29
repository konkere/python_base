# -*- coding: utf-8 -*-

# День сурка
#
# Напишите функцию one_day() которая возвращает количество кармы от 1 до 7
# и может выкидывать исключения:
# - IamGodError
# - DrunkError
# - CarCrashError
# - GluttonyError
# - DepressionError
# - SuicideError
# Одно из этих исключений выбрасывается с вероятностью 1 к 13 каждый день
#
# Функцию оберните в бесконечный цикл, выход из которого возможен только при накоплении
# кармы до уровня ENLIGHTENMENT_CARMA_LEVEL. Исключения обработать и записать в лог.
# При создании собственных исключений максимально использовать функциональность
# базовых встроенных исключений.

from random import randint


class GroundhogError(Exception):

    def __init__(self):
        self.message = ''

    def __str__(self):
        return self.message


class IamGodError(GroundhogError):

    def __init__(self):
        self.message = 'Азъ есмь Бог!'


class DrunkError(GroundhogError):

    def __init__(self):
        self.message = 'Алкогольная интоксикация'


class CarCrashError(GroundhogError):

    def __init__(self):
        self.message = 'Погиб в автокатастрофе'


class GluttonyError(GroundhogError):

    def __init__(self):
        self.message = 'Обжорство сгубило'


class DepressionError(GroundhogError):

    def __init__(self):
        self.message = 'Большое депрессивное расстройство'


class SuicideError(GroundhogError):

    def __init__(self):
        self.message = 'Покончил с собой'


def one_day():
    day_carma = randint(1, 7)
    day_error_dice = randint(0, 13)
    if day_error_dice == 13:
        # TODO используем из random choice выбираем ошибку и только потом вызываем ()
        raise error_rnd()
    return day_carma


def error_rnd():
    # TODO список выносим в глобальную область, список у нас будет из объектов без ()
    errors = [
        IamGodError(),
        DrunkError(),
        CarCrashError(),
        GluttonyError(),
        DepressionError(),
        SuicideError(),
    ]
    return errors[randint(0, 5)]


ENLIGHTENMENT_CARMA_LEVEL = 777
day = 0
carma = 0

# TODO нужно написать функцию которая будет записывать логи в функцию

while carma < ENLIGHTENMENT_CARMA_LEVEL:
    day += 1
    print(f'-===== День {day} =====-')
    try:
        carma += one_day()
    # TODO тут мы должны отлавливать каждую ошибку, наполнять список и потом записать все в файл
    except GroundhogError as exc:
        print(f'{exc}')
    print(f'Карма: {carma}')

print(f'Просветление произошло на {day} день')

# https://goo.gl/JnsDqu
