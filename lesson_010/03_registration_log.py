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
            self.write_bad(line, exc)
        else:
            self.write_good(line)

    def check_fields_exist(self, line):
        name, email, age = line.split(' ')
        return name, email, age

    def check_name(self, name):
        if not name.isalpha():
            raise NotNameError

    def check_email(self, email):
        exist_dot = False
        exist_at = False
        for char in email:
            if char == '.':
                exist_dot = True
            if char == '@':
                exist_at = True
        if not (exist_dot and exist_at):
            raise NotEmailError

    def check_age(self, age):
        if not (age.isdigit() and (9 < int(age) < 100)):
            raise ValueError('Поле возраст НЕ является числом от 10 до 99')

    def write_good(self, line):
        with open(self.file_regs_good, mode='a') as file:
            line = f'{line}\n'
            file.write(line)

    def write_bad(self, line, error):
        with open(self.file_regs_bad, mode='a') as file:
            line_error = f'{line} 🠖 {error}\n'
            file.write(line_error)


RegsParser('registrations.txt')
