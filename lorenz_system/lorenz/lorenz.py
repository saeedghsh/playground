"""Lorenz Attractor"""

# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

from dataclasses import dataclass
from typing import Sequence

import numpy as np
from scipy.integrate import solve_ivp
from scipy.integrate._ivp.ivp import OdeResult


class TimeLine:
    def __init__(self, start: int, end: int, count: int):
        self._start = start
        self._end = end
        self._times = np.linspace(start, end, count)

    @property
    def times(self) -> np.ndarray:
        return self._times

    @property
    def start(self) -> int:
        return self._start

    @property
    def end(self) -> int:
        return self._end


@dataclass
class LorenzParameters:
    sigma: float
    rho: float
    beta: float


class LorenzSystem:
    def __init__(
        self,
        time_line: TimeLine,
        parameters: LorenzParameters,
        initial_points: Sequence[float],
    ):
        self._time_line = time_line
        self._parameters = parameters
        self._solution: OdeResult = solve_ivp(
            self.lorenz_system,
            (time_line.start, time_line.end),
            initial_points,
            args=(parameters.sigma, parameters.rho, parameters.beta),
            dense_output=True,
        )

    @staticmethod
    def lorenz_system(t: float, point, sigma: float, rho: float, beta: float):
        # pylint: disable=unused-argument
        x, y, z = point
        dx_dt = sigma * (y - x)
        dy_dt = x * (rho - z) - y
        dz_dt = x * y - beta * z
        return [dx_dt, dy_dt, dz_dt]

    def solve(self) -> np.ndarray:
        """Solve for the actual points on the attractor"""
        return self._solution.sol(self._time_line.times)
