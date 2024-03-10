from unittest import TestCase
from unittest.mock import Mock, call

from entities.connect_four_engine import ConnectFourEngine


class TestConnectFourEngine(TestCase):
    def setUp(self) -> None:
        self.judge_mock = Mock()
        self.engine = ConnectFourEngine(judge=self.judge_mock)
        self.engine_with_judge = ConnectFourEngine()

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
