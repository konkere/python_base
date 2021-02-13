# -*- coding: utf-8 -*-

import unittest
from lesson_014.bowling import score_by_frame


class ScoreByFrameTest(unittest.TestCase):

    def test_strike(self):
        result = score_by_frame('X0')
        self.assertEqual(result, 20)

    def test_spare(self):
        result = score_by_frame('4/')
        self.assertEqual(result, 15)

    def test_with_points(self):
        result = score_by_frame('35')
        self.assertEqual(result, 8)

    def test_with_points_0(self):
        result = score_by_frame('08')
        self.assertEqual(result, 8)


if __name__ == '__main__':
    unittest.main()
