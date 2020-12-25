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
        self.sort_by()
        self.table_stat()

    def parse_line(self, line):
        for char in line:
            if char.isalpha() and char in self.stat:
                self.stat[char] += 1
            elif char.isalpha() and char not in self.stat:
                self.stat[char] = 1

    def sort_by(self):
        # frequency decrease
        self.letters_sort = sorted(self.stat.items(), key=lambda item: item[1], reverse=True)

    def table_stat(self):
        letters_summ = 0
        print('╔' + '═' * 7 + '╤' + '═' * 9 + '╗')
        print('║{letter:^7}│{quantity:^9}║'.format(letter='буква', quantity='частота'))
        print('╠' + '═' * 7 + '╪' + '═' * 9 + '╣')
        for number, [letter, quantity] in enumerate(self.letters_sort):
            letters_summ += quantity
            print('║{letter:^7}│{quantity:^9}║'.format(letter=letter, quantity=quantity))
            print('╟' + '─' * 7 + '┼' + '─' * 9 + '╢')
        print('║{letters:^7}╪{summ:^9}║'.format(letters='Итого', summ=letters_summ))
        print('╚' + '═' * 7 + '╧' + '═' * 9 + '╝')


class LettersStatFrequencyUp(LettersStat):

    def sort_by(self):
        # frequency increase
        self.letters_sort = sorted(self.stat.items(), key=lambda item: item[1])


class LettersStatAlphabetDown(LettersStat):

    def sort_by(self):
        # alphabet decrease
        self.letters_sort = sorted(self.stat.items(), key=lambda item: item[0], reverse=True)


class LettersStatAlphabetUp(LettersStat):

    def sort_by(self):
        # alphabet increase
        self.letters_sort = sorted(self.stat.items(), key=lambda item: item[0])


letters_frequency_decrease = LettersStat(file_name='python_snippets/voyna-i-mir.txt.zip')
letters_frequency_decrease.parse_file()

# letters_frequency_increase = LettersStatFrequencyUp(file_name='python_snippets/voyna-i-mir.txt.zip')
# letters_frequency_increase.parse_file()

# letters_alphabet_decrease = LettersStatAlphabetDown(file_name='python_snippets/voyna-i-mir.txt.zip')
# letters_alphabet_decrease.parse_file()

# letters_alphabet_increase = LettersStatAlphabetUp(file_name='python_snippets/voyna-i-mir.txt.zip')
# letters_alphabet_increase.parse_file()

# После зачета первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
