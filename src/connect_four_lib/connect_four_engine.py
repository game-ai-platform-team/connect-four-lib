import random
import time

from connect_four_lib.connect_four_heuristic import ConnectFourHeuristic
from connect_four_lib.connect_four_judge import ConnectFourJudge
from game_state import GameState

INFINITY = 1000000
COLUMNS = 7


class ConnectFourEngine:
    def __init__(
        self,
        difficulty: int = 1000,
        judge: ConnectFourJudge | None = None,
        heuristic: ConnectFourHeuristic | None = None,
        choices: list[int] | None = None,
    ) -> None:
        self.__judge: ConnectFourJudge = judge or ConnectFourJudge()
        self.__choices: list[int] = choices or [3, 4, 2, 5, 1, 6, 0]
        self.__heuristic: ConnectFourHeuristic = heuristic or ConnectFourHeuristic()
        self.__difficulty: int = difficulty
        self.__start_time: float = 0

    def __is_timeout(self) -> bool:
        time_used = int((time.perf_counter() - self.__start_time) * 1000)
        return time_used >= self.__difficulty

    def add_move(self, move: str) -> None:
        move_position = self.__judge.add_move(move)

        self.__heuristic.evaluate_relevant_windows(
            move_position[0], move_position[1], self.__judge.board
        )

    def __remove_last_move(self) -> None:
        move_position = self.__judge.remove_last_move()

        self.__heuristic.evaluate_relevant_windows(
            move_position[0], move_position[1], self.__judge.board
        )

    def get_best_move(self) -> str | None:
        if len(self.__judge.get_all_moves()) <= 2:
            return str(COLUMNS // 2)

        best_move = self.iterative_deepening()

        if best_move is None:
            return None

        return str(best_move)

    def iterative_deepening(self) -> int | None:
        depth = 1
        best_move = self.__choices[0]
        best_evaluation = -INFINITY
        self.__start_time = time.perf_counter()

        while not self.__is_timeout():
            for move in self.__choices:
                evaluation = self.min_max(move, depth, -INFINITY, INFINITY, True)

                if evaluation > best_evaluation:
                    best_move = move

            depth += 1

        return best_move

    def min_max(
        self, move: int, depth: int, alpha: int, beta: int, maximizing: bool
    ) -> int:
        """
        Function that performs Minmax algorithm as DFS and returns the evaluation of last move.

        Args:
            move (int): Move to evaluate.
            depth (int): Maximum depth of DFS.
            alpha (int): Lower bound of the evaluation.
            beta (int): Upper bound of the evaluation.
            mode (bool): Determines whether to maximize evaluation.

        Returns:
            int: Evaluation of last move.
        """

        if (
            depth == 0
            or self.__judge.validate(str(move))
            not in [GameState.CONTINUE, GameState.DRAW, GameState.WIN]
            or self.__is_timeout()
        ):
            evaluation = self.__heuristic.evaluate_entire_board()

            if maximizing:
                evaluation *= -1

            return evaluation

        if maximizing:
            best_value = -INFINITY

            for next_move in self.__choices:
                self.add_move(str(move))
                new_value = self.min_max(next_move, depth - 1, alpha, beta, False)
                self.__remove_last_move()

                best_value = max(best_value, new_value)
                alpha = max(alpha, best_value)

                if alpha >= beta:
                    break
        else:
            best_value = INFINITY

            for next_move in self.__choices:
                self.add_move(str(move))
                new_value = self.min_max(next_move, depth - 1, alpha, beta, True)
                self.__remove_last_move()

                best_value = min(best_value, new_value)
                beta = min(beta, best_value)

                if alpha >= beta:
                    break

        return best_value

    def random_valid_move(self) -> str:
        move = str(random.choice(self.__judge.get_valid_locations()))
        return move
