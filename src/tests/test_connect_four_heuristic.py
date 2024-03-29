from unittest import TestCase

from connect_four_lib.config import HEURISTIC_BASE, MAX_HEURISTIC
from connect_four_lib.connect_four_heuristic import ConnectFourHeuristic


class TestConnectFourHeuristic(TestCase):
    def setUp(self) -> None:
        self.max_evaluation = 5000

    def test_evaluate_window_returns_big_integer_if_win(self):
        window1 = (1,) * 4
        window2 = (2,) * 4

        self.assertEqual(
            ConnectFourHeuristic._evaluate_window(window1, 1), MAX_HEURISTIC
        )
        self.assertEqual(
            ConnectFourHeuristic._evaluate_window(window2, 2), MAX_HEURISTIC
        )

    def test_evaluate_window_returns_zero_if_window_contains_another_color(self):
        windows = [(-1, 0, 1, 3), (1, 0, 1, 2), (2, 2, 2, 1), (1, 2, 0, 0)]
        for window in windows:
            self.assertEqual(ConnectFourHeuristic._evaluate_window(window, 1), 0)
            self.assertEqual(ConnectFourHeuristic._evaluate_window(window, 2), 0)

    def test_evaluate_window_returns_amount_of_points_if_only_one_color(self):
        windows = [
            (1, 0, 0, 0),
            (0, 0, 1, 0),
            (1, 0, 1, 0),
            (1, 0, 0, 1),
            (1, 1, 1, 0),
        ]

        for window in windows:
            self.assertEqual(
                HEURISTIC_BASE ** window.count(1),
                ConnectFourHeuristic._evaluate_window(window, 1),
            )

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

        self.assertGreater(ConnectFourHeuristic.evaluate(board, 1), self.max_evaluation)
        self.assertLess(ConnectFourHeuristic.evaluate(board, 2), -self.max_evaluation)

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

        self.assertGreater(ConnectFourHeuristic.evaluate(board, 2), self.max_evaluation)
        self.assertLess(ConnectFourHeuristic.evaluate(board, 1), -self.max_evaluation)

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
        self.assertGreater(ConnectFourHeuristic.evaluate(board, 2), self.max_evaluation)
        self.assertLess(ConnectFourHeuristic.evaluate(board, 1), -self.max_evaluation)

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
        self.assertGreater(ConnectFourHeuristic.evaluate(board, 1), self.max_evaluation)
        self.assertLess(ConnectFourHeuristic.evaluate(board, 2), -self.max_evaluation)

    def test_evaluate_returns_zero_when_board_is_empty(self):
        board = [[0] * 6 * 7]
        self.assertEqual(ConnectFourHeuristic.evaluate(board, 1), 0)
        self.assertEqual(ConnectFourHeuristic.evaluate(board, 2), 0)

    def test_evaluate_detects_better_situation(self):
        board_better_1 = [
            [0, 0, 0, 0, 0, 0],
            [1, 1, 1, 0, 0, 0],
            [2, 2, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
        ]
        board_worse_1 = [
            [1, 0, 0, 0, 0, 0],
            [1, 2, 0, 0, 0, 0],
            [2, 2, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
        ]
        board_better_2 = [
            [0, 0, 0, 0, 0, 0],
            [1, 1, 1, 2, 0, 0],
            [2, 2, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
        ]
        board_worse_2 = [
            [0, 0, 0, 0, 0, 0],
            [1, 1, 1, 0, 0, 0],
            [2, 2, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0],
            [2, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
        ]

        self.assertLess(
            ConnectFourHeuristic.evaluate(board_worse_1, 1),
            ConnectFourHeuristic.evaluate(board_better_1, 1),
        )
        self.assertLess(
            ConnectFourHeuristic.evaluate(board_worse_2, 2),
            ConnectFourHeuristic.evaluate(board_better_2, 2),
        )
