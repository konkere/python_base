# -*- coding: utf-8 -*-

import unittest
from lesson_014.bowling import get_score


class GetScoreTest(unittest.TestCase):

    def test_contain_digits(self):
        result = get_score('12121212121212121212')
        self.assertEqual(result, 30)

    def test_contain_strike(self):
        result = get_score('X121212121212121212')
        self.assertEqual(result, 47)

    def test_contain_multiple_strikes(self):
        result = get_score('X121212X1212X1212')
        self.assertEqual(result, 81)

    def test_contain_spare(self):
        result = get_score('4/121212121212121212')
        self.assertEqual(result, 42)

    def test_contain_multiple_spares(self):
        result = get_score('4/12125/1212128/1212')
        self.assertEqual(result, 66)

    def test_contain_miss(self):
        result = get_score('-5121212121212121212')
        self.assertEqual(result, 32)

    def test_contain_multiple_misses(self):
        result = get_score('-5121212123-1212-712')
        self.assertEqual(result, 36)

    def test_contain_specials(self):
        result = get_score('12X125-124/X12-88/')
        self.assertEqual(result, 95)


if __name__ == '__main__':
    unittest.main()

# TODO дополнить тесты на ошибки и не только

# TODO дописать тесты на переполнение, на недополнение, на ноль! + такие тесты как к примеру:
# TODO 'X4/341412X513/1-X'
# TODO 'X4/-41-12X5-3/1--9'
# TODO '99999999999999999999'
# TODO 'X4/-41-79X5-3/1--9'
# TODO '--------------------'
# TODO '-/-/-/-/-/-/-/-/-/-/'
# TODO 'XXXXXXXXXX'
# TODO '2/4/6/8/1/3/5/7/9/1/'
# TODO '/2/4/6/8/1/3/5/7/9/1'
# TODO 'qwerasdfzxcvtyghbnui'
# TODO '2/4/6/8/1/3/5/7/9/1/X'
# TODO '2/4/6/8/1/3/5/7/9/1'
# TODO ''
# TODO чем больше тестов тем лучше