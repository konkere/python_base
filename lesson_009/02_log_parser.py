# -*- coding: utf-8 -*-

# Имеется файл events.txt вида:
#
# [2018-05-17 01:55:52.665804] NOK
# [2018-05-17 01:56:23.665804] OK
# [2018-05-17 01:56:55.665804] OK
# [2018-05-17 01:57:16.665804] NOK
# [2018-05-17 01:57:58.665804] OK
# ...
#
# Напишите программу, которая считывает файл
# и выводит число событий NOK за каждую минуту в другой файл в формате
#
# [2018-05-17 01:57] 1234
# [2018-05-17 01:58] 4321
# ...
#
# Входные параметры: файл для анализа, файл результата
#
# Требования к коду: он должен быть готовым к расширению функциональности - делать сразу на классах.
# Для этого пригодится шаблон проектирование "Шаблонный метод"
#   см https://refactoring.guru/ru/design-patterns/template-method
#   и https://gitlab.skillbox.ru/vadim_shandrinov/python_base_snippets/snippets/4


class EventsParser:

    def __init__(self, file_in, file_out):
        self.file_in = file_in
        self.file_out = file_out
        self.count = 0
        open(self.file_out, mode='w+').close()

    def parse_file(self):
        with open(self.file_in, 'r', encoding='utf8') as file:
            prev_date_time = ''
            for line in file:
                prev_date_time = self.parse_line(line, prev_date_time)

    def parse_line(self, line, prev_date_time):
        line_year = line[1:5]
        line_month = line[6:8]
        line_day = line[9:11]
        line_hour = line[12:14]
        line_minute = line[15:17]
        line_date_time = f'[{line_year}.{line_month}.{line_day} {line_hour}:{line_minute}]'
        if line_date_time != prev_date_time != '':
            line_out = f'{prev_date_time} {self.count}\n'
            self.write_line(line_out)
            self.count = 0
        if len(line) == 33:
            self.count += 1
        return line_date_time

    def write_line(self, line):
        file_out = open(self.file_out, mode='a')
        file_out.write(line)
        file_out.close()


# TODO 0 нам не нужны в статистике
event_parse = EventsParser('events.txt', 'events_nok_by_min.txt')
event_parse.parse_file()

# TODO этот вариант
# Группировка -- это как с минутами? В этот час/месяц/год столько-то NOKов?

# После зачета первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
