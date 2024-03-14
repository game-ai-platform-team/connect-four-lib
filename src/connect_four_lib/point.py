class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x: int = x
        self.y: int = y

    def __add__(self, other: "Point") -> "Point":
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Point") -> "Point":
        return Point(self.x - other.x, self.y - other.y)
