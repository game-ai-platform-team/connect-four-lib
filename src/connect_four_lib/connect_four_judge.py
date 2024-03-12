from connect_four_lib.connect_four_heuristic import ConnectFourHeuristic
from connect_four_lib.heuristic import Heuristic
from connect_four_lib.judge import Judge
from connect_four_lib.win_checker import WinChecker
from game_state import GameState


class ConnectFourJudge(Judge):
    def __init__(
        self,
        moves: list[int] | None = None,
        board: list[list[int]] | None = None,
        heuristic: ConnectFourHeuristic | None = None,
    ) -> None:
        self.__board: list[list[int]] = board or self.initialize_board()
        self.__moves: list[int] = moves or []
        self.__heuristic: ConnectFourHeuristic = heuristic or ConnectFourHeuristic()
        self.win_checker = WinChecker()

    @property
    def board(self) -> list[list[int]]:
        return self.__board

    def initialize_board(self, rows: int = 6, columns: int = 7) -> list[list[int]]:
        board = [([0] * rows) for i in range(columns)]
        return board

    def get_last_move(self) -> tuple[int, int] | None:
        if not self.__moves:
            return None

        last_move = None
        column = self.__moves[-1]

        for row in range(len(self.__board[column]) - 1, -1, -1):
            if self.__board[column][row] != 0:
                last_move = (column, row)
                break

        return last_move

    def validate(self, move: str) -> GameState:
        state = GameState.CONTINUE
        if not self.__check_valid_move(move):
            return GameState.INVALID

        if not self.__check_illegal_move(int(move)):
            return GameState.ILLEGAL

        if self.__is_draw():
            state = GameState.DRAW
        elif self.__is_win():
            state = GameState.WIN

        return state

    def add_move(self, move: str) -> tuple[int, int]:
        column = int(move)
        move_position = (-1, -1)

        for row in range(len(self.__board[column])):
            if self.__board[column][row] == 0:
                move_position = (column, row)

                self.__board[column][row] = (len(self.__moves)) % 2 + 1
                self.__moves.append(column)
                self.__heuristic.evaluate_relevant_windows(column, row, self.board)

                break

        return move_position

    ##Removes a move to the judge and re-evaluates relevant windows to it
    def remove_last_move(self) -> tuple[int, int]:
        move = self.get_last_move()

        if not move:
            raise IndexError

        self.__moves.pop()
        self.__board[move[0]][move[1]] = 0

        return move

    def get_debug_info(self):
        pass

    def analyze(self, color: int = 1) -> float:
        if self.__is_draw():
            return 0

        return Heuristic.evaluate(self.__board, color)

    def get_all_moves(self) -> list[str]:
        return [str(move) for move in self.__moves]

    def __check_valid_move(self, move: str) -> bool:
        move_int = -1
        try:
            move_int = int(move)
        except ValueError:
            return False

        if not 0 <= move_int <= len(self.__board):
            return False

        return True

    def __check_illegal_move(self, move: int) -> bool:
        if self.__board[move][-1] != 0:
            return False

        return True

    def is_game_over(self) -> GameState:
        if self.__is_win():
            return GameState.WIN
        if self.__is_draw():
            return GameState.DRAW
        return GameState.CONTINUE

    def __is_draw(self) -> bool:
        return len(self.__moves) == 42

    def __is_win(self) -> bool:
        return self.win_checker.check_win(self.__board)

    def is_valid_location(self, column):
        return self.__board[column][-1] == 0

    def get_valid_locations(self) -> list[int]:
        valid_locations = [col for col in range(7) if self.is_valid_location(col)]

        return valid_locations
