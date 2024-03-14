import cProfile

from connect_four_lib.heuristic import Heuristic


def main():
    board = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 1],
        [1, 2, 1, 2, 1, 0, 2],
        [1, 2, 1, 2, 1, 2, 2],
        [1, 2, 1, 2, 1, 1, 2],
    ]

    for _ in range(1000):
        Heuristic.evaluate(board, 1)


cProfile.run("main()")