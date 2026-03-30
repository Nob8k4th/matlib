from matlib.matrix import Matrix, identity, zeros


def test_matrix_addition():
    a = Matrix([[1, 2], [3, 4]])
    b = Matrix([[5, 6], [7, 8]])
    assert (a + b).data == [[6, 8], [10, 12]]


def test_matrix_subtraction():
    a = Matrix([[5, 7], [9, 11]])
    b = Matrix([[1, 2], [3, 4]])
    assert (a - b).data == [[4, 5], [6, 7]]


def test_matrix_transpose():
    matrix = Matrix([[1, 2, 3], [4, 5, 6]])
    assert matrix.transpose().data == [[1, 4], [2, 5], [3, 6]]


def test_matrix_determinant_2x2():
    matrix = Matrix([[4, 6], [3, 8]])
    assert matrix.determinant() == 14


def test_identity_generation():
    assert identity(3).data == [[1, 0, 0], [0, 1, 0], [0, 0, 1]]


def test_zeros_generation():
    assert zeros(2, 3).data == [[0, 0, 0], [0, 0, 0]]


def test_matrix_multiplication_case_one():
    a = Matrix([[1, 2], [3, 4]])
    b = Matrix([[5, 6], [7, 8]])
    assert (a * b).data == [[19, 22], [43, 50]]


def test_matrix_multiplication_case_two():
    a = Matrix([[2, 1], [0, 3]])
    b = Matrix([[1, 4], [2, 5]])
    assert (a * b).data == [[4, 13], [6, 15]]


def test_matrix_determinant_3x3_case_one():
    matrix = Matrix([[6, 1, 1], [4, -2, 5], [2, 8, 7]])
    assert matrix.determinant() == -306


def test_matrix_determinant_3x3_case_two():
    matrix = Matrix([[3, 2, 1], [1, 0, 2], [4, 1, 5]])
    assert matrix.determinant() == 1
