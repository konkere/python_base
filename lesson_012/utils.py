# -*- coding: utf-8 -*-

import time
import os.path


def time_track(func):
    def surrogate(*args, **kwargs):
        started_at = time.time()

        result = func(*args, **kwargs)

        ended_at = time.time()
        elapsed = round(ended_at - started_at, 4)
        print(f'Функция работала {elapsed} секунд(ы)')
        return result
    return surrogate


def volatility(min, max):
    half_sum = (max + min) / 2
    result = ((max - min) / half_sum) * 100
    return result


def files_in_dir():
    subdir = 'trades'
    workdir = os.path.join(os.getcwd(), subdir)
    for file in os.listdir(workdir):
        yield os.path.join(workdir, file)


def result(tickers_volatility, tickers_volatility_0):
    tickers_volatility = sorted(tickers_volatility, key=lambda x: x[1], reverse=True)
    tickers_volatility_0.sort()
    print('Максимальная волатильность:')
    for number in range(3):
        ticker = tickers_volatility[number][0]
        volatility_percent = round(tickers_volatility[number][1], 2)
        print(f'\t{ticker} - {volatility_percent} %')
    print('Минимальная волатильность:')
    for number in range(3):
        ticker = tickers_volatility[number - 3][0]
        volatility_percent = round(tickers_volatility[number - 3][1], 2)
        print(f'\t{ticker} - {volatility_percent} %')
    print('Нулевая волатильность:')
    print('\t' + ', '.join(tickers_volatility_0))