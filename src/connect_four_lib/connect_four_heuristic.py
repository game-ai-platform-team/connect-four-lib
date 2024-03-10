class ConnectFourHeuristic:
    def __init__(self, first_player: bool = True) -> None:
        ## 4 tables for storing the evaluation of 4 space windows starting from each space
        self.horizontal_windows: list[list[int]] = [([0] * 6) for i in range(4)]
        self.vertical_windows: list[list[int]] = [([0] * (3)) for i in range(7)]
        self.ddown_windows: list[list[int]] = [([0] * (6)) for i in range(4)]
        self.dup_windows: list[list[int]] = [([0] * (3)) for i in range(4)]
        self.__board: list[list[int]] = [([0] * (6)) for i in range(7)]

        if first_player:
            self.my_color = 1
            self.opponent_color = 2
        else:
            self.my_color = 2
            self.opponent_color = 1

    ## Recognize 4 space windows that the given coordinates are in and re-evaluates them
    def evaluate_relevant_windows(self, col, row, board):
        self.__board = board
        self.__evaluate_horizontal(col, row)
        self.__evaluate_vertical(col, row)
        self.__evaluate_ddown(col, row)
        self.__evaluate_dup(col, row)

    def __evaluate_horizontal(self, col, row):
        window = [0, 0, 0, 0]
        low_cap = max(col - 3, 0)
        top_cap = min(col + 1, 4)
        for i in range(low_cap, top_cap):
            for x in range(4):
                window[x] = self.__board[i + x][row]
            self.horizontal_windows[i][row] = self.evaluate_single_window(window)

    def __evaluate_vertical(self, col, row):
        window = [0, 0, 0, 0]
        low_cap = max(0, row - 3)
        top_cap = min(row + 1, 3)
        for i in range(low_cap, top_cap):
            for x in range(4):
                window[x] = self.__board[col][i + x]
            self.vertical_windows[col][i] = self.evaluate_single_window(window)

    def __evaluate_ddown(self, col, row):
        window = [0, 0, 0, 0]
        low_space = min(3, col, 5 - row)
        low_cap = -1 * low_space
        top_space = min(3, 6 - col, row)
        top_cap = low_cap + low_space + top_space - 2
        for i in range(low_cap, top_cap):
            for x in range(4):
                window[x] = self.__board[col + i + x][row - i - x]
            self.ddown_windows[col + i][row - i] = self.evaluate_single_window(window)

    def __evaluate_dup(self, col, row):
        window = [0, 0, 0, 0]
        low_space = min(3, col, row)
        low_cap = -1 * low_space
        top_space = min(6 - col, 5 - row)
        top_cap = low_cap + low_space + top_space - 2
        for i in range(low_cap, top_cap):
            for x in range(4):
                window[x] = self.__board[col + i + x][row + i + x]
            self.dup_windows[col + i][row + i] = self.evaluate_single_window(window)

    def evaluate_single_window(self, window: list[int]) -> int:
        my_pieces = window.count(self.my_color)
        opponent_pieces = window.count(self.opponent_color)
        if my_pieces == 4:
            return 1000
        if opponent_pieces == 4:
            return -1000
        if my_pieces > 0 and opponent_pieces > 0:
            return 0
        if my_pieces > 0:
            return 2**my_pieces
        if opponent_pieces > 0:
            return -1 * 2**opponent_pieces
        return 0

    ##Checks a win has been found in any window
    def is_win(self) -> bool:
        return (
            self.check_win(self.horizontal_windows)
            or self.check_win(self.vertical_windows)
            or self.check_win(self.dup_windows)
            or self.check_win(self.ddown_windows)
        )

    def check_win(self, window: list[list[int]]):
        for i in window:
            for j in i:
                if j in (1000, -1000):
                    return True
        return False

    ##Calculates the sum of the evaluations of all 4-space windows on the board and returns it
    def evaluate_entire_board(self) -> int:
        evaluation = 0
        for i in self.horizontal_windows:
            for j in i:
                evaluation += j
        for i in self.vertical_windows:
            for j in i:
                evaluation += j
        for i in self.dup_windows:
            for j in i:
                evaluation += j
        for i in self.ddown_windows:
            for j in i:
                evaluation += j
        return evaluation
