from modelspec import *
from modelspec.utils import *

from modelspec.utils import _val_info

import numpy as np


try:
    import unittest2 as unittest
except ImportError:
    import unittest


class TestUtils(unittest.TestCase):
    def test_evaluate(self):

        assert evaluate("33") == 33.0
        assert evaluate("33") == 33
        assert evaluate(33) == 33
        params = {"p": 33}
        assert evaluate("p+p", params, verbose=True) == 66

        assert type(evaluate("33")) == int
        assert type(evaluate("33.0")) == int
        assert type(evaluate("33.1")) == float
        assert type(evaluate("33.1a")) == str

        assert type(evaluate("33.1a")) == str

        import random

        rng = random.Random(1234)

        # print('random: %s'%evaluate('1*random()',rng=rng))
        assert evaluate("1*random()", rng=rng) == 0.9664535356921388

        assert evaluate("math.sin(math.pi/2)", verbose=True) == 1

        assert evaluate([1, 2, 3], verbose=True)[2] == 3

        params = {"a": np.array([0, 1, 0]), "b": np.array([1, 1, 3])}

        assert evaluate("a+b", params, verbose=True)[2] == 3

    def test_val_info_tuple(self):
        print(_val_info((1, 2)))
        print(_val_info((("test", 1), 2)))
        print(_val_info((("test", object()), 2)))


if __name__ == "__main__":
    tu = TestUtils()
    tu.test_evaluate()
