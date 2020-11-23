# -*- coding: utf-8 -*-
from random import randint
from termcolor import cprint

secret_number = None

# TODO list set dict tuple и так далее зарезервированные слова использовать их не рекомендуется в названии
# TODO подробнее в FAQ
# TODO Поправить нейминг по коду.


def pick_secret_number():
    global secret_number
    secret_number_list = [0]
    secret_number_set = {}
    while not len(secret_number_list) == len(secret_number_set):
        secret_number = randint(1000, 9999)
        secret_number_list = list(map(int, str(secret_number)))
        secret_number_set = set(secret_number_list)
    # print(secret_number)


def check_secret_number(user_number):
    user_number_as_digits = list(map(int, user_number))
    secret_number_as_digits = list(map(int, str(secret_number)))
    bulls_and_cows = {'bulls': 0, 'cows': 0}
    for digit in range(0, 4):
        if user_number_as_digits[digit] in secret_number_as_digits:
            bulls_and_cows['cows'] += 1
    for digit in range(0, 4):
        if user_number_as_digits[digit] == secret_number_as_digits[digit]:
            bulls_and_cows['bulls'] += 1
    bulls_and_cows['cows'] -= bulls_and_cows['bulls']
    return bulls_and_cows


def check_user_number(user_number):
    if (user_number.isdigit()) and (999 < int(user_number) < 10000):
        user_number_list = list(map(int, user_number))
        user_number_set = set(user_number_list)
        return len(user_number_list) == len(user_number_set)
    return False


# TODO тут у нас общение с пользователем в главный модуль
def end_game(user_turn):
    cprint('Побeда! Ходов сделано: {0}.'.format(user_turn), color='magenta')


def check_to_win(bulls):
    if bulls == 4:
        return True
    else:
        return False
