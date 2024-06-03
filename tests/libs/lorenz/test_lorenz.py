# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
import numpy as np
import pytest

from libs.lorenz.lorenz import LorenzParameters, TimeLine


def test_timeline_initialization():
    timeline = TimeLine(start=0, end=10, count=5)
    assert timeline.start == 0
    assert timeline.end == 10
    expected_times = np.linspace(0, 10, 5)
    np.testing.assert_array_equal(timeline.times, expected_times)


@pytest.mark.parametrize(
    "start, end, count, expected_times",
    [
        (0, 10, 5, np.linspace(0, 10, 5)),
        (1, 5, 3, np.linspace(1, 5, 3)),
        (2, 8, 4, np.linspace(2, 8, 4)),
    ],
)
def test_timeline_times(start, end, count, expected_times):
    timeline = TimeLine(start=start, end=end, count=count)
    np.testing.assert_array_equal(timeline.times, expected_times)
    assert timeline.start == start
    assert timeline.end == end


def test_timeline_single_value():
    timeline = TimeLine(start=5, end=5, count=1)
    assert timeline.start == 5
    assert timeline.end == 5
    np.testing.assert_array_equal(timeline.times, np.array([5]))


def test_lorenz_parameters_initialization():
    params = LorenzParameters(sigma=10.0, rho=28.0, beta=2.66667)
    assert params.sigma == 10.0
    assert params.rho == 28.0
    assert params.beta == 2.66667


@pytest.mark.parametrize(
    "sigma, rho, beta",
    [
        (10.0, 28.0, 2.66667),
        (14.0, 35.0, 3.0),
        (8.0, 25.0, 2.5),
    ],
)
def test_lorenz_parameters_values(sigma, rho, beta):
    params = LorenzParameters(sigma=sigma, rho=rho, beta=beta)
    assert params.sigma == sigma
    assert params.rho == rho
    assert params.beta == beta


if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__]))
