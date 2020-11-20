# -*- coding: utf-8 -*-
from random import randint

secret_number = []


def pick_secret_number():
    global secret_number
    secret_digit = randint(1, 9)
    secret_number.append(secret_digit)
    for digit in range(2, 5):
        while secret_digit in secret_number:
            secret_digit = randint(0, 9)
        else:
            secret_number.append(secret_digit)
    return secret_number


def check_secret_number(user_number):
    user_number_as_digits = list(map(int, user_number))
    bulls, cows = 0, 0
    for digit in range(0, 4):
        if user_number_as_digits[digit] in secret_number:
            cows += 1
    for digit in range(0, 4):
        if user_number_as_digits[digit] == secret_number[digit]:
            bulls += 1
    cows -= bulls
    return bulls, cows


def check_user_number(user_number):
    if (user_number.isdigit()) and (999 < int(user_number) < 10000):
        user_number_list = list(map(int, user_number))
        user_number_set = set(user_number_list)
        return len(user_number_list) == len(user_number_set)
    return False
