# -*- coding: utf-8 -*-

# В очередной спешке, проверив приложение с прогнозом погоды, вы выбежали
# навстречу ревью вашего кода, которое ожидало вас в офисе.
# И тут же день стал хуже - вместо обещанной облачности вас встретил ливень.

# Вы промокли, настроение было испорчено, и на ревью вы уже пришли не в духе.
# В итоге такого сокрушительного дня вы решили написать свою программу для прогноза погоды
# из источника, которому вы доверяете.

# Для этого вам нужно:

# Создать модуль-движок с классом WeatherMaker, необходимым для получения и формирования предсказаний.
# В нём должен быть метод, получающий прогноз с выбранного вами сайта (парсинг + re) за некоторый диапазон дат,
# а затем, получив данные, сформировать их в словарь {погода: Облачная, температура: 10, дата:datetime...}

# Добавить класс ImageMaker.
# Снабдить его методом рисования открытки
# (использовать OpenCV, в качестве заготовки брать lesson_016/python_snippets/external_data/probe.jpg):
#   С текстом, состоящим из полученных данных (пригодится cv2.putText)
#   С изображением, соответствующим типу погоды
# (хранятся в lesson_016/python_snippets/external_data/weather_img ,но можно нарисовать/добавить свои)
#   В качестве фона добавить градиент цвета, отражающего тип погоды
# Солнечно - от желтого к белому
# Дождь - от синего к белому
# Снег - от голубого к белому
# Облачно - от серого к белому

# Добавить класс DatabaseUpdater с методами:
#   Получающим данные из базы данных за указанный диапазон дат.
#   Сохраняющим прогнозы в базу данных (использовать peewee)

# Сделать программу с консольным интерфейсом, постаравшись все выполняемые действия вынести в отдельные функции.
# Среди действий, доступных пользователю, должны быть:
#   Добавление прогнозов за диапазон дат в базу данных
#   Получение прогнозов за диапазон дат из базы
#   Создание открыток из полученных прогнозов
#   Выведение полученных прогнозов на консоль
# При старте консольная утилита должна загружать прогнозы за прошедшую неделю.

# Рекомендации:
# Можно создать отдельный модуль для инициализирования базы данных.
# Как далее использовать эту базу данных в движке:
# Передавать DatabaseUpdater url-путь
# https://peewee.readthedocs.io/en/latest/peewee/playhouse.html#db-url
# Приконнектится по полученному url-пути к базе данных
# Инициализировать её через DatabaseProxy()
# https://peewee.readthedocs.io/en/latest/peewee/database.html#dynamically-defining-a-database


import argparse
from db_updater import DatabaseUpdater
from weather_engine import convert_date
from datetime import datetime, timedelta
from card_maker import ImageMaker, view_pic


def args_parser():
    parser = argparse.ArgumentParser(description='Weather forecasts console script')
    parser.add_argument(
        '-u', '--update',
        action='store_true',
        help='Добавление прогнозов за диапазон дат в базу данных',
        required=False
    )
    parser.add_argument(
        '-r', '--request',
        action='store_true',
        help='Получение прогнозов за диапазон дат из базы',
        required=False,
    )
    parser.add_argument(
        '-c', '--cards',
        action='store_true',
        help='Создание открыток из прогнозов за диапазон дат',
        required=False
    )
    parser.add_argument(
        '-p', '--print',
        action='store_true',
        help='Выведение на консоль прогнозов за диапазон дат',
        required=False
    )
    parser.add_argument('-d', '--date', type=str, help='Дата начала периода', required=False)
    parser.add_argument('-d2', '--date_end', type=str, help='Дата конца периода', required=False)
    args = parser.parse_args().__dict__
    return args


def forecast_to_console(weather):
    date = weather['date'].strftime('%d.%m.%Y')
    temp_day = weather['temp_day']
    temp_night = weather['temp_night']
    phrase = weather['phrase']
    print(f'{date}:\nТемпература днём/ночью: {temp_day}/{temp_night}\n{phrase}\n')


class ConsoleForecasts:

    def __init__(self, args):
        self.args = args
        self.db_upd = DatabaseUpdater('sqlite:///weather.db')
        self.last_week_forecasts()
        self.check_args()
        self.junction_box()

    def last_week_forecasts(self):
        today = datetime.now().date()
        date_start = today - timedelta(days=8)
        date_end = today - timedelta(days=1)
        old_forecasts = self.db_upd.read_entries([date_start, date_end])
        if not old_forecasts:
            print('В базе нет записей о погоде на прошлой неделе.')
        else:
            print('Погода на прошедшей неделе:\n')
            for weather in old_forecasts:
                forecast_to_console(weather)

    def check_args(self):
        if self.args['date']:
            try:
                date = convert_date(self.args['date'])
            except AttributeError:
                print(f'Проверьте правильность введённой даты: {self.args["date"]}')
                exit(1)
            else:
                self.args['date'] = date
        else:
            exit(0)
        if self.args['date_end']:
            try:
                date_end = convert_date(self.args['date_end'])
            except AttributeError:
                print(f'Проверьте правильность введённой даты: {self.args["date_end"]}')
                exit(1)
            else:
                self.args['date_end'] = date_end
        else:
            self.args['date_end'] = self.args['date']

    def junction_box(self):
        dates_range = [self.args['date'], self.args['date_end']]
        entries = self.db_upd.read_entries(dates_range)
        self.arg_update(dates_range)
        self.arg_request(entries)
        self.arg_print(entries)
        self.arg_cards(entries)

    def arg_update(self, dates_range):
        if self.args['update'] and self.args['date']:
            self.db_upd.request_weather(dates_range)
            self.db_upd.write_entries()

    def arg_request(self, entries):
        # Не совсем понял, чем отличаются эти пункты в плане пользовательского опыта при использовании консольной
        # утилиты, поэтому реализовал вывод сырых данных из базы.
        #   Получение прогнозов за диапазон дат из базы
        #   Выведение полученных прогнозов на консоль
        if self.args['request'] and self.args['date']:
            print('Погода в базе данных:\n')
            for weather in entries:
                print(weather)
            print('')

    def arg_print(self, entries):
        if self.args['print'] and self.args['date']:
            print('Погода по запросу:\n')
            for weather in entries:
                forecast_to_console(weather)

    def arg_cards(self, entries):
        if self.args['cards'] and self.args['date']:
            for weather in entries:
                im = ImageMaker(weather)
                view_pic(im.weather_card)


if __name__ == '__main__':
    args = args_parser()
    forecasts = ConsoleForecasts(args)
