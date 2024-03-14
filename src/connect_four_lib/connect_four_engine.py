import random
import time

from connect_four_lib.config import INFINITY
from connect_four_lib.connect_four_judge import ConnectFourJudge
from connect_four_lib.game_state import GameState


class ConnectFourEngine:
    def __init__(
        self,
        difficulty: int = 1000,
        judge: ConnectFourJudge | None = None,
        choices: list[int] | None = None,
        weight: int = 2,
    ) -> None:
        self.judge: ConnectFourJudge = judge or ConnectFourJudge()
        self.__choices: list[int] = choices or [3, 4, 2, 5, 1, 6, 0]
        self.__difficulty: int = difficulty
        self.__start_time: float = 0
        self.__color: int = -1
        self.__weight: int = weight

    def __is_timeout(self) -> bool:
        time_used = (time.process_time() - self.__start_time) * 1000
        return time_used >= self.__difficulty

    def add_move(self, move: str) -> None:
        self.judge.add_move(move)

    def get_best_move(self) -> str | None:
        if len(self.judge.get_all_moves()) <= 2:
            return str(3)

        best_move = self.iterative_deepening()

        if best_move is None:
            return None

        return str(best_move)

    def iterative_deepening(self) -> int | None:
        self.__color = len(self.judge.get_all_moves()) % 2 + 1
        depth = 1
        best_move = self.__choices[0]
        self.__start_time = time.process_time()

        while not self.__is_timeout():
            best_move = max(
                self.__choices, key=lambda move: self.min_max(move, depth, False)
            )
            depth += 1

        return best_move

    def min_max(
        self,
        move: int,
        depth: int,
        maximizing: bool = True,
        alpha: float = -INFINITY,
        beta: float = INFINITY,
    ) -> float:
        """
        Function that performs Minmax algorithm as DFS and returns the evaluation of last move.

        Args:
            move (int): Move to evaluate.
            depth (int): Maximum depth of DFS.
            maximizing (bool): Determines whether to maximize evaluation. Defaults to True.
            alpha (int, optional): Lower bound of the evaluation. Defaults to -INFINITY.
            beta (int, optional): Upper bound of the evaluation. Defaults to INFINITY.

        Returns:
            int: Evaluation of last move.
        """

        if self.judge.validate(str(move)) not in [
            GameState.CONTINUE,
            GameState.DRAW,
            GameState.WIN,
        ]:
            return -INFINITY

        if depth == 0:
            return self.judge.analyze(self.__color)

        if maximizing:
            best_value = -INFINITY

            for next_move in self.__choices:
                self.judge.add_move(str(move))
                new_value = self.__weight**depth * self.min_max(
                    next_move, depth - 1, False, alpha, beta
                )
                self.judge.remove_last_move()

                best_value = max(best_value, new_value)
                alpha = max(alpha, best_value)

                if alpha >= beta:
                    break
        else:
            best_value = INFINITY

            for next_move in self.__choices:
                self.judge.add_move(str(move))
                new_value = self.__weight**depth * self.min_max(
                    next_move, depth - 1, True, alpha, beta
                )
                self.judge.remove_last_move()

                best_value = min(best_value, new_value)
                beta = min(beta, best_value)

                if alpha >= beta:
                    break

        return best_value

    def random_valid_move(self) -> str:
        move = str(random.choice(self.judge.get_valid_moves()))
        return move
