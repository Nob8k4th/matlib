import pytest

from matlib.vector import Vector


@pytest.mark.parametrize(
    "left,right,expected",
    [
        ([1, 2, 3], [4, 5, 6], 32),
    ],
)
def test_dot_product(left, right, expected):
    assert Vector(left).dot(Vector(right)) == expected


def test_cross_product():
    result = Vector([1, 0, 0]).cross(Vector([0, 1, 0]))
    assert result.values == [0, 0, 1]


def test_cross_product_dimension_error():
    with pytest.raises(ValueError):
        Vector([1, 2]).cross(Vector([3, 4]))


def test_normalize_non_zero_vector():
    normalized = Vector([3, 4, 0]).normalize()
    assert normalized.values == [0.6, 0.8, 0.0]


def test_normalize_zero_vector_should_raise():
    with pytest.raises(ValueError):
        Vector([0, 0, 0]).normalize()
