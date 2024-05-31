# pylint: disable=missing-module-docstring
import numpy as np


class SimpleRandomWalk:
    # pylint: disable=missing-class-docstring
    # pylint: disable=missing-function-docstring
    # pylint: disable=invalid-name
    def __init__(self, length: int):
        assert isinstance(length, int) and length > 0
        self._length = length
        self._T = np.arange(length)
        self._Y = np.random.randint(0, 2, length) * 2 - 1
        self._Y[0] = 0
        self._X = np.add.accumulate(self._Y)

    def __repr__(self) -> str:
        return f"length {self._length}"

    def __str__(self) -> str:
        return f"SimpleRandomWalk (length={self._length})"

    @property
    def X(self):
        return self._X

    @property
    def T(self):
        return self._T
