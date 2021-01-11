# -*- coding: utf-8 -*-

# Написать декоратор, который будет логировать (записывать в лог файл)
# ошибки из декорируемой функции и выбрасывать их дальше.
#
# Имя файла лога - function_errors.log
# Формат лога: <имя функции> <параметры вызова> <тип ошибки> <текст ошибки>
# Лог файл открывать каждый раз при ошибке в режиме 'a'


import os


def log_errors(log_file):
    if os.path.exists(log_file):
        os.remove(log_file)

    def log_errors_sub(func):

        def surrogate(*args, **kwargs):
            try:
                real_func = func(*args, **kwargs)
                return real_func
            except Exception as exc:
                params_call = []
                for param_call in args:
                    params_call.append(param_call)
                for param_call in kwargs:
                    params_call.append(f'{param_call}={kwargs[param_call]}')
                line = f'{func.__name__} - {params_call} - {type(exc).__name__} - {exc}\n'
                with open(log_file, mode='a') as file:
                    file.write(line)

        return surrogate

    return log_errors_sub


# Проверить работу на следующих функциях
@log_errors('function_errors.log')
def perky(param):
    return param / 0


@log_errors('function_errors.log')
def check_line(line):
    name, email, age = line.split(' ')
    if not name.isalpha():
        raise ValueError("it's not a name")
    if '@' not in email or '.' not in email:
        raise ValueError("it's not a email")
    if not 10 <= int(age) <= 99:
        raise ValueError('Age not in 10..99 range')


lines = [
    'Ярослав bxh@ya.ru 600',
    'Земфира tslzp@mail.ru 52',
    'Тролль nsocnzas.mail.ru 82',
    'Джигурда wqxq@gmail.com 29',
    'Земфира 86',
    'Равшан wmsuuzsxi@mail.ru 35',
]

for line in lines:
    try:
        check_line(line=line)
    except Exception as exc:
        print(f'Invalid format: {exc}')

perky(param=42)

# Усложненное задание (делать по желанию).
# Написать декоратор с параметром - именем файла
#
# @log_errors('function_errors.log')
# def func():
#     pass
