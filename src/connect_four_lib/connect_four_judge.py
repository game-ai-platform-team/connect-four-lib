from connect_four_lib.connect_four_heuristic import ConnectFourHeuristic
from connect_four_lib.game_state import GameState
from connect_four_lib.judge import Judge
from connect_four_lib.point import Point


class ConnectFourJudge(Judge):
    def __init__(
        self,
        moves: list[int] | None = None,
        board: list[list[int]] | None = None,
    ) -> None:
        self.__board: list[list[int]] = board or self.initialize_board()
        self.__moves: list[int] = moves or []

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

        if self.__is_win(self.__get_point_of_move(move)):
            state = GameState.WIN

        return state

    def add_move(self, move: str) -> Point:
        column = int(move)
        point = self.__get_point_of_move(move)

        self.__board[point.y][point.x] = (len(self.__moves)) % 2 + 1
        self.__moves.append(column)
        return point

    def remove_last_move(self) -> tuple[int, int]:
        move = self.get_last_move()

        if not move:
            raise IndexError

        self.__moves.pop()
        self.__board[move[0]][move[1]] = 0

        return move

    def get_debug_info(self):
        pass

    def analyze(self, color: int) -> float:
        if self.__is_draw():
            return 0

        return ConnectFourHeuristic.evaluate(self.__board, color)

    def get_all_moves(self) -> list[str]:
        return [str(move) for move in self.__moves]

    def __get_point_of_move(self, move: str) -> Point:
        column = int(move)

        for row, point in enumerate(self.__board[column]):
            if point == 0:
                return Point(row, column)

        return Point(-1, -1)

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

    def __is_draw(self) -> bool:
        return len(self.__moves) + 1 >= 42

    def __is_win(self, point: Point) -> bool:
        offsets = [Point(0, 1), Point(1, 0), Point(1, 1), Point(1, -1)]
        color = len(self.get_all_moves()) % 2 + 1

        self.__board[point.y][point.x] = color
        consecutive_points = [
            self.__count_points_in_line(point, offset, color)
            + self.__count_points_in_line(point, -offset, color)
            - 1
            for offset in offsets
        ]
        self.__board[point.y][point.x] = 0

        return 4 in consecutive_points

    def __count_points_in_line(self, point: Point, offset: Point, color: int) -> int:
        if (
            not 0 <= point.x < len(self.__board[0])
            or not 0 <= point.y < len(self.__board)
            or self.__board[point.y][point.x] != color
        ):
            return 0

        return 1 + self.__count_points_in_line(point + offset, offset, color)

    def get_valid_moves(self) -> list[int]:
        return [move for move in range(7) if self.__check_illegal_move(move)]
