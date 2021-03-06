# -*- coding: utf-8 -*-


# Есть функция генерации списка простых чисел


def get_prime_numbers(n):
    prime_numbers = []
    for number in range(2, n + 1):
        for prime in prime_numbers:
            if number % prime == 0:
                break
        else:
            prime_numbers.append(number)
    return prime_numbers

# Часть 1
# На основе алгоритма get_prime_numbers создать класс итерируемых обьектов,
# который выдает последовательность простых чисел до n
#
# Распечатать все простые числа до 10000 в столбик


class PrimeNumbers:

    def __init__(self, n):
        self.n = n
        self.i = 1
        self.prime_numbers = []

    def __iter__(self):
        self.i = 1
        self.prime_numbers = []
        return self

    def __next__(self):
        self.i += 1
        for number in range(self.i, self.n + 1):
            for prime in self.prime_numbers:
                if number % prime == 0:
                    break
            else:
                self.i = number
                self.prime_numbers.append(self.i)
                return self.i
        raise StopIteration()


# Part 1:
# prime_number_iterator = PrimeNumbers(n=10000)
# for number in prime_number_iterator:
#     print(number)


# Часть 2
# Теперь нужно создать генератор, который выдает последовательность простых чисел до n
# Распечатать все простые числа до 10000 в столбик


def prime_numbers_generator(n, func=None):
    prime_numbers = []
    for number in range(2, n + 1):
        for prime in prime_numbers:
            if number % prime == 0:
                break
        else:
            prime_numbers.append(number)
            if not func:
                yield number
            elif func(number):
                yield number


# Part 2
# for number in prime_numbers_generator(n=10000):
#     print(number)


# Часть 3
# Написать несколько функций-фильтров, которые выдает True, если число:
# 1) "счастливое" в обыденном пониманиии - сумма первых цифр равна сумме последних
#       Если число имеет нечетное число цифр (например 727 или 92083),
#       то для вычисления "счастливости" брать равное количество цифр с начала и конца:
#           727 -> 7(2)7 -> 7 == 7 -> True
#           92083 -> 92(0)83 -> 9+2 == 8+3 -> True
# 2) "палиндромное" - одинаково читающееся в обоих направлениях. Например 723327 и 101
# 3) придумать свою (https://clck.ru/GB5Fc в помощь)
#
# Подумать, как можно применить функции-фильтры к полученной последовательности простых чисел
# для получения, к примеру: простых счастливых чисел, простых палиндромных чисел,
# простых счастливых палиндромных чисел и так далее. Придумать не менее 2х способов.
#
# Подсказка: возможно, нужно будет добавить параметр в итератор/генератор.


def lucky_number(number):
    number_str = str(number)
    half_digits = len(number_str) // 2
    left_sum = 0
    right_sum = 0
    for digit in range(half_digits):
        left_sum += int(number_str[digit])
        right_sum += int(number_str[-1 - digit])
    return left_sum == right_sum


def palindrome_number(number):
    number_str = str(number)
    half_digits = len(number_str) // 2
    for digit in range(half_digits):
        if number_str[digit] != number_str[-1 - digit]:
            return False
    return True


def automorphic_number(number):
    number_exp2 = str(number ** 2)
    number_str = str(number)
    digits = len(number_str)
    for digit in range(digits):
        if number_str[digit] != number_exp2[digit - digits]:
            return False
    return True


# Первый способ (полученные в итераторе простые числа дополнительно проверяем нужными функциями):
# Отстранённое уточнение: все палиндромные числа -- счастливые по сути.
prime_number_iterator = PrimeNumbers(n=10000)
for number in prime_number_iterator:
    if palindrome_number(number):
        print(number)

# Второй способ (передаём нужную функцию аргументом в генератор)
for number in prime_numbers_generator(n=10000, func=palindrome_number):
    print(number)


############################## Просто для теста функций ##############################
# numbers_to_check = [
#     12345,
#     1234,
#     66754,
#     77077,
#     2890625,
#     727,
#     92083,
#     723327,
#     101,
#     56789,
#     109376,
#     376,
# ]
#
# for number in numbers_to_check:
#     count = 0
#     result = f'Число {number} - '
#     if lucky_number(number):
#         result += 'счастливое '
#         count += 1
#     if palindrome_number(number):
#         result += 'палиндром '
#         count += 1
#     if automorphic_number(number):
#         result += 'автоморфное '
#         count += 1
#     if count == 0:
#         result += 'обычное'
#     print(result)
######################################################################################

# зачет!
