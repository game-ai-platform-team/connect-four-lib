import unittest

from connect_four_lib.connect_four_heuristic import ConnectFourHeuristic
from connect_four_lib.connect_four_judge import ConnectFourJudge


class TestConnectFourHeuristic(unittest.TestCase):
    def setUp(self) -> None:
        self.judge = ConnectFourJudge()

    def test_evaluate_window_with_player1_moves_only(self):
        heuristic = ConnectFourHeuristic(False)
        self.assertEqual(heuristic.evaluate_single_window([0, 1, 0, 0]), -2)
        self.assertEqual(heuristic.evaluate_single_window([0, 1, 0, 1]), -4)

    def test_evaluate_window_with_player2_moves_only(self):
        heuristic = ConnectFourHeuristic(False)
        self.assertEqual(heuristic.evaluate_single_window([0, 2, 0, 0]), 2)
        self.assertEqual(heuristic.evaluate_single_window([0, 2, 0, 2]), 4)

    def test_evaluate_window_with_both_players_moves(self):
        heuristic = ConnectFourHeuristic(True)
        self.assertEqual(heuristic.evaluate_single_window([0, 2, 0, 1]), 0)
        self.assertEqual(heuristic.evaluate_single_window([2, 2, 2, 1]), 0)

    def test_evaluate_window_with_nothing_in_it(self):
        heuristic = ConnectFourHeuristic(True)
        self.assertEqual(heuristic.evaluate_single_window([0, 0, 0, 0]), 0)

    def test_evaluate_window_with_one_players_moves(self):
        heuristic = ConnectFourHeuristic(False)
        self.assertEqual(heuristic.evaluate_single_window([1, 0, 0, 1]), -4)
        self.assertEqual(heuristic.evaluate_single_window([1, 0, 1, 1]), -8)
        self.assertEqual(heuristic.evaluate_single_window([0, 2, 2, 2]), 8)

    def test_evaluate_window_with_win(self):
        heuristic = ConnectFourHeuristic(False)
        self.assertEqual(heuristic.evaluate_single_window([1, 1, 1, 1]), -1000)
        self.assertEqual(heuristic.evaluate_single_window([2, 2, 2, 2]), 1000)

    def test_evaluate_window_with_both_players_moves_in_it(self):
        heuristic = ConnectFourHeuristic(True)
        self.assertEqual(heuristic.evaluate_single_window([1, 2, 1, 1]), 0)
        self.assertEqual(heuristic.evaluate_single_window([2, 2, 0, 1]), 0)
        self.assertEqual(heuristic.evaluate_single_window([2, 0, 0, 1]), 0)

    def test_evaluate_horizontal_with_one_players_moves(self):
        heuristic = ConnectFourHeuristic(True)
        board = [[1,2,0,0,0,0], 
                 [1,2,0,0,0,0], 
                 [0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0]]
        for i in [(0,0), (0,1), (1,0), (1,1)]:
            heuristic.evaluate_relevant_windows(i[0], i[1], board)
        self.assertEqual(heuristic.horizontal_windows[0][0], 4)
        self.assertEqual(heuristic.horizontal_windows[1][0], 2)
        self.assertEqual(heuristic.horizontal_windows[2][0], 0)
        self.assertEqual(heuristic.horizontal_windows[0][1], -4)
        self.assertEqual(heuristic.horizontal_windows[1][1], -2)
        self.assertEqual(heuristic.horizontal_windows[2][1], 0)

    def test_evaluate_horizontal_with_both_players_moves(self):
        heuristic = ConnectFourHeuristic(True)
        board = [[2,0,0,0,0,0], 
                 [1,0,0,0,0,0], 
                 [0,0,0,0,0,0],
                 [2,0,0,0,0,0], 
                 [1,0,0,0,0,0], 
                 [1,0,0,0,0,0], 
                 [0,0,0,0,0,0]]
        for i in [(4,0), (3,0), (5,0), (0,0), (1,0)]:
            heuristic.evaluate_relevant_windows(i[0], i[1], board)
        self.assertEqual(heuristic.horizontal_windows[3][0], 0)
        self.assertEqual(heuristic.horizontal_windows[0][0], 0)

    def test_evaluate_vertical_with_one_players_moves(self):
        heuristic = ConnectFourHeuristic(True)
        board = [[1,1,1,0,0,0], 
                 [2,2,0,0,0,0], 
                 [0,0,0,0,0,0],
                 [0,0,0,0,0,0],
                 [0,0,0,0,0,0],
                 [0,0,0,0,0,0],
                 [0,0,0,0,0,0]]
        for i in [(0,0), (0,1), (0,2), (1,0), (1,1)]:
            heuristic.evaluate_relevant_windows(i[0], i[1], board)
        self.assertEqual(heuristic.vertical_windows[0][0], 8)
        self.assertEqual(heuristic.vertical_windows[0][1], 4)
        self.assertEqual(heuristic.vertical_windows[0][2], 2)
        self.assertEqual(heuristic.vertical_windows[1][0], -4)
        self.assertEqual(heuristic.vertical_windows[1][1], -2)
        self.assertEqual(heuristic.vertical_windows[1][2], 0)

    def test_evaluate_vertical_with_both_players_moves(self):
        heuristic = ConnectFourHeuristic(True)
        board = [[1,2,1,2,0,0], 
                 [1,0,0,0,0,0], 
                 [2,1,0,0,0,0],
                 [0,0,0,0,0,0],
                 [0,0,0,0,0,0],
                 [0,0,0,0,0,0],
                 [0,0,0,0,0,0]]
        for i in [(0,0), (0,1), (0,2), (0,3), (1,0), (2,0), (2,1)]:
            heuristic.evaluate_relevant_windows(i[0], i[1], board)
        self.assertEqual(heuristic.vertical_windows[0][1], 0)
        self.assertEqual(heuristic.vertical_windows[0][2], 0)
        self.assertEqual(heuristic.vertical_windows[2][0], 0)

    def test_evaluate_dup_with_one_players_moves(self):
        heuristic = ConnectFourHeuristic(True)
        board = [[2,0,0,0,0,0], 
                 [1,0,0,0,0,0], 
                 [2,1,0,0,0,0],
                 [1,2,1,0,0,0],
                 [0,0,0,0,0,0],
                 [0,0,0,0,0,0],
                 [0,0,0,0,0,0]]
        for i in [(3,0), (3,1), (3,2), (2,0), (2,1), (1,0), (0,0)]:
            heuristic.evaluate_relevant_windows(i[0], i[1], board)

        self.assertEqual(heuristic.dup_windows[0][0], -2)
        self.assertEqual(heuristic.dup_windows[1][0], 8)
        self.assertEqual(heuristic.dup_windows[2][0], -4)
        self.assertEqual(heuristic.dup_windows[3][0], 2)
        self.assertEqual(heuristic.dup_windows[3][1], -2)
        self.assertEqual(heuristic.dup_windows[3][2], 2)

    def test_evaluate_dup_with_both_players_moves(self):
        heuristic = ConnectFourHeuristic(True)
        board = [[0,0,0,0,0,0], 
                 [0,0,0,0,0,0], 
                 [0,0,0,0,0,0],
                 [1,2,1,0,0,0],
                 [2,1,2,1,0,0],
                 [2,1,2,1,2,0],
                 [1,2,1,2,1,2]]
        for i in [(3,0), (3,1), (3,2), (4,0), (4,1), (4,2), (4,3), (5,0), (5,1), (5,2), (5,3), (5,4), (6,0), (6,1), (6,2), (6,3), (6,4), (6,5)]:
            heuristic.evaluate_relevant_windows(i[0], i[1], board)

        self.assertEqual(heuristic.dup_windows[2][0], 0)
        self.assertEqual(heuristic.dup_windows[1][0], 4)
        self.assertEqual(heuristic.dup_windows[0][2], 0)
        self.assertEqual(heuristic.dup_windows[1][2], 0)
        self.assertEqual(heuristic.dup_windows[2][2], 0)
        self.assertEqual(heuristic.dup_windows[0][2], 0)

    def test_evaluate_ddown_with_one_players_moves(self):
        heuristic = ConnectFourHeuristic(True)
        board = [[1,0,0,0,0,0], 
                 [1,1,2,0,0,0], 
                 [2,2,1,2,0,0],
                 [0,0,0,0,0,0],
                 [0,0,0,0,0,0],
                 [0,0,0,0,0,0],
                 [0,0,0,0,0,0]]
        for i in [(1,0), (2,0), (1,1), (2,1), (2,2), (1,2), (0,0), (2,3)]:
            heuristic.evaluate_relevant_windows(i[0], i[1], board)
        self.assertEqual(heuristic.dup_windows[0][0], 8)
        self.assertEqual(heuristic.dup_windows[1][1], 4)
        self.assertEqual(heuristic.dup_windows[0][1], -4)
        self.assertEqual(heuristic.dup_windows[2][2], 2)

    def test_evaluate_ddown_with_both_players_moves(self):
        heuristic = ConnectFourHeuristic(False)
        board = [[1,2,1,2,1,0], 
                 [2,1,2,1,0,0], 
                 [2,1,2,1,0,0],
                 [2,0,0,0,0,0],
                 [0,0,0,0,0,0],
                 [0,0,0,0,0,0],
                 [0,0,0,0,0,0]]
        for i in [(0,0), (0,1), (0,2), (0,3), (0,4), (1,0), (1,1), (1,2), (1,3), (2,0), (2,1), (2,2), (2,3), (3,0)]:
            heuristic.evaluate_relevant_windows(i[0], i[1], board)
        self.assertEqual(heuristic.ddown_windows[0][4], 0)
        self.assertEqual(heuristic.ddown_windows[0][3], 0)
        self.assertEqual(heuristic.ddown_windows[1][3], 0)
