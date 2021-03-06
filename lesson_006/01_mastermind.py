# -*- coding: utf-8 -*-

# Игра «Быки и коровы»
# https://goo.gl/Go2mb9
#
# Правила:
# Компьютер загадывает четырехзначное число, все цифры которого различны
# (первая цифра числа отлична от нуля). Игроку необходимо разгадать задуманное число.
# Игрок вводит четырехзначное число c неповторяющимися цифрами,
# компьютер сообщают о количестве «быков» и «коров» в названном числе
# «бык» — цифра есть в записи задуманного числа и стоит в той же позиции,
#       что и в задуманном числе
# «корова» — цифра есть в записи задуманного числа, но не стоит в той же позиции,
#       что и в задуманном числе
#
# Например, если задумано число 3275 и названо число 1234,
# получаем в названном числе одного «быка» и одну «корову».
# Очевидно, что число отгадано в том случае, если имеем 4 «быка».
#
# Формат ответа компьютера
# > быки - 1, коровы - 1


# Составить отдельный модуль mastermind_engine, реализующий функциональность игры.
# В mastermind_engine нужно реализовать функции:
#   загадать_число()
#   проверить_число(NN) - возвращает словарь {'bulls': N, 'cows': N}
# Загаданное число хранить в глобальной переменной.
# Обратите внимание, что строки - это список символов.
#
# В текущем модуле (lesson_006/01_mastermind.py) реализовать логику работы с пользователем:
#   модуль движка загадывает число
#   в цикле, пока число не отгадано
#       у пользователя запрашивается вариант числа
#       проверяем что пользователь ввел допустимое число (4 цифры, все цифры разные, не начинается с 0)
#       модуль движка проверяет число и выдает быков/коров
#       результат быков/коров выводится на консоль
#  когда игрок угадал таки число - показать количество ходов и вопрос "Хотите еще партию?"
#
# При написании кода учитывайте, что движок игры никак не должен взаимодействовать с пользователем.
# Все общение с пользователем (вывод на консоль и запрос ввода от пользователя) делать в 01_mastermind.py.
# Движок игры реализует только саму функциональность игры. Разделяем: mastermind_engine работает
# только с загаданным числом, а 01_mastermind - с пользователем и просто передает числа на проверку движку.
# Это пример применения SOLID принципа (см https://goo.gl/GFMoaI) в архитектуре программ.
# Точнее, в этом случае важен принцип единственной ответственности - https://goo.gl/rYb3hT

from termcolor import cprint
from mastermind_engine import pick_secret_number, check_secret_number, check_user_number, check_to_win

continue_game = ['yes', 'y', 'да', 'д']
user_turn = 0
secret_number = pick_secret_number()


def input_user_number():
    global user_number
    while not check_user_number(user_number):
        user_number = input('Попытка №{0}: '.format(user_turn))


def question_to_continue():
    user_continue_game = input('Сыграем ещё? [y/n] ')
    if user_continue_game not in continue_game:
        print('До новых встреч!')
        exit(0)


def end_game(user_turn):
    cprint('Побeда! Ходов сделано: {0}.'.format(user_turn), color='magenta')


cprint('Я загадал 4-значное число (первая цифра не ноль, все цифры уникальны).', color='green')
cprint('Попробуешь угадать?', color='green')

while True:
    user_number = ''
    user_turn += 1
    input_user_number()
    bulls_and_cows = check_secret_number(user_number)
    cprint('Быков: {0}, коров: {1}'.format(bulls_and_cows['bulls'], bulls_and_cows['cows']), color='yellow')
    win_game = check_to_win(bulls_and_cows['bulls'])
    if win_game:
        end_game(user_turn)
        question_to_continue()
        secret_number = pick_secret_number()
        user_turn = 0
        cprint('Я загадал ещё одно 4-значное число.', color='green')


# зачет!
