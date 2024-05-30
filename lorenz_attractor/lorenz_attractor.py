"""Lorenz Attractor"""
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

from typing import Sequence
import numpy
from scipy.integrate import solve_ivp
from scipy.integrate._ivp.ivp import OdeResult
import matplotlib.pyplot as plt

class LorenzSystem:  
    def __init__(
        self,
        time_start: int = 0,
        time_end: int = 100,
        time_points_count: int = 10000,
        initial_point: Sequence[float] = [0.1, 0.0, 0.0],
        sigma: float = 10.0,
        rho: float = 28.0,
        beta: float = 8.0 / 3.0,
    ):
        self._time_start = time_start
        self._time_end = time_end
        self._initial_point = initial_point
        self._sigma = sigma
        self._rho = rho
        self._beta = beta
        self._time_points = numpy.linspace(time_start, time_end, time_points_count)
        self._solution = solve_ivp(
            self.lorenz_system,
            (self.time_start, self.time_end),
            self.initial_point,
            args=(self.sigma, self.rho, self.beta),
            dense_output=True,
        )


    @property
    def time_start(self) -> int:
        return self._time_start
    @property
    def time_end(self) -> int:
        return self._time_end
    @property
    def initial_point(self) -> Sequence[float]:
        return self._initial_point
    @property
    def sigma(self) -> float:
        return self._sigma
    @property
    def rho(self) -> float:
        return self._rho
    @property
    def beta(self) -> float:
        return self._beta
    @property
    def time_points(self) -> numpy.ndarray:
        return self._time_points
    @property
    def solution(self) -> OdeResult:
        return self._solution

    @staticmethod
    def lorenz_system(t: float, point, sigma: float, rho: float, beta: float):  # pylint: disable=unused-argument
        x, y, z = point
        dx_dt = sigma * (y - x)
        dy_dt = x * (rho - z) - y
        dz_dt = x * y - beta * z
        return [dx_dt, dy_dt, dz_dt]

    def solve(self) -> numpy.ndarray:
        # Solve for the actual points on the attractor
        return self.solution.sol(self.time_points)

lorenz = LorenzSystem()
solution_points = lorenz.solve()


# Plotting the attractor
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(solution_points[0], solution_points[1], solution_points[2])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Lorenz Attractor')
plt.show()
