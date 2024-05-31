"""Test for the LogisticMap class"""

import numpy as np

# to be able to import `chaos.logisticmap`, it is important that this
# directory (test) contains the `__init__.py`
from chaos.logisticmap import LogisticMap, logistic_map

R = 2.0
COUNT = 3
LENGTH = 6
X0 = [0.25, 0.50, 0.75]


def _initiate_logistic_map():
    return LogisticMap(r=R, x0=X0, length=LENGTH, count=COUNT)


class TestLogisticMap:
    # pylint: disable=missing-function-docstring
    # pylint: disable=missing-class-docstring
    def test___init__(self):
        # pylint: disable=protected-access
        lm = _initiate_logistic_map()
        assert lm.r == R
        assert lm._count == COUNT
        assert lm._length == LENGTH

    def test___str__(self):
        lm = _initiate_logistic_map()
        assert str(lm) == "LogisticMap(r=2.00, x0=[0.25, 0.50, 0.75])"

    def test___repr__(self):
        lm = _initiate_logistic_map()
        assert repr(lm) == "LogisticMap(r=2.00, x0=[0.25, 0.50, 0.75])"

    def test___len__(self):
        lm = _initiate_logistic_map()
        assert len(lm) == 3

    def test_get_r(self):
        lm = _initiate_logistic_map()
        assert lm.r == R

    def test_set_r(self):
        lm = _initiate_logistic_map()
        lm.r = R + 1.0
        assert lm.r == R + 1

    def test_get_x0(self):
        lm = _initiate_logistic_map()
        assert lm.x0 == X0

    def test_set_x0(self):
        lm = _initiate_logistic_map()
        lm.x0 = [x0 + 0.1 for x0 in X0]
        assert lm.x0 == [x0 + 0.1 for x0 in X0]

    def test_get_x(self):
        lm = _initiate_logistic_map()
        assert lm.x.shape == (6, 3)

    def test_get_xy(self):
        x = np.linspace(0, 1, 100)
        y = logistic_map(R, x)
        lm = _initiate_logistic_map()
        assert (lm.xy == np.array([x, y]).T).all()

    def test_get_cobweb(self):
        lm = _initiate_logistic_map()
        assert lm.cobweb.shape == (LENGTH, 2)

    def test_scramble(self):
        lm = _initiate_logistic_map()
        x = lm.x.copy()
        lm.scramble()
        assert x.shape == lm.x.shape == (6, 3)
        assert (lm.x != x).any()
