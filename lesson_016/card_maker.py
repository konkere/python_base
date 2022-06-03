# -*- coding: utf-8 -*-

import os
import re
import cv2


def weather_pics_dict(path):
    pattern = r'([A-z]*)[.][A-z]*'
    pics = os.listdir(path)
    pics_dict = {}
    for pic in pics:
        pic_name = re.match(pattern, pic).group(1)
        pics_dict[pic_name] = os.path.join(path, pic)
    return pics_dict


def view_pic(pic_to_view):
    cv2.imshow('Weather forecast', pic_to_view)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


class ImageMaker:

    def __init__(self, weather):
        self.weather_pics_path = weather_pics_dict('python_snippets/external_data/weather_img')
        self.weather_words = {
            'cloud': ['облачн', 'облак'],
            'rain': ['дожд', 'ливн', 'ливен'],
            'snow': ['снег', 'снеж'],
            'sun': ['солн', 'ясно'],
            'wind': ['ветр', 'ветер'],
        }
        self.weather_gradient_step = {
            'cloud': [.5, .5, .5],
            'rain': [0, .6, .6],
            'snow': [0, .25, .5],
            'sun': [.5, 0, 0],
            'wind': [.5, .5, 1],
        }
        self.weather = weather
        self.weather_keyword = self.pick_weather_keyword(self.weather['phrase'])
        self.base_pic_path = 'python_snippets/external_data/probe.jpg'
        self.weather_card = cv2.imread(self.base_pic_path)
        self.weather_card_height, self.weather_card_width = self.weather_card.shape[:2]
        self.create_card()

    def create_card(self):
        if self.weather_keyword:
            self.fill_gradient()
            self.place_pic_on_pic()
        self.generate_texts()

    def pick_weather_keyword(self, text):
        text = text.lower()
        for keyword in self.weather_words:
            if any(x in text for x in self.weather_words[keyword]):
                return keyword
        return None

    def fill_gradient(self):
        step = self.weather_gradient_step[self.weather_keyword]
        blue = green = red = 255
        for width in range(100, self.weather_card_width):
            cv2.line(
                img=self.weather_card,
                color=(blue, green, red),
                pt1=(width, 0),
                pt2=(width, self.weather_card_height)
            )
            blue -= step[0]
            green -= step[1]
            red -= step[2]

    def place_pic_on_pic(self):
        weather_pic_path = self.weather_pics_path[self.weather_keyword]
        weather_pic = cv2.imread(weather_pic_path)
        weather_pic_height, weather_pic_width = weather_pic.shape[:2]
        self.weather_card[:weather_pic_height, :weather_pic_width] = weather_pic[:]

    def generate_texts(self):
        self.place_text_on_pic(
            text=self.weather['phrase'],
            coord=(10, self.weather_card_height - 10),
            color=(0, 0, 0),
            font_size=.5,
            font_thickness=1
        )
        self.place_text_on_pic(
            text=self.weather['date'].strftime('%d.%m.%Y'),
            coord=(self.weather_card_width // 2, 20),
            color=(0, 0, 0),
            font_size=.5,
            font_thickness=1
        )
        self.place_text_on_pic(
            text='Температура днем/ночью:',
            coord=(self.weather_card_width // 3, self.weather_card_height // 4),
            color=(0, 0, 0),
            font_size=.5,
            font_thickness=1
        )
        self.place_text_on_pic(
            text=self.weather['temp_day'],
            coord=(self.weather_card_width // 3, self.weather_card_height * 2 // 3),
            color=(0, 0, 0),
            font_size=2,
            font_thickness=2
        )
        self.place_text_on_pic(
            text=f"/{self.weather['temp_night']}",
            coord=(self.weather_card_width * 5 // 8, self.weather_card_height * 2 // 3),
            color=(0, 0, 0),
            font_size=1,
            font_thickness=1
        )

    def place_text_on_pic(self, text, coord, color, font_size, font_thickness):
        self.weather_card = cv2.putText(
            img=self.weather_card,
            text=text,
            org=coord,
            fontFace=cv2.FONT_HERSHEY_COMPLEX,
            color=color,
            fontScale=font_size,
            thickness=font_thickness,
            lineType=cv2.LINE_AA
        )
