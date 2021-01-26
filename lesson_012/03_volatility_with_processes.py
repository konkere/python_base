# -*- coding: utf-8 -*-


# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью в МНОГОПРОЦЕССНОМ стиле
#
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

from multiprocessing import Process, Queue
from queue import Empty
from utils import time_track, volatility, result, files_in_dir


class TickersParser(Process):

    def __init__(self, file, collector, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.file = file
        self.collector = collector
        self.name_ticker = ''
        self.volatility = 0
        self.file_titles = 'SECID,TRADETIME,PRICE,QUANTITY\n'

    def run(self):
        price_min, price_max = self.parse_file()
        self.volatility = volatility(price_min, price_max)
        self.collector.put(dict(ticker=self.name_ticker, volatility=self.volatility))

    def parse_file(self):
        prices = []
        with open(self.file, 'r', encoding='utf8') as file:
            for line in file:
                if not line == self.file_titles:
                    price = self.parse_line(line)
                    prices.append(price)
        prices.sort()
        price_min = prices[0]
        price_max = prices[-1]
        return price_min, price_max

    def parse_line(self, line):
        if not self.name_ticker:
            self.name_ticker = line.split(',')[0]
        price = float(line.split(',')[2])
        return price


@time_track
def main():
    collector = Queue()
    tickers = []
    tickers_volatility = []
    tickers_volatility_0 = []
    for file in files_in_dir():
        tickers.append(TickersParser(file, collector=collector))
    for ticker in tickers:
        ticker.start()

    while True:
        try:
            data = collector.get(timeout=.01)
            if data['volatility'] == 0.0:
                tickers_volatility_0.append(data['ticker'])
            else:
                tickers_volatility.append([data['ticker'], data['volatility']])
        except Empty:
            if not any(ticker.is_alive() for ticker in tickers):
                break

    for ticker in tickers:
        ticker.join()
    result(tickers_volatility, tickers_volatility_0)


# Intel 4 cores (8 threads) 3.6GHz base frequency (4.2GHz turbo) - Функция работала 0.6666 секунд(ы)
# AMD 4 core 1.7GHz - Функция работала 5.8824 секунд(ы)
if __name__ == '__main__':
    main()
