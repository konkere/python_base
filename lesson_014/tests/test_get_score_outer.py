# -*- coding: utf-8 -*-

import unittest
from lesson_014.bowling import get_score_outer


class GetScoreOuterTest(unittest.TestCase):

    def test_contain_digits(self):
        result = get_score_outer('12121212121212121212')
        self.assertEqual(result, 30)

    def test_contain_strike(self):
        result = get_score_outer('X121212121212121212')
        self.assertEqual(result, 40)

    def test_contain_multiple_strikes(self):
        result = get_score_outer('X121212X1212X1212')
        self.assertEqual(result, 60)

    def test_contain_spare(self):
        result = get_score_outer('4/121212121212121212')
        self.assertEqual(result, 38)

    def test_contain_multiple_spares(self):
        result = get_score_outer('4/12125/1212128/1212')
        self.assertEqual(result, 54)

    def test_contain_miss(self):
        result = get_score_outer('-5121212121212121212')
        self.assertEqual(result, 32)

    def test_contain_multiple_misses(self):
        result = get_score_outer('-5121212123-1212-712')
        self.assertEqual(result, 36)

    def test_contain_specials(self):
        result = get_score_outer('12X125-124/X12-88/')
        self.assertEqual(result, 81)

    def test_more_than_10(self):
        with self.assertRaises(SyntaxError):
            get_score_outer('99')

    def test_multiple_more_than_10(self):
        with self.assertRaises(SyntaxError):
            get_score_outer('9988448899778866')

    def test_more_symbols(self):
        with self.assertRaises(SyntaxError):
            get_score_outer('1111111111111111111111')

    def test_rnd1(self):
        result = get_score_outer('X4/341412X513/1-X')
        self.assertEqual(result, 96)

    def test_rnd2(self):
        result = get_score_outer('X4/-41-12X5-3/1--9')
        self.assertEqual(result, 83)

    def test_99999999999999999999(self):
        with self.assertRaises(SyntaxError):
            get_score_outer('99999999999999999999')

    def test_rnd3(self):
        with self.assertRaises(SyntaxError):
            get_score_outer('X4/-41-79X5-3/1--9')

    def test_10_x_minus(self):
        result = get_score_outer('--------------------')
        self.assertEqual(result, 0)

    def test_10_x_minus_spare(self):
        result = get_score_outer('-/-/-/-/-/-/-/-/-/-/')
        self.assertEqual(result, 100)

    def test_10_x_strike(self):
        result = get_score_outer('XXXXXXXXXX')
        self.assertEqual(result, 270)

    def test_10_x_spare(self):
        result = get_score_outer('2/4/6/8/1/3/5/7/9/1/')
        self.assertEqual(result, 144)

    def test_spare_err(self):
        with self.assertRaises(SyntaxError):
            get_score_outer('/2/4/6/8/1/3/5/7/9/1')

    def test_unknown_symb(self):
        with self.assertRaises(SyntaxError):
            get_score_outer('qwerasdfzxcvtyghbnui')

    def test_rnd4(self):
        with self.assertRaises(SyntaxError):
            get_score_outer('2/4/6/8/1/3/5/7/9/1/X')

    def test_rnd5(self):
        with self.assertRaises(SyntaxError):
            get_score_outer('2/4/6/8/1/3/5/7/9/1')

    def test_empty(self):
        result = get_score_outer('')
        self.assertEqual(result, 0)

    def test_contain_zero(self):
        with self.assertRaises(SyntaxError):
            get_score_outer('12014521212121212121')

    def test_multiple_contains_zero(self):
        with self.assertRaises(SyntaxError):
            get_score_outer('12014521210121012121')

    def test_zero(self):
        with self.assertRaises(SyntaxError):
            get_score_outer('0')

    def test_spare_without_slash(self):
        with self.assertRaises(SyntaxError):
            get_score_outer('12121264121212121212')

    def test_multiple_spares_without_slash(self):
        with self.assertRaises(SyntaxError):
            get_score_outer('12121264128212911237')


if __name__ == '__main__':
    unittest.main()
