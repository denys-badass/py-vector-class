from __future__ import annotations


class Vector:

    def __init__(self, x: float, y: float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, vector: Vector) -> Vector:
        return Vector(self.x + vector.x, self.y + vector.y)

    def __sub__(self, vector: Vector) -> Vector:
        return Vector(self.x - vector.x, self.y - vector.y)

    def __mul__(self, vector: Vector | float) -> Vector | float:
        if isinstance(vector, Vector):
            return self.x * vector.x + self.y * vector.y

        return Vector(self.x * vector, self.y * vector)

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple[float], end_point: tuple[float]) -> Vector:
        return Vector(end_point[0] - start_point[0], end_point[1] - start_point[1])
