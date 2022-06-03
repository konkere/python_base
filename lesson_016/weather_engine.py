# -*- coding: utf-8 -*-

import re
import requests
from datetime import datetime, timedelta, date as dt_date
from bs4 import BeautifulSoup


def convert_date(date):
    pattern = r'(\d?\d)[-.,:\/\\](\d?\d)[-.,:\/\\]?(\d?\d?\d\d)?'
    current_month = datetime.now().month
    current_year = datetime.now().year
    re_date = re.match(pattern, date)
    day = int(re_date.group(1))
    month = int(re_date.group(2))
    try:
        year = int(re_date.group(3))
        digit_2_year = year < 100
        year = digit_2_year * (current_year // 100) * 100 + year
    except TypeError:
        next_year = current_month > month
        year = next_year + current_year
    date = datetime(year, month, day).date()
    return date


def check_date_range(date_range):
    if not date_range:
        today = datetime.now().date()
        date_range = [today, today + timedelta(days=90)]
    elif isinstance(date_range, dt_date):
        date_range = [date_range, date_range]
    date_range.sort()
    return date_range


def plus_or_minus(temp):
    if int(temp) > 0:
        temp = f'+{temp}'
    return temp


class WeatherMaker:

    def __init__(self, date_range=None):
        self.url_root = 'https://www.accuweather.com/ru/ru/saint-petersburg/295212/daily-weather-forecast/295212?page='
        # self.url_root = 'https://www.accuweather.com/ru/ca/alert/x0b/daily-weather-forecast/54842?page='
        self.date_range = check_date_range(date_range)
        self.pattern_temp = r'(\-?\d+)'
        self.pattern_phrase = r'([А-я" "",""\-"Ёё]+)'
        self.break_early = False

    def __iter__(self):
        for page in range(8):
            if self.break_early:
                break
            else:
                yield from self.parse_page(page)

    def parse_page(self, page):
        url = f'{self.url_root}{page}'
        response = requests.get(url, headers={'User-agent': 'Mozilla/5.0'})
        html_doc = BeautifulSoup(response.text, features='html.parser')
        list_of_dates = html_doc.find_all('span', {'class': 'module-header sub date'})
        list_of_temps_day = html_doc.find_all('span', {'class': 'high'})
        list_of_temps_night = html_doc.find_all('span', {'class': 'low'})
        list_of_phrases = html_doc.find_all('div', {'class': 'phrase'})
        for date, temp_day, temp_night, phrase in zip(
                list_of_dates,
                list_of_temps_day,
                list_of_temps_night,
                list_of_phrases
        ):
            date = convert_date(date.text)
            if self.date_range[0] <= date <= self.date_range[1]:
                yield from self.parse_weather(date, phrase, temp_day, temp_night)
            elif date > self.date_range[1]:
                self.break_early = True
                break

    def parse_weather(self, date, phrase, temp_day, temp_night):
        temp_day = re.findall(self.pattern_temp, temp_day.text)[0]
        temp_night = re.findall(self.pattern_temp, temp_night.text)[0]
        phrase = re.findall(self.pattern_phrase, phrase.text)
        weather = {
            'date': date,
            'temp_day': plus_or_minus(temp_day),
            'temp_night': plus_or_minus(temp_night),
            'phrase': str(phrase[0])
        }
        yield weather
