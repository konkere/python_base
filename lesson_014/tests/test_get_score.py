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

    def test_more_than_10(self):
        with self.assertRaises(SyntaxError):
            get_score('99')

    def test_multiple_more_than_10(self):
        with self.assertRaises(SyntaxError):
            get_score('9988448899778866')

    def test_more_symbols(self):
        with self.assertRaises(SyntaxError):
            get_score('1111111111111111111111')

    def test_rnd1(self):
        result = get_score('X4/341412X513/1-X')
        self.assertEqual(result, 112)

    def test_rnd2(self):
        result = get_score('X4/-41-12X5-3/1--9')
        self.assertEqual(result, 93)

    def test_99999999999999999999(self):
        with self.assertRaises(SyntaxError):
            get_score('99999999999999999999')

    def test_rnd3(self):
        with self.assertRaises(SyntaxError):
            get_score('X4/-41-79X5-3/1--9')

    def test_10_x_minus(self):
        result = get_score('--------------------')
        self.assertEqual(result, 0)

    def test_10_x_minus_spare(self):
        result = get_score('-/-/-/-/-/-/-/-/-/-/')
        self.assertEqual(result, 150)

    def test_10_x_strike(self):
        result = get_score('XXXXXXXXXX')
        self.assertEqual(result, 200)

    def test_10_x_spare(self):
        result = get_score('2/4/6/8/1/3/5/7/9/1/')
        self.assertEqual(result, 150)

    def test_spare_err(self):
        with self.assertRaises(SyntaxError):
            get_score('/2/4/6/8/1/3/5/7/9/1')

    def test_unknown_symb(self):
        with self.assertRaises(SyntaxError):
            get_score('qwerasdfzxcvtyghbnui')

    def test_rnd4(self):
        with self.assertRaises(SyntaxError):
            get_score('2/4/6/8/1/3/5/7/9/1/X')

    def test_rnd5(self):
        with self.assertRaises(SyntaxError):
            get_score('2/4/6/8/1/3/5/7/9/1')

    def test_empty(self):
        result = get_score('')
        self.assertEqual(result, 0)

    def test_contain_zero(self):
        with self.assertRaises(SyntaxError):
            get_score('12014521212121212121')

    def test_multiple_contains_zero(self):
        with self.assertRaises(SyntaxError):
            get_score('12014521210121012121')

    def test_zero(self):
        with self.assertRaises(SyntaxError):
            get_score('0')


if __name__ == '__main__':
    unittest.main()
