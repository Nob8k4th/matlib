from __future__ import annotations

import math


class Vector:
    def __init__(self, values: list[float]) -> None:
        if not values:
            raise ValueError("Vector must contain at least one value")
        self.values = values

    def dot(self, other: "Vector") -> float:
        if len(self.values) != len(other.values):
            raise ValueError("Vectors must have the same dimension")
        return sum(a * b for a, b in zip(self.values, other.values))

    def cross(self, other: "Vector") -> "Vector":
        if len(self.values) != 3 or len(other.values) != 3:
            raise ValueError("Cross product is only defined for 3D vectors")
        a1, a2, a3 = self.values
        b1, b2, b3 = other.values
        return Vector(
            [
                a2 * b3 - a3 * b2,
                a3 * b1 - a1 * b3,
                a1 * b2 - a2 * b1,
            ]
        )

    def normalize(self) -> "Vector":
        norm = math.sqrt(sum(value * value for value in self.values))
        if norm == 0:
            return Vector([0 for _ in self.values])
        return Vector([value / norm for value in self.values])
