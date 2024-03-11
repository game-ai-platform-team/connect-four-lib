import unittest

from connect_four_lib.win_checker import WinChecker
from game_state import GameState


class TestConnectFourJudge(unittest.TestCase):
    def setUp(self) -> None:
        self.checker = WinChecker()

    def test_check_win_in_empty_board(self):
        board = [[0] * 6 * 7]
        self.assertEqual(self.checker.check_win(board), False)

    def test_check_win_in_half_full_board_with_no_win(self):
        board = [
            [1, 1, 0, 0, 0, 0],
            [2, 2, 0, 0, 0, 0],
            [1, 2, 1, 2, 1, 2],
            [2, 1, 2, 1, 2, 0],
            [2, 1, 2, 1, 0, 0],
            [1, 0, 0, 0, 0, 0],
            [1, 2, 1, 2, 1, 2],
        ]
        self.assertEqual(self.checker.check_win(board), False)

    def test_check_win_in_full_board_with_no_win(self):
        board = [
            [1, 1, 1, 2, 2, 2],
            [2, 2, 2, 1, 1, 1],
            [1, 1, 1, 2, 2, 2],
            [2, 2, 2, 1, 1, 1],
            [1, 1, 1, 2, 2, 2],
            [2, 2, 2, 1, 1, 1],
            [1, 1, 1, 2, 2, 2],
        ]
        self.assertEqual(self.checker.check_win(board), False)

    def test_check_win_finds_vertical_win(self):
        board = [
            [1, 1, 1, 2, 0, 0],
            [2, 2, 0, 0, 0, 0],
            [1, 1, 1, 2, 2, 2],
            [2, 2, 2, 1, 1, 1],
            [0, 0, 0, 0, 0, 0],
            [2, 2, 2, 1, 1, 1],
            [1, 1, 2, 2, 2, 2],
        ]
        self.assertEqual(self.checker.check_win(board), True)

        board = [
            [1, 1, 1, 2, 2, 2],
            [2, 2, 2, 1, 1, 1],
            [1, 1, 1, 2, 2, 2],
            [2, 2, 1, 1, 1, 1],
            [1, 1, 1, 2, 2, 2],
            [2, 2, 2, 1, 1, 1],
            [2, 1, 1, 2, 2, 2],
        ]
        self.assertEqual(self.checker.check_win(board), True)

    def test_check_win_finds_horizontal_win(self):
        board = [
            [1, 1, 1, 2, 2, 1],
            [2, 2, 2, 1, 1, 1],
            [1, 1, 1, 2, 1, 1],
            [2, 2, 1, 1, 2, 1],
            [1, 1, 1, 2, 2, 2],
            [2, 0, 0, 0, 0, 0],
            [2, 2, 1, 2, 2, 2],
        ]
        self.assertEqual(self.checker.check_win(board), True)

        board = [
            [1, 1, 1, 2, 2, 1],
            [2, 2, 2, 1, 1, 1],
            [1, 1, 1, 2, 2, 1],
            [2, 2, 1, 1, 1, 2],
            [2, 1, 1, 2, 2, 2],
            [2, 0, 0, 0, 0, 0],
            [2, 2, 1, 2, 2, 2],
        ]
        self.assertEqual(self.checker.check_win(board), True)

    def test_check_win_finds_dup_win(self):
        board = [
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [1, 1, 1, 0, 0, 0],
            [2, 2, 2, 1, 0, 0],
            [2, 1, 1, 2, 1, 0],
            [1, 2, 2, 1, 2, 1],
        ]
        self.assertEqual(self.checker.check_win(board), True)

        board = [
            [2, 0, 0, 0, 0, 0],
            [1, 2, 0, 0, 0, 0],
            [2, 1, 2, 0, 0, 0],
            [1, 1, 1, 2, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
        ]
        self.assertEqual(self.checker.check_win(board), True)

    def test_check_win_finds_ddown_win(self):
        board = [
            [1, 1, 1, 2, 0, 0],
            [2, 1, 2, 0, 0, 0],
            [1, 2, 0, 0, 0, 0],
            [2, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
        ]
        self.assertEqual(self.checker.check_win(board), True)

        board = [
            [1, 2, 1, 2, 1, 2],
            [2, 1, 2, 1, 2, 0],
            [1, 2, 1, 2, 0, 0],
            [2, 1, 2, 0, 0, 0],
            [1, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
        ]
        self.assertEqual(self.checker.check_win(board), True)
