import numpy as np


class SimpleRandomWalk:
    ''''''
    def __init__(self, length: int):
        ''''''
        assert isinstance(length, int) and length > 0
        self._length = length
        self._T = np.arange(length)
        self._Y = np.random.randint(0, 2, length) * 2 - 1
        self._Y[0] = 0
        self._X = np.add.accumulate(self._Y)

    def __repr__(self):
        ''''''
        return {'length': self._length}

    def __str__(self):
        ''''''
        return 'SimpleRandomWalk(length={:d})'.format(self._length)

    @property
    def X(self):
        '''getter'''
        return self._X

    @property
    def T(self):
        '''getter'''
        return self._T
