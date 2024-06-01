# Chaotic Systems
Python implementation and experimentation with few simplistic chaotic systems.

* Logistic Map: <img src="https://render.githubusercontent.com/render/math?math=x_{t %2B 1}=rx_{t}(x_{t} %2B 1)">  
  <p align="center">
      <img src="https://github.com/saeedghsh/playground/blob/master/images/logisticmap_animation.gif" width="900">
  </p>

## Usage
```bash
pip install -r requirements.txt
python main.py logisticmap --length 100 --count 500
```
for help:
```bash
python main.py -h
python main.py logisticmap -h
```

## laundry list
* [x] separate parsers for different type of systems (with subparser)
* [x] generate chaotic processes via logistic maps
  - [ ] reproduce all the plots from [here](https://en.wikipedia.org/wiki/Logistic_map)
    + [x] frequency spectrum
    + [x] [cobweb plot](https://en.wikipedia.org/wiki/Cobweb_plot)
    + [ ] [Bifurcation diagram](https://en.wikipedia.org/wiki/Bifurcation_diagram)
    + [ ] "lyapunov exponent" v.s. `r`: In mathematics the Lyapunov
      exponent or Lyapunov characteristic exponent of a dynamical
      system is a quantity that characterizes the rate of separation
      of infinitesimally close trajectories.

    + [ ] Two- and three-dimensional [Poincaré plots](https://en.wikipedia.org/wiki/Poincar%C3%A9_plot)
  - [ ] use [Tent map](https://en.wikipedia.org/wiki/Tent_map) instead of "Logistic map"
  - [ ] use the "[hyperbolic tangent](https://en.wikipedia.org/wiki/Hyperbolic_functions) map" instead of "Logistic map".

* [ ] the 2D plot from the derivative of the process: <img src="https://render.githubusercontent.com/render/math?math=(x,y)=(dX_{t}, dX_{t %2B 1})">

* [ ] List other chaotic systems
  - [ ] [Arnold tongue](https://en.wikipedia.org/wiki/Arnold_tongue)
  - [ ] double-rod pendulum
  - [ ] Lorenz attractor 
  - [ ] Mobility VS time of blue/red cars from [here](https://en.wikipedia.org/wiki/Chaos_theory)
  - [ ] [Three-body problem](https://en.wikipedia.org/wiki/Three-body_problem)

* [ ] [dynamic mode decomposition](https://en.wikipedia.org/wiki/Dynamic_mode_decomposition)

* [ ] ? predicting chaos ("Although, 3-body is rather a simpler chaotic system" -Adam) "[Newton vs the machine: solving the chaotic three-body problem using deep neural networks](https://arxiv.org/abs/1910.07291)"
* [ ] ? stochastic chaos

## References
* https://en.wikipedia.org/wiki/Arnold_tongue#Standard_circle_map


```python
class LogisticMap_:
    # pylint: disable=missing-class-docstring
    # pylint: disable=missing-function-docstring
    def __init__(self, r: float, length: int = 200):
        if not 0 <= r <= 4:
            raise ValueError(f"Parameter r is expected to be in [1, 4], provided: {r}")
        self._r = r
        self._x0 = np.random.random()
        self._length = length
        self._sequence: np.ndarray
        self._cobweb: np.ndarray
        self._polynomial_map: np.ndarray
        self._construct()

    def _construct(self):
        self._compute_sequence()
        self._compute_cobweb()

    def _logistic_map(self, x: float) -> float:
        return self._r * x * (1 - x)

    def _compute_sequence(self):
        """Compute and cache the full sequence."""
        sequence = [self._x0]
        for _ in range(self._length - 1):
            sequence.append(self._logistic_map(sequence[-1]))
        self._sequence = np.array(sequence)

    def _compute_cobweb(self):
        xy = np.zeros((self._length, 2))
        xy[0, :] = [self._x0, 0]
        for n in range(1, self._length - 1, 2):
            # TODO: can we use the sequence itself and not call _logistic_map again?
            xy[n, :] = [xy[n - 1, 0], self._logistic_map(xy[n - 1, 0])]
            xy[n + 1, :] = [xy[n, 1], xy[n, 1]]
        self._cobweb = xy

    @property
    def r(self):
        return self._r

    @r.setter
    def r(self, r: float):
        if not 0 <= r <= 4:
            raise ValueError(f"Parameter r is expected to be in [1, 4], provided: {r}")
        self._r = r

    @property
    def cobweb(self):
        return self._cobweb

```