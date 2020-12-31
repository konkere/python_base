# -*- coding: utf-8 -*-

# Есть файл с протоколом регистраций пользователей на сайте - registrations.txt
# Каждая строка содержит: ИМЯ ЕМЕЙЛ ВОЗРАСТ, разделенные пробелами
# Например:
# Василий test@test.ru 27
#
# Надо проверить данные из файла, для каждой строки:
# - присутсвуют все три поля
# - поле имени содержит только буквы
# - поле емейл содержит @ и .
# - поле возраст является числом от 10 до 99
#
# В результате проверки нужно сформировать два файла
# - registrations_good.log для правильных данных, записывать строки как есть
# - registrations_bad.log для ошибочных, записывать строку и вид ошибки.
#
# Для валидации строки данных написать метод, который может выкидывать исключения:
# - НЕ присутсвуют все три поля: ValueError
# - поле имени содержит НЕ только буквы: NotNameError (кастомное исключение)
# - поле емейл НЕ содержит @ и .(точку): NotEmailError (кастомное исключение)
# - поле возраст НЕ является числом от 10 до 99: ValueError
# Вызов метода обернуть в try-except.


class NotNameError(Exception):

    def __init__(self):
        self.message = 'Поле имени содержит НЕ только буквы'

    def __str__(self):
        return self.message


class NotEmailError(Exception):

    def __init__(self):
        self.message = 'поле емейл НЕ содержит "@" и "."(точку)'

    def __str__(self):
        return self.message


class RegsParser:

    def __init__(self, file_in):
        self.file_in = file_in
        self.file_regs_good = 'registrations_good.log'
        self.file_regs_bad = 'registrations_bad.log'
        # принял ответ
        open(self.file_regs_good, mode='w+').close()
        open(self.file_regs_bad, mode='w+').close()
        self.parse_file()

    def parse_file(self):
        with open(self.file_in, 'r', encoding='utf8') as file:
            for line in file:
                line = line[:-1]
                self.parse_line(line)

    def parse_line(self, line):
        try:
            name, email, age = self.check_fields_exist(line)
            self.check_name(name)
            self.check_email(email)
            self.check_age(age)
        except (ValueError, NotNameError, NotEmailError) as exc:
            self.write_line(line, exc)
        else:
            self.write_line(line)

    def write_line(self, line, error=False):
        if not error:
            filename = self.file_regs_good
            line = f'{line}\n'
        else:
            filename = self.file_regs_bad
            line = f'{line} 🠖 {error}\n'
        with open(filename, mode='a') as file:
            file.write(line)

    @staticmethod
    def check_fields_exist(line):
        name, email, age = line.split(' ')
        return name, email, age

    @staticmethod
    def check_name(name):
        if not name.isalpha():
            raise NotNameError

    @staticmethod
    def check_email(email):
        exist_chars = {'.': False, '@': False}
        for char in email:
            if char in exist_chars.keys():
                exist_chars[char] = True
        if not all(exist_chars.values()):
            raise NotEmailError

    @staticmethod
    def check_age(age):
        if not (age.isdigit() and (9 < int(age) < 100)):
            raise ValueError('Поле возраст НЕ является числом от 10 до 99')


RegsParser('registrations.txt')

# зачет!
