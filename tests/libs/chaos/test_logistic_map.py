# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
from functools import partial

import numpy as np
import pytest

from libs.chaos.logistic_map import cobweb, logistic_map


@pytest.mark.parametrize(
    "r, x, expected",
    [
        (2.5, 0.5, 0.625),  # Single float test case
        (2.5, np.array([0.1, 0.5, 0.9]), np.array([0.225, 0.625, 0.225])),  # Numpy array test case
        (3.7, 0.0, 0.0),  # Edge case where x is 0
        (3.7, 1.0, 0.0),  # Edge case where x is 1
        (4.0, 0.5, 1.0),  # Edge case where x is 0.5
    ],
)
def test_logistic_map(r, x, expected):
    result = logistic_map(r, x)
    if isinstance(expected, np.ndarray):
        np.testing.assert_allclose(
            result, expected, rtol=1e-5, err_msg=f"Expected {expected}, got {result}"
        )
    else:
        assert result == pytest.approx(expected), f"Expected {expected}, got {result}"


def _linear_map(x: float) -> float:
    """A simple map function for testing cobweb"""
    return 2 * x


@pytest.mark.parametrize(
    "map_function, x0, length, expected",
    [
        (_linear_map, 1.0, 5, np.array([[1.0, 0], [1.0, 2.0], [2.0, 2.0], [2.0, 4.0], [4.0, 4.0]])),
        (_linear_map, 0.5, 3, np.array([[0.5, 0], [0.5, 1.0], [1.0, 1.0]])),
        (_linear_map, 0.0, 5, np.array([[0.0, 0], [0.0, 0.0], [0.0, 0.0], [0.0, 0.0], [0.0, 0.0]])),
    ],
)
def test_cobweb_with_linear_map(map_function, x0, length, expected):
    result = cobweb(map_function, x0, length)
    np.testing.assert_allclose(
        result, expected, rtol=1e-5, err_msg=f"Expected {expected}, got {result}"
    )


@pytest.mark.parametrize(
    "map_function, x0, length, expected",
    [
        (
            partial(logistic_map, r=0.2),
            0.9274860037134183,
            4,
            np.array(
                [[0.927486, 0.0], [0.927486, 0.01345114], [0.01345114, 0.01345114], [0.0, 0.0]]
            ),
        ),
        (
            partial(logistic_map, r=3.6),
            0.7703202667912032,
            4,
            np.array(
                [[0.77032027, 0.0], [0.77032027, 0.63693703], [0.63693703, 0.63693703], [0.0, 0.0]]
            ),
        ),
    ],
)
def test_cobweb_with_logistic_map(map_function, x0, length, expected):
    result = cobweb(map_function, x0, length)
    np.testing.assert_allclose(
        result, expected, rtol=1e-5, err_msg=f"Expected {expected}, got {result}"
    )


if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__]))
