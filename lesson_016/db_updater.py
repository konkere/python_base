# -*- coding: utf-8 -*-

import peewee
from datetime import timedelta
from playhouse.db_url import connect
from weather_engine import WeatherMaker


db_proxy = peewee.DatabaseProxy()


class BaseModel(peewee.Model):
    class Meta:
        database = db_proxy


class Weather(BaseModel):
    date = peewee.DateTimeField()
    temp_day = peewee.CharField()
    temp_night = peewee.CharField()
    phrase = peewee.CharField()


class DatabaseUpdater:

    def __init__(self, db_url):
        self.database = connect(db_url)
        self.weather = Weather
        db_proxy.initialize(self.database)
        self.database.create_tables([self.weather])
        self.weather_forecasts = []

    def insert_entries(self):
        for entry in self.weather_forecasts:
            date = entry['date']
            try:
                forecast_in_db = self.read_entries([date, date])[0]
            except IndexError:
                forecast_in_db = {}
            if not forecast_in_db:
                self.insert_entry(entry)
            elif entry is not forecast_in_db:
                self.remove_entry(date)
                self.insert_entry(entry)

    def insert_entry(self, entry):
        self.weather.create(
            date=entry['date'],
            temp_day=entry['temp_day'],
            temp_night=entry['temp_night'],
            phrase=entry['phrase'],
        )

    def request_weather(self, date_range):
        self.weather_forecasts = WeatherMaker(date_range)

    def write_entries(self):
        if self.weather_forecasts:
            self.insert_entries()

    def read_entries(self, date_range):
        entries = []
        date_range.sort()
        date = date_range[0]
        last_date = date_range[1]
        while date <= last_date:
            try:
                weather = self.weather.get(self.weather.date == date)
            except self.weather.DoesNotExist:
                pass
            else:
                weather_dict = {
                    'date': weather.date.date(),
                    'temp_day': weather.temp_day,
                    'temp_night': weather.temp_night,
                    'phrase': weather.phrase
                }
                entries.append(weather_dict)
            date += timedelta(days=1)
        return entries

    def remove_entry(self, date):
        entry_in_db = self.weather.get(self.weather.date == date)
        entry_in_db.delete_instance()
