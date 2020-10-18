#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть строка с перечислением фильмов

my_favorite_movies = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'

# Выведите на консоль с помощью индексации строки, последовательно:
#   первый фильм
#   последний
#   второй
#   второй с конца

# Запятая не должна выводиться.  Переопределять my_favorite_movies нельзя
# Использовать .split() или .find()или другие методы строки нельзя - пользуйтесь только срезами,
# как указано в задании!

film_1 = my_favorite_movies[:10]
film_2 = my_favorite_movies[12:25]
film_3 = my_favorite_movies[27:33]
film_4 = my_favorite_movies[35:40]
film_5 = my_favorite_movies[42:]

film_list = [film_1, film_2, film_3, film_4, film_5]

print(film_list[0] + '\n' + film_list[-1] + '\n' + film_list[1] + '\n' + film_list[-2])