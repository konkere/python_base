# -*- coding: utf-8 -*-

# Есть словарь кодов товаров

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

# Есть словарь списков количества товаров на складе.

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# Каждая запись отображает сколько и по какой цене закупалось товаров.
#
# Задание: вывести суммарную стоимость каждого ВИДА товара на складе c помощью циклов
#
# Формат вывода:
#   <товар_1> - <кол-во_товара_1> шт, стоимость <общая_стоимость_товара_1> руб
#   <товар_2> - <кол-во_товара_2> шт, стоимость <общая_стоимость_товара_2> руб
#   <товар_4> - <кол-во_товара_3> шт, стоимость <общая_стоимость_товара_3> руб
#
# Например:
#   Стул - 1111 шт, стоимость 8888 руб
#   Диван - 2222 шт, стоимость 9999 руб
#   и так далее
#
# Алгоритм должен получиться приблизительно такой:
#
# цикл for по товарам с получением кода и названия товара
#     инициализация переменных для подсчета количества и стоимости товара
#     получение списка на складе по коду товара
#     цикл for по списку на складе
#         подсчет количества товара
#         подсчет стоимости товара
#     вывод на консоль количества и стоимости товара на складе


def quantity_and_cost(name_of_goods):
    goods_positions = len(store[goods[name_of_goods]])
    goods_quantity, goods_cost = 0, 0
    for i in range(goods_positions):
        goods_quantity += store[goods[name_of_goods]][i]['quantity']
        goods_cost += store[goods[name_of_goods]][i]['price'] * store[goods[name_of_goods]][i]['quantity']
    return goods_quantity, goods_cost


print('Лампа -', quantity_and_cost('Лампа')[0], 'шт., стоимость', quantity_and_cost('Лампа')[1], 'руб.')
print('Стол -', quantity_and_cost('Стол')[0], 'шт., стоимость', quantity_and_cost('Стол')[1], 'руб.')
print('Диван -', quantity_and_cost('Диван')[0], 'шт., стоимость', quantity_and_cost('Диван')[1], 'руб.')
print('Стул -', quantity_and_cost('Стул')[0], 'шт., стоимость', quantity_and_cost('Стул')[1], 'руб.')
