import numpy as np
from collections import namedtuple
from typing import Callable, List, Tuple, Dict, Union


# Convenience Functions
def findmax(f: Callable, xs: List) -> Tuple[float, any]:
    """
    Find the maximum value of a function applied to a list of elements
    and return both the maximum value and the corresponding element.
    """
    f_max = float('-inf')
    x_max = xs[0]
    for x in xs:
        v = f(x)
        if v > f_max:
            f_max, x_max = v, x
    return f_max, x_max


def argmax(f: Callable, xs: List) -> any:
    """
    Find the element that maximizes the function.
    """
    return findmax(f, xs)[1]


# NamedTuple and Dictionary conversion helpers
def dict_from_namedtuple(nt: namedtuple) -> Dict[str, any]:
    return {key: getattr(nt, key) for key in nt._fields}


def isequal_dict_and_namedtuple(d: Dict, nt: namedtuple) -> bool:
    return len(d) == len(nt._fields) and all(d[k] == getattr(nt, k) for k in nt._fields)


# SetCategorical Class
class SetCategorical:
    """
    Represent distributions over discrete sets.
    """

    def __init__(self, elements: List[any], weights: Union[None, List[float]] = None):
        self.elements = elements
        if weights is None:
            weights = np.ones(len(elements))

        l1_norm = np.linalg.norm(weights, ord=1)
        if l1_norm < 1e-6 or np.isinf(l1_norm):
            weights = np.ones(len(elements))

        self.weights = weights / np.sum(weights)  # Normalize weights
        self.distr = np.cumsum(self.weights)  # Cumulative distribution

    def rand(self, n: int = 1) -> Union[any, List[any]]:
        """
        Generate random samples from the distribution.
        """
        indices = np.searchsorted(self.distr, np.random.rand(n))
        if n == 1:
            return self.elements[indices[0]]
        return [self.elements[i] for i in indices]

    def pdf(self, x: any) -> float:
        """
        Calculate the probability of the given element.
        """
        return sum(w if e == x else 0.0 for e, w in zip(self.elements, self.weights))


# Example usage
if __name__ == "__main__":
    # findmax and argmax examples
    xs_outer = [1, 2, 3, 4]
    print(findmax(lambda x: -x, xs_outer))  # (-1, 1)
    print(argmax(lambda x: x ** 2, xs_outer))  # 4

    # Dictionary and NamedTuple examples
    ExampleNT = namedtuple("ExampleNT", ["a", "b", "c"])
    example_nt = ExampleNT(a=1, b=2, c=3)
    example_dict = {"a": 1, "b": 2, "c": 3}

    print(dict_from_namedtuple(example_nt))
    print(isequal_dict_and_namedtuple(example_dict, example_nt))

    # SetCategorical example
    elements = ["up", "down", "left", "right"]
    weights = [0.4, 0.2, 0.3, 0.1]
    sc = SetCategorical(elements, weights)

    print(sc.rand())  # Random sample
    print(sc.rand(5))  # Random 5 samples
    print(sc.pdf("up"))  # Probability of "up"
