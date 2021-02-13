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
