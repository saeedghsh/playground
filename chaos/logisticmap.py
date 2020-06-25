import numpy as np
import typing

logistic_map = lambda r, x: r*x*(1-x)

class LogisticMap:
    ''''''
    def __init__(
            self,
            r: float,
            X0: typing.List[float] = [],
            length: int = 200,
            count: int = 100):
        ''''''
        self._r = r

        # the logistic map curve
        x = np.linspace(0, 1, 100)
        y = logistic_map(r, x)
        self._XY = np.array([x, y]).T

        # processes generated from the logistic map
        self._X0 = X0 if len(X0) else [x0  for x0 in np.random.random(count)]
        self._X = np.array([self._X0])
        self.next(steps=length-1)
        
    def __str__(self):
        ''''''
        return 'LogisticMap(r={:.5f}, x0={:.5f})'.format(self._r, self._x0)
    
    def __repr__(self):
        ''''''
        return self.__str__()

    def __len__(self):
        '''Returns the number of processes'''
        return self._X.shape[1]
    
    @property
    def r(self):
        return self._r
                
    @property
    def X0(self):
        return self._X0

    @property
    def X(self):
        return self._X
    
    @property
    def XY(self):
        return self._XY

    @r.setter
    def r(self, r: float):
        assert isinstance(r, float) and 0 <= r <= 4
        self._r = r
        length = self._X.shape[0]
        x = np.linspace(0, 1, 100)
        y = logistic_map(r, x)
        self._XY = np.array([x, y]).T
        self.reset()
        self.next(steps=length-1)
        
    @X0.setter
    def X0(self, X0: typing.List[float]):
        assert isinstance(X0, list)
        assert all([isinstance(x0, float) for x0 in X0])
        assert all([0<=x0<=1 for x0 in X0])
        self._X0 = X0
        self.reset()

    def reset(self):
        ''''''
        self._X = np.array([[x0 for x0 in self._X0]])
        
    def next(self, steps: int = 1):
        ''''''
        for _ in range(steps):
            self._X = np.append(
                self._X,
                np.atleast_2d(logistic_map(self._r, self._X[-1,:])),
                axis=0)


