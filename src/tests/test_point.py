from unittest import TestCase

from connect_four_lib.point import Point


class TestPoint(TestCase):
    def test_equality_of_points(self):
        self.assertEqual(Point(0, 0), Point(0, 0))
        self.assertEqual(Point(-1, 0), Point(-1, 0))
        self.assertEqual(Point(5, 6), Point(5, 6))

    def test_sum_of_points(self):
        self.assertEqual(Point(1, 2) + Point(3, 4), Point(4, 6))
        self.assertEqual(Point(7, 2) + Point(0, 0), Point(7, 2))

    def test_substraction_of_points(self):
        self.assertEqual(Point(1, 2) - Point(3, 4), Point(-2, -2))
        self.assertEqual(Point(7, 2) - Point(0, 0), Point(7, 2))

    def test_negation_of_point(self):
        self.assertEqual(-Point(0, 0), Point(0, 0))
        self.assertEqual(-Point(3, 4), Point(-3, -4))
        self.assertEqual(-(-Point(7, 1)), Point(7, 1))
