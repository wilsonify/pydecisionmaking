import math

import pytest


def test_named_functions():
    def f1_sum(x, y):
        return x + y

    assert f1_sum(3, 0.1415) == pytest.approx(3.1415)

    def f2(x, y):
        return x + y

    assert f2(3, 0.1415) == pytest.approx(3.1415)


def test_anonymous_functions():
    def h(x):
        return x ** 2 + 1

    assert h(3) == 10

    def g(f, a, b):
        return [f(a), f(b)]

    assert g(h, 5, 10) == [26, 101]
    assert g(lambda x: pytest.approx(math.sin(x) + 1), 10, 20) == [pytest.approx(0.4559788891106302),
                                                                   pytest.approx(1.9129452507276277)]


def test_callable_objects():
    class StructureA:
        def __init__(self, a, b):
            self.a = a
            self.b = b

        def __call__(self, y=None):
            if y is None:
                return self.a + self.b
            return y * self.a + self.b

    x = StructureA(22, 8)
    assert x() == 30
    assert x(2) == 52


def test_optional_arguments():
    def f3(x=10):
        return x ** 2

    assert f3() == 100
    assert f3(3) == 9

    def f4(x, y, z=1):
        return x * y + z

    assert f4(1, 2, 3) == 5
    assert f4(1, 2) == 3


def test_keyword_arguments():
    def f5(x=0):
        return x + 1

    assert f5() == 1
    assert f5(x=10) == 11

    def f6(x, y=10, *, z=2):
        return (x + y) * z

    assert f6(1) == 22
    assert f6(2, z=3) == 36
    assert f6(2, 3) == 10
    assert f6(2, 3, z=1) == 5


def test_dispatch():
    def f_plus_const(x):
        if isinstance(x, int):
            return x + 10
        elif isinstance(x, float):
            return x + 3.1415

    assert f_plus_const(1) == 11
    assert f_plus_const(1.0) == pytest.approx(4.1415)
    assert f_plus_const(1.3) == pytest.approx(4.4415)

    def f(x):
        if isinstance(x, float):
            return 3.1415
        return 5

    assert f([3, 2, 1]) == 5
    assert f(0.00787499699) == pytest.approx(3.1415)


def f(x, y, z):
    if isinstance(x, list):
        return [xi + yi - zi for xi, yi, zi in zip(x, y, z)]
    else:
        return x + y - z


def test_splatting():
    a = [3, 1, 2]
    assert f(*a) == 2

    b = (2, 2, 0)
    assert f(*b) == 4

    assert f([2, 2], [0, 0], [1, 1]) == [1, 1]
