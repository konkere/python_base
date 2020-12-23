# -*- coding: utf-8 -*-

import os
import time
import shutil

# Нужно написать скрипт для упорядочивания фотографий (вообще любых файлов)
# Скрипт должен разложить файлы из одной папки по годам и месяцам в другую.
# Например, так:
#   исходная папка
#       icons/cat.jpg
#       icons/man.jpg
#       icons/new_year_01.jpg
#   результирующая папка
#       icons_by_year/2018/05/cat.jpg
#       icons_by_year/2018/05/man.jpg
#       icons_by_year/2017/12/new_year_01.jpg
#
# Входные параметры основной функции: папка для сканирования, целевая папка.
# Имена файлов в процессе работы скрипта не менять, год и месяц взять из времени последней модификации файла
# (время создания файла берется по разному в разых ОС - см https://clck.ru/PBCAX - поэтому берем время модификации).
#
# Файлы для работы взять из архива icons.zip - раззиповать проводником ОС в папку icons перед написанием кода.
# Имя целевой папки - icons_by_year (тогда она не попадет в коммит, см .gitignore в папке ДЗ)
#
# Пригодятся функции:
#   os.walk
#   os.path.dirname
#   os.path.join
#   os.path.normpath
#   os.path.getmtime
#   time.gmtime
#   os.makedirs
#   shutil.copy2
#
# Чтение документации/гугла по функциям - приветствуется. Как и поиск альтернативных вариантов :)
#
# Требования к коду: он должен быть готовым к расширению функциональности - делать сразу на классах.
# Для этого пригодится шаблон проектирование "Шаблонный метод"
#   см https://refactoring.guru/ru/design-patterns/template-method
#   и https://gitlab.skillbox.ru/vadim_shandrinov/python_base_snippets/snippets/4


class FileSorter:

    def __init__(self, origin_dir, sorted_dir):
        self.origin_dir = os.path.normpath(origin_dir)
        self.sorted_dir = os.path.normpath(sorted_dir)
        if not os.path.exists(self.sorted_dir):
            os.makedirs(self.sorted_dir)

    def go(self):
        for dir_path, dir_names, filenames in os.walk(self.origin_dir):
            for file_name in filenames:
                file_path = os.path.join(dir_path, file_name)
                file_unixtime = os.path.getmtime(file_path)
                file_time = time.gmtime(file_unixtime)
                self.sort_file(dir_path, file_name, str(file_time[0]), str(file_time[1]))

    def sort_file(self, dir_path, file_name, year, month):
        origin_file = os.path.join(dir_path, file_name)
        destination_dir = os.path.join(self.sorted_dir, year, month)
        destination_file = os.path.join(destination_dir, file_name)
        if not os.path.exists(destination_dir):
            os.makedirs(destination_dir)
        if not os.path.exists(destination_file):
            shutil.copy2(origin_file, destination_dir)


file_sorter = FileSorter('./icons', './icons_by_year')
file_sorter.go()

# Усложненное задание (делать по желанию)
# Нужно обрабатывать zip-файл, содержащий фотографии, без предварительного извлечения файлов в папку.
# Это относится только к чтению файлов в архиве. В случае паттерна "Шаблонный метод" изменяется способ
# получения данных (читаем os.walk() или zip.namelist и т.д.)
# Документация по zipfile: API https://docs.python.org/3/library/zipfile.html
