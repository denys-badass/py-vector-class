from __future__ import annotations
import math


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

    def get_normalized(self) -> Vector:
        length = self.get_length()
        norm_x = self.x / length
        norm_y = self.y / length
        return Vector(norm_x, norm_y)

    def angle_between(self, vector: Vector) -> int:
        prod = self * vector
        len_prod = self.get_length() * vector.get_length()
        degree = math.degrees(math.acos(prod / len_prod))
        return round(degree)

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 1))

    def rotate(self, angle: int) -> Vector:
        cos = math.cos(math.radians(angle))
        sin = math.sin(math.radians(angle))
        x = self.x * cos - self.y * sin
        y = self.x * sin + self.y * cos
        return Vector(x, y)

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple[float], end_point: tuple[float]) -> Vector:
        return Vector(end_point[0] - start_point[0], end_point[1] - start_point[1])
