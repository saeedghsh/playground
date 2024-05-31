"""This module provides objects for chaotic processes

Currently it only contains one object, namely "LogisticMap"
"""

from typing import List, Optional

import numpy as np


def logistic_map(r: float, x: np.array) -> np.array:  # pylint: disable=missing-function-docstring
    return r * x * (1 - x)


def cobweb(r: float, x0: float, length: int) -> np.array:
    # pylint: disable=missing-function-docstring
    xy = np.zeros((length, 2))
    xy[0, :] = (x0, 0)
    for n in range(1, length - 1, 2):
        xy[n, 0] = xy[n - 1, 0]
        xy[n, 1] = logistic_map(r, xy[n - 1, 0])
        xy[n + 1, 0] = xy[n, 1]
        xy[n + 1, 1] = xy[n, 1]
    return xy


class LogisticMap:
    # pylint: disable=missing-function-docstring
    # pylint: disable=too-many-instance-attributes
    """The chaotic processes are constructed based on a set of initial
    values (optionally provided or internally generated) and according
    to "logistic map"
    """

    def __init__(
        self, r: float, x0: Optional[List[float]] = None, length: int = 200, count: int = 100
    ):
        self._r = r
        self._count = count
        self._length = length

        # processes generated from the logistic map
        self._x0 = x0 or list(np.random.random(count))
        self._x = np.array([self._x0])
        self._next(steps=length - 1)

        # the logistic map curve and the cobweb
        x = np.linspace(0, 1, 100)
        y = logistic_map(r, x)
        self._xy = np.array([x, y]).T
        self._set_coweb()

    def __str__(self):
        s = "LogisticMap(r={:.2f}, x0=["
        s += ", ".join(["{:.2f}"] * len(self._x0))
        s += "])"
        return s.format(self._r, *(self._x0))

    def __repr__(self):
        return self.__str__()

    def __len__(self):
        return self._x.shape[1]

    @property
    def r(self):
        return self._r

    @r.setter
    def r(self, r: float):
        assert isinstance(r, float) and 0 <= r <= 4
        self._r = r
        length = self._x.shape[0]
        x = np.linspace(0, 1, 100)
        y = logistic_map(r, x)
        self._xy = np.array([x, y]).T
        self._set_coweb()
        self._reset()
        self._next(steps=length - 1)

    @property
    def x0(self):
        return self._x0

    @x0.setter
    def x0(self, x0: List[float]):
        if not all(0 <= i <= 1 for i in x0):
            raise ValueError("Values must always be in [0,1]")
        self._x0 = x0
        self._set_coweb()
        self._reset()

    @property
    def x(self):
        return self._x

    @property
    def xy(self):
        return self._xy

    @property
    def cobweb(self):
        return self._cobweb

    def _reset(self):
        self._x = np.array([list(self._x0)])

    def _next(self, steps: int = 1):
        for _ in range(steps):
            self._x = np.append(
                self._x, np.atleast_2d(logistic_map(self._r, self._x[-1, :])), axis=0
            )

    def _set_coweb(self):
        self._cobweb = cobweb(self._r, self._x0[0], self._length)

    def scramble(self):
        """Regenerates random initial values, and reconstructs the processes"""
        self.x0 = list(np.random.random(self._count))
        self._set_coweb()
        self._reset()
        self._next(steps=self._length - 1)
