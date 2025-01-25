import random


class SetCategorical:
    def __init__(self, elements, probabilities):
        self.elements = elements
        self.probabilities = probabilities

    def rand(self, n=1):
        return random.choices(self.elements, self.probabilities, k=n)

    def pdf(self, element):
        return self.probabilities[self.elements.index(element)]


def test_findmax():
    assert max([0, -10, 3], key=lambda x: x ** 2) == -10


def test_argmax():
    assert max([0, -10, 3], key=abs) == -10


def test_construct_dict_of_named_tuples():
    a_dict = {'a': 1, 'b': 2, 'c': 3}
    assert a_dict == {'a': 1, 'b': 2, 'c': 3}
    assert a_dict == {'a': 1, 'c': 3, 'b': 2}

    b_dict = {('a', 1, 'b', 1): 0.2, ('a', 1, 'b', 2): 0.8}
    print(b_dict)


def test_set_categorical():
    D = SetCategorical(["up", "down", "left", "right"], [0.4, 0.2, 0.3, 0.1])
    random_D = D.rand()[0]
    random_D_array = D.rand(5)
    assert len(random_D_array) == 5
    assert D.pdf("up") == 0.4
