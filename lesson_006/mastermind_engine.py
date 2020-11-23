# -*- coding: utf-8 -*-
from random import randint

secret_number = None


def pick_secret_number():
    global secret_number
    secret_number_digits = [0]
    secret_number_digits_uniq = {}
    while not len(secret_number_digits) == len(secret_number_digits_uniq):
        secret_number = randint(1000, 9999)
        secret_number_digits = list(map(int, str(secret_number)))
        secret_number_digits_uniq = set(secret_number_digits)
    # print(secret_number)


def check_secret_number(user_number):
    user_number_digits = list(map(int, user_number))
    secret_number_digits = list(map(int, str(secret_number)))
    bulls_and_cows = {'bulls': 0, 'cows': 0}
    for digit in range(0, 4):
        if user_number_digits[digit] in secret_number_digits:
            bulls_and_cows['cows'] += 1
    for digit in range(0, 4):
        if user_number_digits[digit] == secret_number_digits[digit]:
            bulls_and_cows['bulls'] += 1
    bulls_and_cows['cows'] -= bulls_and_cows['bulls']
    return bulls_and_cows


def check_user_number(user_number):
    if (user_number.isdigit()) and (999 < int(user_number) < 10000):
        user_number_digits = list(map(int, user_number))
        user_number_digits_uniq = set(user_number_digits)
        return len(user_number_digits) == len(user_number_digits_uniq)
    return False


def check_to_win(bulls):
    if bulls == 4:
        return True
    else:
        return False
