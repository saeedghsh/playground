"""Functionalities for plotting chaotic processes

SlidingFigure: An object to plot the "logistic map" curve and
    processes, with interactive control of the "r" parameters of the
    "logistic map"
"""

from functools import partial
from types import SimpleNamespace
from typing import List

import matplotlib.pyplot as plt
import matplotlib.widgets
import numpy as np

from libs.chaos.logistic_map import generate_data, logistic_map


class LogisticMapVisualizer:
    # pylint: disable=missing-class-docstring
    # pylint: disable=too-few-public-methods
    def __init__(self, sequences_count: int, sequences_length: int):
        self._sequences_count = sequences_count
        self._sequences_length = sequences_length
        self._fig = plt.figure(figsize=(18, 8))
        self._axes = SimpleNamespace(
            curve_and_cobweb=plt.subplot2grid((9, 4), (0, 0), rowspan=8, colspan=1),
            sequences=plt.subplot2grid((9, 4), (0, 1), rowspan=4, colspan=3),
            frequency=plt.subplot2grid((9, 4), (4, 1), rowspan=4, colspan=3),
            slider=plt.subplot2grid((9, 4), (8, 0), rowspan=1, colspan=4),
        )
        self._plots = SimpleNamespace(curve=None, cobweb=None, sequences=None, frequency=None)
        self._slider = matplotlib.widgets.Slider(
            self._axes.slider, "r", 0.0, 4.0, valinit=0.2, valstep=0.2
        )
        self._slider.on_changed(self._update)
        self._fig.tight_layout()
        self._draw_all()
        plt.show()

    def _generate_data(self) -> SimpleNamespace:
        r = self._slider.val
        logistic_map_func = partial(logistic_map, r=r)
        return generate_data(logistic_map_func, self._sequences_count, self._sequences_length)

    def _draw_all(self):
        data = self._generate_data()
        self._plot_curve(data.curve_points)
        self._plot_cobweb(data.cobweb_points)
        self._plot_sequences(data.sequences)
        self._plot_frequency(data.frequency_response)

    def _plot_curve(self, points: np.ndarray):
        axis = self._axes.curve_and_cobweb
        self._plots.curve = axis.plot(points[:, 0], points[:, 1], label="logistic map")[0]
        axis.plot([0, 1], [0, 1], "k", label="linear")
        axis.set_title("logistic map vs. linear")
        axis.set_xlabel("x[t-1]")
        axis.set_ylabel("x[t]")
        axis.axis("equal")
        axis.legend(loc="upper left", fancybox=True, shadow=False, framealpha=0.6)

    def _plot_cobweb(self, points: np.ndarray):
        axis = self._axes.curve_and_cobweb
        self._plots.cobweb = axis.plot(points[:, 0], points[:, 1], "r", alpha=0.7, label="cobweb")[
            0
        ]

    def _plot_sequences(self, sequences: List[np.ndarray]):
        axis = self._axes.sequences
        self._plots.sequences = [axis.plot(s, "k", linewidth=0.3, alpha=0.6)[0] for s in sequences]
        axis.set_title(f"{len(sequences)} chaotic processes")
        axis.set_ylim([0, 1])
        axis.set_xlabel("t")
        axis.set_ylabel("x[t]")

    def _plot_frequency(self, signal: np.ndarray):
        axis = self._axes.frequency
        self._plots.frequency = axis.plot(signal, "k", linewidth=0.3, alpha=0.6)[0]
        axis.set_title("frequency spectrum")
        axis.set_ylim([signal.real.min() - 1, signal.real.max() + 1])
        axis.set_xlabel("f")
        axis.set_ylabel("spectrum")

    def _update(self, _):
        data = self._generate_data()
        self._plots.curve.set_ydata(data.curve_points[:, 1])
        self._plots.cobweb.set_data(data.cobweb_points[:, 0], data.cobweb_points[:, 1])
        for i, p in enumerate(self._plots.sequences):
            p.set_ydata(data.sequences[i])
        self._plots.frequency.set_ydata(data.frequency_response)
        self._plots.frequency.axes.set_ylim(
            [data.frequency_response.real.min() - 1, data.frequency_response.real.max() + 1]
        )
        self._fig.canvas.draw_idle()
