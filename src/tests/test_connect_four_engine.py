from unittest import TestCase
from unittest.mock import Mock, call, patch

from connect_four_lib.connect_four_engine import ConnectFourEngine
from connect_four_lib.connect_four_judge import ConnectFourJudge


def single_depth_analyze_mock(self, color):
    evaluations = {1: 2, 2: 3}
    move = self._ConnectFourJudge__moves[-1]

    return evaluations[move]


def two_depth_analyze_mock(self, color):
    evaluations = {(1, 1): 2, (1, 2): 1, (2, 1): 3, (2, 2): 4}
    moves = tuple(self._ConnectFourJudge__moves)

    return evaluations[moves]


class TestConnectFourEngine(TestCase):
    def setUp(self) -> None:
        self.judge_mock = Mock()
        self.engine = ConnectFourEngine(judge=self.judge_mock)
        self.engine_with_judge = ConnectFourEngine(False)

    def test_make_move_adds_move_to_judges(self):
        self.engine.add_move("1")
        self.engine.add_move("5")
        self.engine.add_move("2")

        self.judge_mock.add_move.assert_has_calls([call("1"), call("5"), call("2")])

    def test_get_best_move_return_value_up_to_two_moves(self):
        self.judge_mock.get_all_moves.return_value = []
        self.assertEqual(self.engine.get_best_move(), str(3))

        self.judge_mock.get_all_moves.return_value = [1]
        self.assertEqual(self.engine.get_best_move(), str(3))

        self.judge_mock.get_all_moves.return_value = [2, 3]
        self.assertEqual(self.engine.get_best_move(), str(3))

    @patch.object(ConnectFourJudge, "analyze", single_depth_analyze_mock)
    def test_min_max_with_depth_one_returns_evaluation_of_move(self):
        judge_mock = Mock(wraps=ConnectFourJudge())
        engine = ConnectFourEngine(judge=judge_mock, choices=[1, 2])

        self.assertEqual(engine.min_max(1, 1), 2)
        self.assertEqual(engine.min_max(2, 1), 3)

    @patch.object(ConnectFourJudge, "analyze", two_depth_analyze_mock)
    def test_min_max_with_depth_two_and_minimizing_returns_minimum_of_next_moves(self):
        judge_mock = Mock(wraps=ConnectFourJudge())
        engine = ConnectFourEngine(judge=judge_mock, choices=[1, 2])

        self.assertEqual(engine.min_max(1, 2, False), 1)
        self.assertEqual(engine.min_max(2, 2, False), 3)

    def test_get_best_move_blocks_opponents_win_column(self):
        for i in ["1", "2", "1", "2", "1"]:
            self.engine_with_judge.add_move(i)
        self.assertEqual(self.engine_with_judge.get_best_move(), "1")

    def test_get_best_move_blocks_opponents_win_row(self):
        for i in ["0", "3", "0", "1", "3", "2"]:
            self.engine_with_judge.add_move(i)
        self.assertEqual(self.engine_with_judge.get_best_move(), "4")

    def test_get_best_move_blocks_opponents_win_diagonal_up(self):
        for i in ["3", "3", "3", "4", "4", "4", "5", "5", "5", "5"]:
            self.engine_with_judge.add_move(i)
        self.assertEqual(self.engine_with_judge.get_best_move(), "2")

    def test_get_best_move_blocks_opponents_win_diagonal_down(self):
        for i in ["3", "3", "3", "2", "2", "2", "1", "1", "1", "1"]:
            self.engine_with_judge.add_move(i)
        self.assertEqual(self.engine_with_judge.get_best_move(), "4")
