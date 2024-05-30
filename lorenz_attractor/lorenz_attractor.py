"""Lorenz Attractor"""

# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

from typing import Sequence
import numpy as np
from scipy.integrate import solve_ivp
from scipy.integrate._ivp.ivp import OdeResult


class LorenzSystem:
    def __init__(
        self,
        time_start: int,
        time_end: int,
        time_points_count: int,
        initial_points: Sequence[float],
        sigma: float,
        rho: float,
        beta: float,
    ):
        self._time_points = np.linspace(time_start, time_end, time_points_count)
        self._solution: OdeResult = solve_ivp(
            self.lorenz_system,
            (time_start, time_end),
            initial_points,
            args=(sigma, rho, beta),
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
        return self._solution.sol(self._time_points)
