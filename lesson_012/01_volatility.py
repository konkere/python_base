# -*- coding: utf-8 -*-


# Описание предметной области:
#
# При торгах на бирже совершаются сделки - один купил, второй продал.
# Покупают и продают ценные бумаги (акции, облигации, фьючерсы, етс). Ценные бумаги - это по сути долговые расписки.
# Ценные бумаги выпускаются партиями, от десятка до несколько миллионов штук.
# Каждая такая партия (выпуск) имеет свой торговый код на бирже - тикер - https://goo.gl/MJQ5Lq
# Все бумаги из этой партии (выпуска) одинаковы в цене, поэтому говорят о цене одной бумаги.
# У разных выпусков бумаг - разные цены, которые могут отличаться в сотни и тысячи раз.
# Каждая биржевая сделка характеризуется:
#   тикер ценнной бумаги
#   время сделки
#   цена сделки
#   обьем сделки (сколько ценных бумаг было куплено)
#
# В ходе торгов цены сделок могут со временем расти и понижаться. Величина изменения цен называтея волатильностью.
# Например, если бумага №1 торговалась с ценами 11, 11, 12, 11, 12, 11, 11, 11 - то она мало волатильна.
# А если у бумаги №2 цены сделок были: 20, 15, 23, 56, 100, 50, 3, 10 - то такая бумага имеет большую волатильность.
# Волатильность можно считать разными способами, мы будем считать сильно упрощенным способом -
# отклонение в процентах от полусуммы крайних значений цены за торговую сессию:
#   полусумма = (максимальная цена + минимальная цена) / 2
#   волатильность = ((максимальная цена - минимальная цена) / полусумма) * 100%
# Например для бумаги №1:
#   half_sum = (12 + 11) / 2 = 11.5
#   volatility = ((12 - 11) / half_sum) * 100 = 8.7%
# Для бумаги №2:
#   half_sum = (100 + 3) / 2 = 51.5
#   volatility = ((100 - 3) / half_sum) * 100 = 188.34%
#
# В реальности волатильность рассчитывается так: https://goo.gl/VJNmmY
#
# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью.
# Бумаги с нулевой волатильностью вывести отдельно.
# Результаты вывести на консоль в виде:
#   Максимальная волатильность:
#       ТИКЕР1 - ХХХ.ХХ %
#       ТИКЕР2 - ХХХ.ХХ %
#       ТИКЕР3 - ХХХ.ХХ %
#   Минимальная волатильность:
#       ТИКЕР4 - ХХХ.ХХ %
#       ТИКЕР5 - ХХХ.ХХ %
#       ТИКЕР6 - ХХХ.ХХ %
#   Нулевая волатильность:
#       ТИКЕР7, ТИКЕР8, ТИКЕР9, ТИКЕР10, ТИКЕР11, ТИКЕР12
# Волатильности указывать в порядке убывания. Тикеры с нулевой волатильностью упорядочить по имени.
#
# Подготовка исходных данных
# 1. Скачать файл https://drive.google.com/file/d/1l5sia-9c-t91iIPiGyBc1s9mQ8RgTNqb/view?usp=sharing
#       (обратите внимание на значок скачивания в правом верхнем углу,
#       см https://drive.google.com/file/d/1M6mW1jI2RdZhdSCEmlbFi5eoAXOR3u6G/view?usp=sharing)
# 2. Раззиповать средствами операционной системы содержимое архива
#       в папку python_base/lesson_012/trades
# 3. В каждом файле в папке trades содержится данные по сделакам по одному тикеру, разделенные запятыми.
#   Первая строка - название колонок:
#       SECID - тикер
#       TRADETIME - время сделки
#       PRICE - цена сделки
#       QUANTITY - количество бумаг в этой сделке
#   Все последующие строки в файле - данные о сделках
#
# Подсказка: нужно последовательно открывать каждый файл, вычитывать данные, высчитывать волатильность и запоминать.
# Вывод на консоль можно сделать только после обработки всех файлов.
#
# Для плавного перехода к мультипоточности, код оформить в обьектном стиле, используя следующий каркас
#
# class <Название класса>:
#
#     def __init__(self, <параметры>):
#         <сохранение параметров>
#
#     def run(self):
#         <обработка данных>

import os.path
# from datetime import datetime


def volatility(min, max):
    half_sum = (max + min) / 2
    result = ((max - min) / half_sum) * 100
    return result


class TickersParser:

    def __init__(self, subdir=''):
        self.workdir = os.path.join(os.getcwd(), subdir)
        self.files = os.listdir(self.workdir)
        self.tickers = {}
        self.tickers_volatility = []
        self.tickers_volatility_0 = []
        self.file_titles = 'SECID,TRADETIME,PRICE,QUANTITY\n'

    def run(self):
        for file in self.files:
            self.parse_file(file)
        for ticker in self.tickers:
            self.tickers[ticker].sort()
            price_min = self.tickers[ticker][0]
            price_max = self.tickers[ticker][-1]
            ticker_volatility = volatility(price_min, price_max)
            if ticker_volatility == 0.0:
                self.tickers_volatility_0.append(ticker)
            else:
                self.tickers_volatility.append((ticker, ticker_volatility))
        self.tickers_volatility = sorted(self.tickers_volatility, key=lambda x: x[1], reverse=True)
        self.tickers_volatility_0.sort()
        self.result()

    def parse_file(self, filename):
        file_path = os.path.join(self.workdir, filename)
        with open(file_path, 'r', encoding='utf8') as file:
            for line in file:
                if not line == self.file_titles:
                    self.parse_line(line)

    def parse_line(self, line):
        # sec_id, time, price, quantity = line.split(',')
        # time = datetime.strptime(time, '%H:%M:%S').time()
        # quantity = int(quantity)
        sec_id = line.split(',')[0]
        price = float(line.split(',')[2])
        if sec_id in self.tickers:
            self.tickers[sec_id].append(price)
        else:
            self.tickers[sec_id] = [price]

    def result(self):
        print('Максимальная волатильность:')
        for number in range(3):
            ticker = self.tickers_volatility[number][0]
            volatility_percent = round(self.tickers_volatility[number][1], 2)
            print(f'\t{ticker} - {volatility_percent} %')
        print('Минимальная волатильность:')
        for number in range(3):
            ticker = self.tickers_volatility[number - 3][0]
            volatility_percent = round(self.tickers_volatility[number - 3][1], 2)
            print(f'\t{ticker} - {volatility_percent} %')
        print('Нулевая волатильность:')
        print('\t' + ', '.join(self.tickers_volatility_0))


tickers = TickersParser(subdir='trades')
tickers.run()
