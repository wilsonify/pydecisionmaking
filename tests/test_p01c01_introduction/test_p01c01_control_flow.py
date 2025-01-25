import itertools


def test_conditional_evaluation():
    x = 10
    y = 24132

    if x < y:
        print("run this if x < y")
    elif x > y:
        print("run this if x > y")
    else:
        print("run this if x == y")

    def f(x2):
        return x2 if x2 > 0 else 0

    assert f(-10) == 0
    assert f(10) == 10


def test_loops():
    X = [1, 2, 3, 4, 6, 8, 11, 13, 16, 18]
    s = 0
    while X:
        s += X.pop()
    assert s == sum([1, 2, 3, 4, 6, 8, 11, 13, 16, 18])

    X = [1, 2, 3, 4, 6, 8, 11, 13, 16, 18]
    s = 0
    for i in range(len(X)):
        s += X[i]
    assert s == sum(X)

    X = [1, 2, 3, 4, 6, 8, 11, 13, 16, 18]
    s = 0
    for y in X:
        s += y
    assert s == sum(X)


def test_iterators():
    X = ["feed", "sing", "ignore"]
    assert list(enumerate(X)) == [(0, "feed"), (1, "sing"), (2, "ignore")]
    assert list(range(1, len(X) + 1)) == [1, 2, 3]

    Y = [-5, -0.5, 0.0]
    assert list(zip(X, Y)) == [("feed", -5.0), ("sing", -0.5), ("ignore", 0.0)]

    assert list(itertools.chain.from_iterable(itertools.combinations(X, r) for r in range(len(X) + 1))) == [
        (),
        ('feed',),
        ('sing',),
        ('ignore',),
        ('feed', 'sing'),
        ('feed', 'ignore'),
        ('sing', 'ignore'),
        ('feed', 'sing', 'ignore')
    ]

    assert list(range(1, len(X) + 1)) == [1, 2, 3]

    z = [[1, 2], [3, 4], [5, 6]]

    assert list(itertools.product(X, Y)) == [
        ("feed", -5.0), ("feed", -0.5), ("feed", 0.0),
        ("sing", -5.0), ("sing", -0.5), ("sing", 0.0),
        ("ignore", -5.0), ("ignore", -0.5), ("ignore", 0.0),
    ]
