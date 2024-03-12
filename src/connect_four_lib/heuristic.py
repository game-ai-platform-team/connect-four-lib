from config import INFINITY


class Heuristic:
    @staticmethod
    def __get_point(column: int, row: int, board: list[list[int]]) -> int:
        if not 0 <= column < len(board) or not 0 <= row < len(board[0]):
            return -1

        return board[column][row]

    @staticmethod
    def __get_windows(column: int, row: int, board: list[list[int]]) -> list[int]:
        windows = []

        windows.append(
            [Heuristic.__get_point(column, row + i, board) for i in range(4)]
        )
        windows.append(
            [Heuristic.__get_point(column + i, row, board) for i in range(4)]
        )
        windows.append(
            [Heuristic.__get_point(column + i, row + i, board) for i in range(4)]
        )
        windows.append(
            [Heuristic.__get_point(column + i, row - i, board) for i in range(4)]
        )

        return windows

    @staticmethod
    def _evaluate_window(window: list[int], color: int) -> int:
        points = window.count(color)
        empty_points = window.count(0)

        evaluation = 0

        if points == 4:
            return INFINITY

        if points + empty_points == 4:
            evaluation = points

        return evaluation

    @staticmethod
    def evaluate(board: list[list[int]], color: int) -> int:
        windows = []

        for column in range(len(board)):
            for row in range(len(board[0])):
                windows.extend(Heuristic.__get_windows(column, row, board))

        evaluation = sum(
            Heuristic._evaluate_window(window, color)
            - Heuristic._evaluate_window(window, 3 - color)
            for window in windows
        )

        return evaluation
