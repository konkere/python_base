# -*- coding: utf-8 -*-

# Подсчитать статистику по буквам в романе Война и Мир.
# Входные параметры: файл для сканирования
# Статистику считать только для букв алфавита (см функцию .isalpha() для строк)
#
# Вывести на консоль упорядоченную статистику в виде
# +---------+----------+
# |  буква  | частота  |
# +---------+----------+
# |    А    |   77777  |
# |    Б    |   55555  |
# |   ...   |   .....  |
# |    a    |   33333  |
# |    б    |   11111  |
# |   ...   |   .....  |
# +---------+----------+
# |  итого  | 9999999  |
# +---------+----------+
#
# Упорядочивание по частоте - по убыванию. Ширину таблицы подберите по своему вкусу
#
# Требования к коду: он должен быть готовым к расширению функциональности - делать сразу на классах.
# Для этого пригодится шаблон проектирование "Шаблонный метод"
#   см https://refactoring.guru/ru/design-patterns/template-method
#   и https://gitlab.skillbox.ru/vadim_shandrinov/python_base_snippets/snippets/4

import zipfile


class LettersStat:

    def __init__(self, file_name):
        self.file_name = file_name
        self.stat = {}
        if self.file_name.endswith('.zip'):
            self.unzip()
        self.letters_sort = []

    def unzip(self):
        zfile = zipfile.ZipFile(self.file_name, 'r')
        for filename in zfile.namelist():
            zfile.extract(filename)
        self.file_name = filename

    def parse_file(self):
        with open(self.file_name, 'r', encoding='cp1251') as file:
            for line in file:
                self.parse_line(line)

    def parse_line(self, line):
        for char in line:
            if char.isalpha() and char in self.stat:
                self.stat[char] += 1
            elif char.isalpha() and char not in self.stat:
                self.stat[char] = 1

    # TODO оставляем этот метод, и пишем в нем дефолтную сортировку.
    def sort_by(self, sortby):
        if sortby == 'frequency decrease':
            self.letters_sort = sorted(self.stat.items(), key=lambda item: item[1], reverse=True)
        elif sortby == 'frequency increase':
            self.letters_sort = sorted(self.stat.items(), key=lambda item: item[1])
        elif sortby == 'alphabet decrease':
            self.letters_sort = sorted(self.stat.items(), key=lambda item: item[0], reverse=True)
        elif sortby == 'alphabet increase':
            self.letters_sort = sorted(self.stat.items(), key=lambda item: item[0])

    def table_stat(self):
        print('╔' + '═' * 7 + '╤' + '═' * 9 + '╗')
        print('║{letter:^7}│{quantity:^9}║'.format(letter='буква', quantity='частота'))
        print('╠' + '═' * 7 + '╪' + '═' * 9 + '╣')
        for number, [letter, quantity] in enumerate(self.letters_sort):
            print('║{letter:^7}│{quantity:^9}║'.format(letter=letter, quantity=quantity))
            if number < len(self.letters_sort) - 1:
                print('╟' + '─' * 7 + '┼' + '─' * 9 + '╢')
        print('╚' + '═' * 7 + '╧' + '═' * 9 + '╝')

# TODO применим шаблонный метод
# TODO из https://gitlab.skillbox.ru/vadim_shandrinov/python_base_snippets/snippets/4
# TODO тут определяем еще 3 дочерних класса, и в них переопределяем только метод sort_by

# TODO общее количество еще бы знать в таблице.

letters = LettersStat(file_name='python_snippets/voyna-i-mir.txt.zip')
# letters = LettersStat(file_name='voyna-i-mir.txt')
letters.parse_file()
letters.sort_by('frequency decrease')
# letters.sort_by('frequency increase')
# letters.sort_by('alphabet increase')
# letters.sort_by('alphabet decrease')
letters.table_stat()

# После зачета первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
