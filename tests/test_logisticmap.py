"""Test for the LogisticMap class"""

# to be able to import `chaos.logisticmap`, it is important that this
# directory (test) contains the `__init__.py`
from chaos.logisticmap import LogisticMap

R = 2.0
COUNT = 4
LENGTH = 6
X0 = [0.25, 0.5, 0.75]


def initiate_logistic_map():
    return LogisticMap(r=R, X0=X0, length=LENGTH, count=COUNT)


class TestLogisticMap:
    def test_init(self):
        lm = initiate_logistic_map()
        assert lm._r == R
        assert lm._count == COUNT
        assert lm._length == LENGTH

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
        assert True

    def test_get_XY(self):
        assert True

    def test__reset(self):
        assert True

    def test__next(self):
        assert True

    def test_scramble(self):
        assert True
