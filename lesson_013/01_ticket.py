# -*- coding: utf-8 -*-


# Заполнить все поля в билете на самолет.
# Создать функцию, принимающую параметры: ФИО, откуда, куда, дата вылета,
# и заполняющую ими шаблон билета Skillbox Airline.
# Шаблон взять в файле lesson_013/images/ticket_template.png
# Пример заполнения lesson_013/images/ticket_sample.png
# Подходящий шрифт искать на сайте ofont.ru

import os.path
import argparse

from PIL import Image, ImageDraw, ImageFont, ImageColor


def make_ticket(fio, from_, to, date, out_file='out_img.png'):
    path_to_img = os.path.join('images', 'ticket_template.png')
    path_to_font = 'ofont_ru_Mipgost.ttf'
    font_size = 20
    initial_offset = (50, 145 - font_size)
    img = Image.open(path_to_img)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(path_to_font, size=font_size)
    x_y = [
        initial_offset,
        (initial_offset[0], initial_offset[1] + 70),
        (initial_offset[0], initial_offset[1] + 135),
        (initial_offset[0] + 240, initial_offset[1] + 135),
    ]
    fields = [
        fio,
        from_,
        to,
        date,
    ]
    for field in range(4):
        draw.text(x_y[field], fields[field], font=font, fill=ImageColor.colormap['black'])
    # img.show()
    img.save(out_file)


# make_ticket(fio='Атрейдес П.Л.', from_='Каладан', to='Арракис', date='26.02')

# Усложненное задание (делать по желанию).
# Написать консольный скрипт c помощью встроенного python-модуля argparse.
# Скрипт должен принимать параметры:
#   --fio - обязательный, фамилия.
#   --from - обязательный, откуда летим.
#   --to - обязательный, куда летим.
#   --date - обязательный, когда летим.
#   --save_to - необязательный, путь для сохранения заполненнего билета.
# и заполнять билет.

def args_parser():
    parser = argparse.ArgumentParser(description='Ticket maker')
    parser.add_argument('--fio', type=str, help='ФИО', required=True)
    parser.add_argument('--from', type=str, help='Пункт отправления', required=True)
    parser.add_argument('--to', type=str, help='Пункт прибытия', required=True)
    parser.add_argument('--date', type=str, help='Дата отправления', required=True)
    parser.add_argument('--out_file', type=str, help='Путь для сохранения заполненного билета', required=False)
    args = parser.parse_args().__dict__
    if not args['out_file']:
        args['out_file'] = 'out_img.png'
    return args


args = args_parser()

make_ticket(
    fio=args['fio'],
    from_=args['from'],
    to=args['to'],
    date=args['date'],
    out_file=args['out_file']
)

# 01_ticket.py --fio='Атрейдес П.Л.' --from='Каладан' --to='Арракис' --date='26.02' --out_file='out_yai.png'
