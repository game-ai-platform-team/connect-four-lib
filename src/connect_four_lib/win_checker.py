class WinChecker:
    def __init__(self):
        pass

    def check_win(self, board):
        # Check for horizontal win
        for row in board:
            for col in range(len(row) - 3):
                if row[col] == row[col + 1] == row[col + 2] == row[col + 3] != 0:
                    return True

        # Check for vertical win
        for col in range(len(board[0])):
            for row in range(len(board) - 3):
                if (
                    board[row][col]
                    == board[row + 1][col]
                    == board[row + 2][col]
                    == board[row + 3][col]
                    != 0
                ):
                    return True

        # Check for diagonal upwards win
        for row in range(len(board) - 3):
            for col in range(len(board[0]) - 3):
                if (
                    board[row][col]
                    == board[row + 1][col + 1]
                    == board[row + 2][col + 2]
                    == board[row + 3][col + 3]
                    != 0
                ):
                    return True

        # Check for diagonal downwards win
        for row in range(3, len(board)):
            for col in range(len(board[0]) - 3):
                if (
                    board[row][col]
                    == board[row - 1][col + 1]
                    == board[row - 2][col + 2]
                    == board[row - 3][col + 3]
                    != 0
                ):
                    return True

        return False
