import numpy as np
from scipy.linalg import det, inv


def test_add_numbers():
    assert 1 + 1 == 2


def test_add_strings():
    assert "1" + "1" == "11"


def test_booleans():
    x = True
    y = False
    assert x is True
    assert isinstance(x, bool)
    assert x != y
    assert not x is False
    assert x and y is False
    assert x or y is True


def test_numbers():
    x, y = 4, 2
    assert isinstance(42, int)
    assert isinstance(42.0, float)
    assert x + y == 6
    assert x - y == 2
    assert x * y == 8
    assert x / y == 2.0
    assert x ** y == 16
    assert x % y == 0
    assert x // y == 2
    assert 3 < 4
    assert 3 <= 4
    assert 3 != 4
    assert 3 < 4 < 5


def test_strings():
    x = "optimal"
    assert x == "optimal"
    assert isinstance(x, str)


def test_symbols():
    A = "A"
    Battery = "Battery"
    assert A == "A"
    assert Battery == "Battery"
    assert str("Failure") == "Failure"


def test_vectors():
    x = np.array([3.1415, 1.618, 2.7182])
    assert np.allclose(np.sin(np.arange(1, 6)), [
        0.8414709848078965,
        0.9092974268256817,
        0.1411200080598672,
        -0.7568024953079282,
        -0.9589242746631385,
    ])
    assert isinstance(x, np.ndarray)
    assert x[0] == 3.1415
    assert x[-1] == 2.7182
    y = np.array([1, 2, 5, 3, 1])
    assert np.array_equal(y[0:3], [1, 2, 5])
    assert np.array_equal(y[::-1], [1, 3, 5, 2, 1])

    # Modifications
    y = list(y)
    y.append(-1)
    assert y == [1, 2, 5, 3, 1, -1]
    y.pop()
    assert y == [1, 2, 5, 3, 1]
    y.extend([2, 3])
    assert y == [1, 2, 5, 3, 1, 2, 3]
    y.sort()
    assert y == [1, 1, 2, 2, 3, 3, 5]


def test_linear_algebra():
    x = np.array([1, 2])
    y = np.array([3, 4])
    assert np.array_equal(x + y, [4, 6])
    assert np.dot(x, y) == 11
    assert np.prod(y) == 12
    assert np.array_equal(x * y, [3, 8])
    assert np.allclose(np.sin(x), [0.8414709848078965, 0.9092974268256817])
    assert np.allclose(np.sqrt(x), [1.0, 1.4142135623730951])


def test_matrices():
    X = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
    assert X.shape == (4, 3)
    assert X[1, 2] == 6
    assert np.array_equal(X[0, :], [1, 2, 3])
    assert np.array_equal(X[:, 1], [2, 5, 8, 11])

    Y = np.array([[1, 3], [3, 1]])
    assert np.allclose(inv(Y), [[-0.125, 0.375], [0.375, -0.125]])
    assert det(Y) == -8.0
