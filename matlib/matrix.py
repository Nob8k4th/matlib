from __future__ import annotations


class Matrix:
    def __init__(self, data: list[list[float]]) -> None:
        if not data or not data[0]:
            raise ValueError("Matrix data must be non-empty")
        row_length = len(data[0])
        if any(len(row) != row_length for row in data):
            raise ValueError("All rows must have the same length")
        self.data = data

    @property
    def rows(self) -> int:
        return len(self.data)

    @property
    def cols(self) -> int:
        return len(self.data[0])

    def __add__(self, other: "Matrix") -> "Matrix":
        self._ensure_same_shape(other)
        result = [
            [self.data[i][j] + other.data[i][j] for j in range(self.cols)]
            for i in range(self.rows)
        ]
        return Matrix(result)

    def __sub__(self, other: "Matrix") -> "Matrix":
        self._ensure_same_shape(other)
        result = [
            [self.data[i][j] - other.data[i][j] for j in range(self.cols)]
            for i in range(self.rows)
        ]
        return Matrix(result)

    def __mul__(self, other: "Matrix") -> "Matrix":
        if self.cols != other.rows:
            raise ValueError("Inner matrix dimensions must agree")
        result = []
        for i in range(self.rows):
            row = []
            for j in range(other.cols):
                value = sum(self.data[i][k] * other.data[j][k] for k in range(self.cols))
                row.append(value)
            result.append(row)
        return Matrix(result)

    def transpose(self) -> "Matrix":
        transposed = [[self.data[i][j] for i in range(self.rows)] for j in range(self.cols)]
        return Matrix(transposed)

    def determinant(self) -> float:
        if self.rows != self.cols:
            raise ValueError("Determinant is only defined for square matrices")
        if self.rows == 2:
            a, b = self.data[0]
            c, d = self.data[1]
            return a * d - b * c
        if self.rows == 3:
            a, b, c = self.data[0]
            d, e, f = self.data[1]
            g, h, i = self.data[2]
            return a * (e * i - f * h) + b * (d * i - f * g) + c * (d * h - e * g)
        raise ValueError("Determinant is only supported for 2x2 and 3x3 matrices")

    def _ensure_same_shape(self, other: "Matrix") -> None:
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same shape")


def identity(n: int) -> Matrix:
    if n <= 0:
        raise ValueError("Size must be positive")
    return Matrix([[1 if i == j else 0 for j in range(n)] for i in range(n)])


def zeros(m: int, n: int) -> Matrix:
    if m <= 0 or n <= 0:
        raise ValueError("Matrix dimensions must be positive")
    return Matrix([[0 for _ in range(n)] for _ in range(m)])
