#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pprint import pprint

# Есть словарь координат городов

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


# Создаём переменные координат каждого города, X и Y, для облегчения читабельности
moscow_x, moscow_y = sites['Moscow'][0], sites['Moscow'][1]
london_x, london_y = sites['London'][0], sites['London'][1]
paris_x, paris_y = sites['Paris'][0], sites['Paris'][1]

# Вычисляем расстояния между городами в обе (не обязательно, но на случай пополнения кода в будущем) стороны
moscow2london = london2moscow = ((moscow_x - london_x) ** 2 + (moscow_y - london_y) ** 2) ** 0.5
moscow2paris = paris2moscow = ((moscow_x - paris_x) ** 2 + (moscow_y - paris_y) ** 2) ** 0.5
paris2london = london2paris = ((paris_x - london_x) ** 2 + (paris_y - london_y) ** 2) ** 0.5

# Пополняем словарь расстояний между городами
distances = {'Moscow': {'London': moscow2london, 'Paris': moscow2paris},
             'London': {'Moscow': london2moscow, 'Paris': london2paris},
             'Paris': {'Moscow': paris2moscow, 'London': paris2london}
             }

# Смотрим вывод всего словаря с расстояниями
pprint(distances)

# зачет!
