from enum import Enum


class GameState(Enum):
    CONTINUE = 0
    WIN = 1
    LOSE = 2
    DRAW = 3
    INVALID = 4
    ILLEGAL = 5
    MAX_TURNS = 6
    TIMEOUT = 7

    def __str__(self):
        values = {
            GameState.CONTINUE: "CONTINUE",
            GameState.WIN: "WIN",
            GameState.LOSE: "LOSE",
            GameState.DRAW: "DRAW",
            GameState.INVALID: "INVALID",
            GameState.ILLEGAL: "ILLEGAL",
            GameState.MAX_TURNS: "MAX_TURNS",
            GameState.TIMEOUT: "TIMEOUT",
        }
        return values[self]
