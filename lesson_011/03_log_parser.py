# -*- coding: utf-8 -*-

# На основе своего кода из lesson_009/02_log_parser.py напишите итератор (или генератор)
# котрый читает исходный файл events.txt и выдает число событий NOK за каждую минуту
# <время> <число повторений>
#
# пример использования:
#
# grouped_events = <создание итератора/генератора>  # Итератор или генератор? выбирайте что вам более понятно
# for group_time, event_count in grouped_events:
#     print(f'[{group_time}] {event_count}')
#
# на консоли должно появится что-то вроде
#
# [2018-05-17 01:57] 1234


def grouped_event_generator(file_in):
    with open(file_in, 'r', encoding='utf8') as file:
        count = 0
        current_date_time = ''
        for line in file:
            if len(line) == 33:
                line_year = line[1:5]
                line_month = line[6:8]
                line_day = line[9:11]
                line_hour = line[12:14]
                line_minute = line[15:17]
                line_date_time = f'{line_year}.{line_month}.{line_day} {line_hour}:{line_minute}'
                if current_date_time == '':
                    current_date_time = line_date_time
                if line_date_time == current_date_time:
                    count += 1
                else:
                    yield current_date_time, count
                    count = 1
                    current_date_time = line_date_time
        if count > 0:
            yield current_date_time, count


grouped_events = grouped_event_generator('events.txt')
for group_time, event_count in grouped_events:
    print(f'[{group_time}] {event_count}')

# зачет!
