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
        board = [
            [1, 2, 0, 0, 0, 0],
            [1, 2, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
        ]
        for i in [(0, 0), (0, 1), (1, 0), (1, 1)]:
            heuristic.evaluate_relevant_windows(i[0], i[1], board)
        self.assertEqual(heuristic.horizontal_windows[0][0], 4)
        self.assertEqual(heuristic.horizontal_windows[1][0], 2)
        self.assertEqual(heuristic.horizontal_windows[2][0], 0)
        self.assertEqual(heuristic.horizontal_windows[0][1], -4)
        self.assertEqual(heuristic.horizontal_windows[1][1], -2)
        self.assertEqual(heuristic.horizontal_windows[2][1], 0)

    def test_evaluate_horizontal_with_both_players_moves(self):
        heuristic = ConnectFourHeuristic(True)
        board = [
            [2, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [2, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
        ]
        for i in [(4, 0), (3, 0), (5, 0), (0, 0), (1, 0)]:
            heuristic.evaluate_relevant_windows(i[0], i[1], board)
        self.assertEqual(heuristic.horizontal_windows[3][0], 0)
        self.assertEqual(heuristic.horizontal_windows[0][0], 0)

    def test_evaluate_vertical_with_one_players_moves(self):
        heuristic = ConnectFourHeuristic(True)
        board = [
            [1, 1, 1, 0, 0, 0],
            [2, 2, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
        ]
        for i in [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1)]:
            heuristic.evaluate_relevant_windows(i[0], i[1], board)
        self.assertEqual(heuristic.vertical_windows[0][0], 8)
        self.assertEqual(heuristic.vertical_windows[0][1], 4)
        self.assertEqual(heuristic.vertical_windows[0][2], 2)
        self.assertEqual(heuristic.vertical_windows[1][0], -4)
        self.assertEqual(heuristic.vertical_windows[1][1], -2)
        self.assertEqual(heuristic.vertical_windows[1][2], 0)

    def test_evaluate_vertical_with_both_players_moves(self):
        heuristic = ConnectFourHeuristic(True)
        board = [
            [1, 2, 1, 2, 0, 0],
            [1, 0, 0, 0, 0, 0],
            [2, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
        ]
        for i in [(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (2, 0), (2, 1)]:
            heuristic.evaluate_relevant_windows(i[0], i[1], board)
        self.assertEqual(heuristic.vertical_windows[0][1], 0)
        self.assertEqual(heuristic.vertical_windows[0][2], 0)
        self.assertEqual(heuristic.vertical_windows[2][0], 0)

    def test_evaluate_dup_with_one_players_moves(self):
        heuristic = ConnectFourHeuristic(True)
        board = [
            [2, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0],
            [2, 1, 0, 0, 0, 0],
            [1, 2, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
        ]
        for i in [(3, 0), (3, 1), (3, 2), (2, 0), (2, 1), (1, 0), (0, 0)]:
            heuristic.evaluate_relevant_windows(i[0], i[1], board)


import unittest

from connect_four_lib.connect_four_judge import ConnectFourJudge
from game_state import GameState


class TestConnectFourJudge(unittest.TestCase):
    def setUp(self) -> None:
        self.judge = ConnectFourJudge()

        self.board_empty_six_by_seven_board = [[0] * 6 for i in range(7)]
        self.board_empty_four_by_four_board = [[0] * 4 for i in range(4)]

        self.board_one_column_full = [[1, 2, 1, 2, 1, 2]]
        self.board_one_column_full.extend([[0] * 6 for i in range(6)])

        self.board_one_column_one_move = [[1, 0, 0, 0, 0, 0]]
        self.board_one_column_one_move.extend([[0] * 6 for i in range(6)])
        self.board_full = [
            [1, 1, 2, 2, 1, 1],
            [2, 2, 1, 1, 2, 2],
            [1, 1, 2, 1, 2, 1],
            [2, 2, 1, 1, 2, 2],
        ]

    def test_move_not_convertable_to_int_is_invalid(self):
        self.assertEqual(self.judge.validate("aaa"), GameState.INVALID)
        self.assertEqual(self.judge.validate("7ä"), GameState.INVALID)
        self.assertEqual(self.judge.validate("-1ö"), GameState.INVALID)
        self.assertEqual(self.judge.validate("1.01"), GameState.INVALID)
        self.assertEqual(self.judge.validate("1.0"), GameState.INVALID)

    def test_upwards_diagonal_win_in_corner_is_recognized(self):
        for i in [6, 6, 6, 6, 5, 5, 5, 5, 5, 6, 6, 4, 4, 4, 4, 3, 3, 2, 3]:
            self.judge.add_move(i)

        self.assertEqual(self.judge.is_game_over(), GameState.WIN)

    def test_move_outside_board_return_invalid_state(self):
        self.assertEqual(self.judge.validate("-1"), GameState.INVALID)
        self.assertEqual(self.judge.validate("70"), GameState.INVALID)
        self.assertEqual(self.judge.validate("1000"), GameState.INVALID)
        self.assertEqual(self.judge.validate("-10000"), GameState.INVALID)

    def test_valid_move_returns_continue(self):
        self.assertEqual(self.judge.validate("3"), GameState.CONTINUE)
        self.assertEqual(self.judge.validate("6"), GameState.CONTINUE)
        self.assertEqual(self.judge.validate("0"), GameState.CONTINUE)

    def test_move_returns_illegal_if_column_is_full(self):
        judge = ConnectFourJudge(
            moves=[1, 2, 1, 2, 1, 2], board=self.board_one_column_full
        )
        self.assertEqual(judge.validate("0"), GameState.ILLEGAL)

    def test_move_returns_continue_if_column_is_not_full(self):
        judge = ConnectFourJudge(
            moves=[1, 2, 1, 2, 1, 2], board=self.board_one_column_full
        )
        self.assertEqual(judge.validate("1"), GameState.CONTINUE)
        self.assertEqual(judge.validate("6"), GameState.CONTINUE)

    def test_getboard_gets_board(self):
        self.assertEqual(self.judge.board, self.board_empty_six_by_seven_board)

    def test_add_move_adds_move(self):
        self.judge.add_move(0)
        self.assertNotEqual(self.judge.board[0][0], 0)

    def test_add_move_adds_correct_move(self):
        self.judge.add_move(0)
        self.assertEqual(self.judge.board[0][0], 1)
        self.judge.add_move(3)
        self.assertEqual(self.judge.board[3][0], 2)

    def test_get_board_returns_correct_board_after_five_moves(self):
        judge = ConnectFourJudge()
        for i in [0, 0, 1, 3, 0]:
            judge.add_move(i)

        self.assertEqual(
            judge.board,
            [
                [1, 2, 1, 0, 0, 0],
                [1, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [2, 0, 0, 0, 0, 0],
                [0] * 6,
                [0] * 6,
                [0] * 6,
            ],
        )

    def test_play_a_full_game_that_results_in_a_draw(self):
        judge = ConnectFourJudge()

        for _ in range(6):
            judge.add_move(0)
            judge.add_move(1)
            judge.add_move(2)
            judge.add_move(4)
            judge.add_move(3)
            judge.add_move(5)
            judge.add_move(6)

        self.assertEqual(judge.is_game_over(), GameState.DRAW)

    def test_horizontal_win_is_recognized(self):
        for i in [0, 0, 1, 1, 2, 2, 3]:
            self.judge.add_move(i)
        self.assertEqual(self.judge.is_game_over(), GameState.WIN)

    def test_horizontal_win_is_recognized_part_two(self):
        for i in [1, 2, 3, 4, 1, 1, 2, 2, 3, 3, 4]:
            self.judge.add_move(i)
        self.assertEqual(self.judge.is_game_over(), GameState.WIN)

    def test_vertical_win_is_recognized(self):
        for i in [2, 0, 2, 1, 2, 1, 2]:
            self.judge.add_move(i)
        self.assertEqual(self.judge.is_game_over(), GameState.WIN)

    def test_vertical_win_is_recognized_part_two(self):
        for i in [0, 6, 6, 6, 0, 6, 0, 6, 2, 6]:
            self.judge.add_move(i)
        self.assertEqual(self.judge.is_game_over(), GameState.WIN)

    def test_upwards_diagonal_win_is_recognized(self):
        for i in [1, 0, 3, 3, 3, 2, 2, 4, 4, 4, 4]:
            self.judge.add_move(i)
        self.assertEqual(self.judge.is_game_over(), GameState.WIN)

    def test_downwards_diagonal_win_is_recognized(self):
        for i in [5, 4, 4, 2, 2, 2, 2, 1, 3, 3, 3]:
            self.judge.add_move(i)

        self.assertEqual(self.judge.is_game_over(), GameState.WIN)

    def test_downwards_diagonal_win_in_corner_is_recognized(self):
        judge = ConnectFourJudge()
        for i in [0, 1, 0, 3, 2, 2, 1, 1, 0, 0]:
            judge.add_move(i)
        self.assertEqual(judge.is_game_over, GameState.WIN)

    def test_move_list_is_empty_at_start(self):
        self.assertEqual(self.judge.get_all_moves(), [])

    def test_add_move_updates_moves(self):
        self.judge.add_move(0)

        self.assertEqual(self.judge.get_all_moves(), ["0"])

    def test_calculate_latest_move(self):
        self.judge.add_move("3")
        latest_move = self.judge.get_last_move()
        self.assertEqual(latest_move, (3, 0))

    def test_remove_latest(self):
        self.judge.add_move("3")
        self.judge.add_move("2")
        self.judge.remove_last_move()
        latest_move = self.judge.get_last_move()
        self.assertEqual(latest_move, (3, 0))

    def test_calculate_latest_move_after_four_moves(self):
        self.judge.add_move("3")
        self.judge.add_move("3")
        self.judge.add_move("3")
        self.judge.add_move("3")

        latest_move = self.judge.get_last_move()
        self.assertEqual(latest_move, (3, 3))

    def test_get_valid_locations(self):
        self.assertEqual(self.judge.get_valid_locations(), [0, 1, 2, 3, 4, 5, 6])

        self.assertEqual(heuristic.dup_windows[0][0], -2)
        self.assertEqual(heuristic.dup_windows[1][0], 8)
        self.assertEqual(heuristic.dup_windows[2][0], -4)
        self.assertEqual(heuristic.dup_windows[3][0], 2)
        self.assertEqual(heuristic.dup_windows[3][1], -2)
        self.assertEqual(heuristic.dup_windows[3][2], 2)

    def test_evaluate_dup_with_both_players_moves(self):
        heuristic = ConnectFourHeuristic(True)
        board = [
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [1, 2, 1, 0, 0, 0],
            [2, 1, 2, 1, 0, 0],
            [2, 1, 2, 1, 2, 0],
            [1, 2, 1, 2, 1, 2],
        ]
        for i in [
            (3, 0),
            (3, 1),
            (3, 2),
            (4, 0),
            (4, 1),
            (4, 2),
            (4, 3),
            (5, 0),
            (5, 1),
            (5, 2),
            (5, 3),
            (5, 4),
            (6, 0),
            (6, 1),
            (6, 2),
            (6, 3),
            (6, 4),
            (6, 5),
        ]:
            heuristic.evaluate_relevant_windows(i[0], i[1], board)

        self.assertEqual(heuristic.dup_windows[2][0], 0)
        self.assertEqual(heuristic.dup_windows[1][0], 4)
        self.assertEqual(heuristic.dup_windows[0][2], 0)
        self.assertEqual(heuristic.dup_windows[1][2], 0)
        self.assertEqual(heuristic.dup_windows[2][2], 0)
        self.assertEqual(heuristic.dup_windows[0][2], 0)

    def test_evaluate_ddown_with_one_players_moves(self):
        heuristic = ConnectFourHeuristic(True)
        board = [
            [1, 0, 0, 0, 0, 0],
            [1, 1, 2, 0, 0, 0],
            [2, 2, 1, 2, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
        ]
        for i in [(1, 0), (2, 0), (1, 1), (2, 1), (2, 2), (1, 2), (0, 0), (2, 3)]:
            heuristic.evaluate_relevant_windows(i[0], i[1], board)
        self.assertEqual(heuristic.dup_windows[0][0], 8)
        self.assertEqual(heuristic.dup_windows[1][1], 4)
        self.assertEqual(heuristic.dup_windows[0][1], -4)
        self.assertEqual(heuristic.dup_windows[2][2], 2)

    def test_evaluate_ddown_with_both_players_moves(self):
        heuristic = ConnectFourHeuristic(False)
        board = [
            [1, 2, 1, 2, 1, 0],
            [2, 1, 2, 1, 0, 0],
            [2, 1, 2, 1, 0, 0],
            [2, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
        ]
        for i in [
            (0, 0),
            (0, 1),
            (0, 2),
            (0, 3),
            (0, 4),
            (1, 0),
            (1, 1),
            (1, 2),
            (1, 3),
            (2, 0),
            (2, 1),
            (2, 2),
            (2, 3),
            (3, 0),
        ]:
            heuristic.evaluate_relevant_windows(i[0], i[1], board)
        self.assertEqual(heuristic.ddown_windows[0][4], 0)
        self.assertEqual(heuristic.ddown_windows[0][3], 0)
        self.assertEqual(heuristic.ddown_windows[1][3], 0)
