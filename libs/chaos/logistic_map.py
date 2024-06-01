"""This module provides objects for chaotic processes"""

import numpy as np


def _logistic_map(r: float, x: np.ndarray) -> np.ndarray:
    """Return next value of a logistic map, give parameter r and current value x."""
    return r * x * (1 - x)


def _cobweb(r: float, x0: float, length: int) -> np.ndarray:
    """Return the Cobweb diagram of a logistic map sequence."""
    xy = np.zeros((length, 2))
    xy[0, :] = (x0, 0)
    for n in range(1, length - 1, 2):
        xy[n, :] = [xy[n - 1, 0], _logistic_map(r, xy[n - 1, 0])]
        xy[n + 1, :] = [xy[n, 1], xy[n, 1]]
    return xy


class LogisticMap:
    # pylint: disable=missing-function-docstring
    """The chaotic processes are constructed based on a set of initial
    values (optionally provided or internally generated) and according
    to "logistic map"
    """

    def __init__(self, r: float, length: int, count: int):
        self._r = r
        self._count = count
        self._length = length
        self._x0: list
        self._x: np.ndarray
        self._xy: np.ndarray
        self._cobweb: np.ndarray
        self._construct()

    def _construct(self):
        self._x0 = list(np.random.random(self._count))
        self._x = np.array([self._x0])
        self._compute_sequences(steps=self._length - 1)
        x = np.linspace(0, 1, self._count)
        y = _logistic_map(self._r, x)
        self._xy = np.array([x, y]).T
        self._cobweb = _cobweb(self._r, self._x0[0], self._length)

    def _compute_sequences(self, steps):
        for _ in range(steps):
            self._x = np.append(
                self._x, np.atleast_2d(_logistic_map(self._r, self._x[-1, :])), axis=0
            )

    @property
    def r(self):
        return self._r

    @r.setter
    def r(self, r: float):
        assert isinstance(r, float) and 0 <= r <= 4
        self._r = r
        self._construct()

    @property
    def x(self):
        return self._x

    @property
    def xy(self):
        return self._xy

    @property
    def cobweb(self):
        return self._cobweb
