# -*- coding: utf-8 -*-

import os
import time
import shutil
import zipfile

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

    def __init__(self, origin_path, sorted_dir):
        self.origin_path = os.path.normpath(origin_path)
        self.sorted_dir = os.path.normpath(sorted_dir)
        self.check_dir_exist(self.sorted_dir)
        self.go()

    def check_dir_exist(self, dir):
        if not os.path.exists(dir):
            os.makedirs(dir)

    def go(self):
        for dir_path, dir_names, filenames in os.walk(self.origin_path):
            for file_name in filenames:
                file_path = os.path.join(dir_path, file_name)
                file_unixtime = os.path.getmtime(file_path)
                file_time = time.gmtime(file_unixtime)
                self.sort_file(dir_path, file_name, str(file_time[0]), str(file_time[1]))

    def sort_file(self, dir_path, file_name, year, month):
        origin_file = os.path.join(dir_path, file_name)
        destination_dir = os.path.join(self.sorted_dir, year, month)
        destination_file = os.path.join(destination_dir, file_name)
        self.check_dir_exist(destination_dir)
        if not os.path.exists(destination_file):
            shutil.copy2(origin_file, destination_dir)


class FileSorterFromZip(FileSorter):

    def go(self):
        with zipfile.ZipFile(f'{self.origin_path}', 'r') as zfile:
            zip_list = zfile.infolist()
            for element in zip_list:
                if element.file_size > 0:
                    year = str(element.date_time[0])
                    month = str(element.date_time[1])
                    self.sort_file(zfile, element, year, month)

    def sort_file(self, zfile, element, year, month):
        date_time = time.mktime(element.date_time + (0, 0, 0))
        destination_dir = os.path.join(self.sorted_dir, year, month)
        self.check_dir_exist(destination_dir)
        element.filename = os.path.basename(element.filename)
        destination_file = os.path.join(destination_dir, element.filename)
        zfile.extract(element, destination_dir)
        os.utime(path=destination_file, times=(date_time, date_time))


# file_sorter = FileSorter('./icons', './icons_by_year')
file_sorter = FileSorterFromZip('./icons.zip', './icons_by_year')

# Усложненное задание (делать по желанию)
# Нужно обрабатывать zip-файл, содержащий фотографии, без предварительного извлечения файлов в папку.
# Это относится только к чтению файлов в архиве. В случае паттерна "Шаблонный метод" изменяется способ
# получения данных (читаем os.walk() или zip.namelist и т.д.)
# Документация по zipfile: API https://docs.python.org/3/library/zipfile.html
