# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=protected-access
# pylint: disable=unused-argument
from types import SimpleNamespace
from unittest.mock import MagicMock, patch

import numpy as np
import pytest
from matplotlib.widgets import Slider

from libs.chaos.visualizer import LogisticMapVisualizer


@patch("matplotlib.pyplot.show")
@patch("libs.chaos.logistic_map.generate_data")
def test_logistic_map_visualizer(mock_generate_data, mock_show):
    # Mock data to return for generate_data
    mock_data = SimpleNamespace(
        sequences=[np.array([0.1, 0.2, 0.3])],
        cobweb_points=np.array([[0.1, 0.2], [0.2, 0.3], [0.3, 0.4]]),
        frequency_response=np.array([1.0, 0.5, 0.2]),
        curve_points=np.random.rand(100, 2),  # Ensure 100 points for curve
    )
    mock_generate_data.return_value = mock_data

    # Initialize visualizer
    visualizer = LogisticMapVisualizer(sequences_count=1, sequences_length=3)

    # Cache initial values
    initial_curve_ydata = visualizer._plots.curve.get_ydata().copy()
    initial_cobweb_xdata, initial_cobweb_ydata = visualizer._plots.cobweb.get_data()
    initial_sequences_ydata = [p.get_ydata().copy() for p in visualizer._plots.sequences]
    initial_frequency_ydata = visualizer._plots.frequency.get_ydata().copy()

    # Check if the plots are created
    assert visualizer._plots.curve is not None
    assert visualizer._plots.cobweb is not None
    assert visualizer._plots.sequences is not None
    assert visualizer._plots.frequency is not None

    # Check if the slider is created
    assert isinstance(visualizer._slider, Slider)

    # Simulate slider change and generate new mock data
    new_mock_data = SimpleNamespace(
        sequences=[np.array([0.3, 0.2, 0.1])],
        cobweb_points=np.array([[0.3, 0.2], [0.2, 0.1], [0.1, 0.0]]),
        frequency_response=np.array([0.5, 0.25, 0.1]),
        curve_points=np.random.rand(100, 2),  # Ensure 100 points for curve
    )
    mock_generate_data.return_value = new_mock_data

    with patch.object(visualizer._fig.canvas, "draw_idle", MagicMock()) as mock_draw_idle:
        visualizer._slider.set_val(0.4)
        visualizer._update(None)

        # Verify if the plots have been updated
        mock_draw_idle.assert_called()
        assert mock_draw_idle.call_count == 3

        # Ensure the data has been updated
        assert not np.array_equal(visualizer._plots.curve.get_ydata(), initial_curve_ydata)
        assert not np.array_equal(visualizer._plots.cobweb.get_data()[0], initial_cobweb_xdata)
        assert not np.array_equal(visualizer._plots.cobweb.get_data()[1], initial_cobweb_ydata)
        assert all(
            not np.array_equal(p.get_ydata(), initial_ydata)
            for p, initial_ydata in zip(visualizer._plots.sequences, initial_sequences_ydata)
        )
        assert not np.array_equal(visualizer._plots.frequency.get_ydata(), initial_frequency_ydata)

        # Check shapes and sizes to ensure correct data structure
        assert visualizer._plots.curve.get_ydata().shape == new_mock_data.curve_points[:, 1].shape
        assert (
            visualizer._plots.cobweb.get_data()[0].shape == new_mock_data.cobweb_points[:, 0].shape
        )
        assert (
            visualizer._plots.cobweb.get_data()[1].shape == new_mock_data.cobweb_points[:, 1].shape
        )
        assert visualizer._plots.sequences[0].get_ydata().shape == new_mock_data.sequences[0].shape
        assert (
            visualizer._plots.frequency.get_ydata().shape == new_mock_data.frequency_response.shape
        )


@pytest.mark.parametrize("sequences_count, sequences_length", [(1, 3), (2, 5)])
@patch("matplotlib.pyplot.show")
@patch("libs.chaos.logistic_map.generate_data")
def test_logistic_map_visualizer_param(
    mock_generate_data, mock_show, sequences_count, sequences_length
):
    mock_data = SimpleNamespace(
        sequences=[np.random.rand(sequences_length) for _ in range(sequences_count)],
        cobweb_points=np.random.rand(sequences_length, 2),
        frequency_response=np.random.rand(sequences_length),
        curve_points=np.random.rand(100, 2),  # Ensure 100 points for curve
    )
    mock_generate_data.return_value = mock_data

    visualizer = LogisticMapVisualizer(
        sequences_count=sequences_count, sequences_length=sequences_length
    )

    assert len(visualizer._plots.sequences) == sequences_count
    assert all(len(p.get_ydata()) == sequences_length for p in visualizer._plots.sequences)


if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__]))
