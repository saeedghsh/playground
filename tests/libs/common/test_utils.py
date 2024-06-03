# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
from unittest.mock import MagicMock, patch

import pytest

from libs.common.utils import memory_guard_decorator


def test_memory_guard_decorator():
    mock_process = MagicMock()
    mock_memory_info = MagicMock()
    mock_memory_info.rss = 150 * 1024**2  # 150 MB
    mock_process.memory_info.return_value = mock_memory_info

    with patch("psutil.Process", return_value=mock_process):

        @memory_guard_decorator(threshold=100)
        def test_func():
            return "test_result"

        with patch("sys.exit") as mock_exit:
            result = test_func()
            assert result == "test_result"
            mock_exit.assert_called_once_with(1)

    mock_memory_info.rss = 50 * 1024**2  # 50 MB

    with patch("psutil.Process", return_value=mock_process):

        @memory_guard_decorator(threshold=100)
        def test_func_low_memory():
            return "test_result_low_memory"

        with patch("sys.exit") as mock_exit:
            result = test_func_low_memory()
            assert result == "test_result_low_memory"
            mock_exit.assert_not_called()


@pytest.mark.parametrize(
    "memory_usage, threshold, should_exit",
    [
        (150, 100, True),
        (50, 100, False),
        (100, 100, False),
    ],
)
def test_memory_guard_decorator_param(memory_usage, threshold, should_exit):
    mock_process = MagicMock()
    mock_memory_info = MagicMock()
    mock_memory_info.rss = memory_usage * 1024**2  # Convert MB to bytes
    mock_process.memory_info.return_value = mock_memory_info

    with patch("psutil.Process", return_value=mock_process):

        @memory_guard_decorator(threshold=threshold)
        def test_func():
            return "test_result"

        with patch("sys.exit") as mock_exit:
            result = test_func()
            assert result == "test_result"
            if should_exit:
                mock_exit.assert_called_once_with(1)
            else:
                mock_exit.assert_not_called()


if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__]))
