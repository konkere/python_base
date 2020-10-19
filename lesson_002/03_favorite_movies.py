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
# Есть вариант взять с конца строки отрицательным индексом [-15:]
film_5 = my_favorite_movies[-15:]

# Я думал, списком красивее. Потом просто по заданию вписывать соответсвующие цифры.
# В задании же как? Не просто "первый/третий", а также "последний/второй с конца".
# Ну, вроде как: надо последний? Вот - [-1]

# По вопросу использования list в названии списка.
# В задании 08_garden точно также используется зарезервированное set,
# предложенное его, задания, автором. Видимо, там его стоит поменять,
# чтобы не смущать учеников.

print(f"""Вариант с f:
{film_1}
{film_5}
{film_2}
{film_4}
""")
print('Вариант с sep:', film_1, film_5, film_2, film_4, sep='\n')
