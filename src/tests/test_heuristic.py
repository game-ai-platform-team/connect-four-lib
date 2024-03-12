from unittest import TestCase

from config import INFINITY
from connect_four_lib.heuristic import Heuristic


class TestHeuristic(TestCase):
    def setUp(self) -> None:
        self.max_evaluation = 400

    def test_evaluate_window_returns_infinity_if_win(self):
        window1 = [1] * 4
        window2 = [2] * 4

        self.assertEqual(Heuristic._evaluate_window(window1, 1), INFINITY)
        self.assertEqual(Heuristic._evaluate_window(window2, 2), INFINITY)

    def test_evaluate_window_returns_zero_if_window_contains_another_color(self):
        windows = [[-1, 0, 1, 3], [1, 0, 1, 2], [2, 2, 2, 1], [1, 2, 0, 0]]
        for window in windows:
            self.assertEqual(Heuristic._evaluate_window(window, 1), 0)
            self.assertEqual(Heuristic._evaluate_window(window, 2), 0)

    def test_evaluate_window_returns_amount_of_points_if_only_one_color(self):
        windows = [
            [1, 0, 0, 0],
            [0, 0, 1, 0],
            [1, 0, 1, 0],
            [1, 0, 0, 1],
            [1, 1, 1, 0],
        ]

        for window in windows:
            self.assertEqual(window.count(1), Heuristic._evaluate_window(window, 1))

    def test_evaluate_board_detects_horizontal_win(self):
        board = [
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [2, 0, 0, 0, 0, 0],
            [1, 2, 0, 0, 0, 0],
            [1, 2, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0],
        ]

        self.assertGreater(Heuristic.evaluate(board, 1), self.max_evaluation)
        self.assertLess(Heuristic.evaluate(board, 2), -self.max_evaluation)

    def test_evaluate_board_detects_vertical_win(self):
        board = [
            [2, 2, 2, 2, 0, 0],
            [1, 1, 1, 0, 0, 0],
            [1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
        ]

        self.assertGreater(Heuristic.evaluate(board, 2), INFINITY - self.max_evaluation)
        self.assertLess(Heuristic.evaluate(board, 1), -INFINITY + self.max_evaluation)

    def test_evaluate_board_detects_downwards_vertical_win(self):
        board = [
            [1, 2, 1, 2, 0, 0],
            [1, 1, 2, 0, 0, 0],
            [1, 2, 0, 0, 0, 0],
            [2, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
        ]
        self.assertGreater(Heuristic.evaluate(board, 2), INFINITY - self.max_evaluation)
        self.assertLess(Heuristic.evaluate(board, 1), -INFINITY + self.max_evaluation)

    def test_evaluate_board_detects_upwards_vertical_win(self):
        board = [
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [1, 2, 1, 0, 0, 0],
            [2, 2, 2, 1, 0, 0],
            [2, 2, 2, 1, 1, 0],
            [1, 1, 1, 2, 2, 1],
        ]
        self.assertGreater(Heuristic.evaluate(board, 1), INFINITY - self.max_evaluation)
        self.assertLess(Heuristic.evaluate(board, 2), -INFINITY + self.max_evaluation)

    def test_evaluate_returns_zero_when_board_is_empty(self):
        board = [[0] * 6 * 7]
        self.assertEqual(Heuristic.evaluate(board, 1), 0)
        self.assertEqual(Heuristic.evaluate(board, 2), 0)

    def test_evaluate(self):
        board1 = [
            [1, 0, 0, 0, 0, 0],
            [1, 2, 0, 0, 0, 0],
            [2, 2, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
        ]
        board2 = [
            [1, 0, 0, 0, 0, 0],
            [1, 2, 1, 0, 0, 0],
            [2, 2, 1, 2, 0, 0],
            [2, 1, 0, 0, 0, 0],
            [2, 2, 0, 0, 0, 0],
            [1, 1, 1, 2, 1, 2],
            [1, 2, 0, 0, 0, 0],
        ]

        self.assertEqual(Heuristic.evaluate(board1, 1), -2)
        self.assertEqual(Heuristic.evaluate(board1, 2), 2)

        self.assertEqual(Heuristic.evaluate(board2, 2), -4)
        self.assertEqual(Heuristic.evaluate(board2, 1), 4)
