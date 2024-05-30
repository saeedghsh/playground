"""Test for the LogisticMap class"""

# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring

import numpy as np

# to be able to import `chaos.logisticmap`, it is important that this
# directory (test) contains the `__init__.py`
from chaos.logisticmap import LogisticMap, logistic_map

R = 2.0
COUNT = 3
LENGTH = 6
X0 = [0.25, 0.50, 0.75]


def initiate_logistic_map():
    return LogisticMap(r=R, X0=X0, length=LENGTH, count=COUNT)


class TestLogisticMap:
    def test___init__(self):
        lm = initiate_logistic_map()
        assert lm._r == R
        assert lm._count == COUNT
        assert lm._length == LENGTH

    def test___str__(self):
        lm = initiate_logistic_map()
        assert lm.__str__() == "LogisticMap(r=2.00, x0=[0.25, 0.50, 0.75])"

    def test___repr__(self):
        lm = initiate_logistic_map()
        assert lm.__repr__() == "LogisticMap(r=2.00, x0=[0.25, 0.50, 0.75])"

    def test___len__(self):
        lm = initiate_logistic_map()
        assert len(lm) == 3

    def test_get_r(self):
        lm = initiate_logistic_map()
        assert lm.r == R

    def test_set_r(self):
        lm = initiate_logistic_map()
        lm.r = R + 1.0
        assert lm._r == R + 1

    def test_get_X0(self):
        lm = initiate_logistic_map()
        assert lm.X0 == X0

    def test_set_X0(self):
        lm = initiate_logistic_map()
        lm.X0 = [x0 + 0.1 for x0 in X0]
        assert lm._X0 == [x0 + 0.1 for x0 in X0]

    def test_get_X(self):
        lm = initiate_logistic_map()
        assert lm.X.shape == (6, 3)

    def test_get_XY(self):
        x = np.linspace(0, 1, 100)
        y = logistic_map(R, x)
        lm = initiate_logistic_map()
        assert (lm.XY == np.array([x, y]).T).all()

    def test_get_cobweb(self):
        lm = initiate_logistic_map()
        assert lm.cobweb.shape == (LENGTH, 2)

    def test__reset(self):
        lm = initiate_logistic_map()
        assert lm.X.shape == (6, 3)
        lm._reset()
        assert lm.X.shape == (1, 3)

    def test__next(self):
        lm = initiate_logistic_map()
        assert lm.X.shape == (6, 3)
        lm._reset()
        lm._next(3)
        assert lm.X.shape == (4, 3)

    def test_scramble(self):
        lm = initiate_logistic_map()
        X = lm.X.copy()
        lm.scramble()
        assert X.shape == lm.X.shape == (6, 3)
        assert (lm.X != X).any()
