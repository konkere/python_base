#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os.path
import requests
import configparser
import logging.config
from aiogram import Bot


logging.config.fileConfig('logging.conf')
tlgrm_bot_logger = logging.getLogger('tlgrm_bot_logger')


class Conf:

    def __init__(self):
        self.config_file = 'settings.conf'
        self.config = configparser.ConfigParser()
        self.exist()
        self.config.read(self.config_file)
        self.bot_id = self.read('Settings', 'bot_id')
        self.chat_id = self.read('Settings', 'chat_id')

    def exist(self):
        if not os.path.exists(self.config_file):
            try:
                self.create()
            except FileNotFoundError as exc:
                tlgrm_bot_logger.warning(exc)

    def create(self):
        self.config.add_section('Settings')
        self.write('Settings', 'bot_id', '000000000:00000000000000000000000000000000000')
        self.write('Settings', 'chat_id', '00000000000000')
        raise FileNotFoundError(f'Required to fill data in config (section [Settings]): {self.config_file}')

    def read(self, section, setting):
        value = self.config.get(section, setting)
        return value

    def write(self, section, setting, value):
        self.config.set(section, setting, value)
        with open(self.config_file, "w") as config_file:
            self.config.write(config_file)


class TlgrmBot:

    def __init__(self):
        self.config = Conf()
        self.bot = Bot(token=self.config.bot_id)
        self.commands = {
            'start': 'О-хайо',
            'hello': 'О-хайо',
            'help': 'Помощь в пути',
            'ping': 'pong'
        }
        self.username = self.get_username()
        self.commands_update_with_botname()

    def get_username(self):
        url_getme = f'https://api.telegram.org/bot{self.config.bot_id}/getMe'
        r = requests.get(url_getme)
        r = r.json()
        try:
            username = r['result']['username']
        except KeyError:
            username = ''
        return username

    def commands_update_with_botname(self):
        commands = list(self.commands.keys())
        for command in commands:
            command_username = f'{command}@{self.username}'
            self.commands[command_username] = self.commands[command]

    def send(self):
        pass
