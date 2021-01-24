# -*- coding: utf-8 -*-


# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью в МНОГОПОТОЧНОМ стиле
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

from threading import Thread
from utils import time_track, volatility, result, files_in_dir


class TickersParser(Thread):

    def __init__(self, file, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.file = file
        self.name_ticket = ''
        self.volatility = 0
        self.file_titles = 'SECID,TRADETIME,PRICE,QUANTITY\n'

    def run(self):
        price_min, price_max = self.parse_file()
        self.volatility = volatility(price_min, price_max)

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
        if not self.name_ticket:
            self.name_ticket = line.split(',')[0]
        price = float(line.split(',')[2])
        return price


@time_track
def main():
    tickers = []
    tickers_volatility = []
    tickers_volatility_0 = []
    for file in files_in_dir():
        tickers.append(TickersParser(file))
    for ticker in tickers:
        ticker.start()
    for ticker in tickers:
        ticker.join()
    for ticker in tickers:
        if ticker.volatility == 0.0:
            tickers_volatility_0.append(ticker.name_ticket)
        else:
            tickers_volatility.append([ticker.name_ticket, ticker.volatility])
    result(tickers_volatility, tickers_volatility_0)


if __name__ == '__main__':
    main()
