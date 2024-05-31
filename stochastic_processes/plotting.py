# pylint: disable=missing-module-docstring
from typing import Any

import matplotlib.pyplot as plt
import matplotlib.widgets
import numpy as np


class SlidingFigure:
    # pylint: disable=missing-class-docstring
    # pylint: disable=missing-function-docstring
    # pylint: disable=too-many-instance-attributes
    # pylint: disable=invalid-name
    def __init__(self, random_walks: list):
        assert isinstance(random_walks, list) and len(random_walks)

        self._random_walks = random_walks
        self._T = random_walks[0].T
        self._X = np.array([rw.X for rw in random_walks])
        self._bins = np.arange(self._X.min() - 0.5, self._X.max() + 1, 1)

        self._length = self._X.shape[1]
        self._X_max = np.abs(self._X.reshape(-1)).max()
        self._X_max = max([self._X_max, np.sqrt(self._T[-1])])
        self._t0 = int(self._length / 10)

        self._fig = plt.figure(figsize=(16, 8))
        self._axes = [
            plt.subplot2grid((9, 1), (0, 0), rowspan=4),
            plt.subplot2grid((9, 1), (4, 0), rowspan=4),
            plt.subplot2grid((9, 1), (8, 0), rowspan=1),
        ]

        self._time_slider = matplotlib.widgets.Slider(
            self._axes[2], "time stamp", 0, self._length, valinit=self._t0, valstep=1
        )
        self._time_slider.on_changed(self.update)

        self.plot_lines(self._axes[0])
        self.plot_hist(self._axes[1])
        self._fig.tight_layout()
        plt.show()

    def plot_lines(self, axis):
        self._lines = [
            axis.plot(rw.T[: self._t0], rw.X[: self._t0], alpha=0.7)[0] for rw in self._random_walks
        ]
        axis.plot(self._T, np.sqrt(self._T), "k-.", linewidth=0.75, label=r"$\pm\sqrt{t}$")
        axis.plot(self._T, -np.sqrt(self._T), "k-.", linewidth=0.75)
        axis.set_title('a collection of "simple random walks"')
        axis.set_xlabel("t")
        axis.set_ylabel("X")
        axis.legend(loc="upper left", fancybox=True, shadow=False, framealpha=0.6)
        # axis.axis('equal')
        axis.set_xlim([0, self._length])
        axis.set_ylim([-self._X_max, self._X_max])

    def plot_hist(self, axis):
        axis.hist(self._X[:, : self._t0].reshape(-1), bins=self._bins)
        axis.set_title('histogram of all "simple random walks" values')
        axis.set_xlabel("X")
        axis.set_ylabel("distribution")
        axis.set_xlim([self._bins.min(), self._bins.max()])

    def update_lines(self, idx: int):
        for line, rw in zip(self._lines, self._random_walks):
            line.set_data(rw.T[:idx], rw.X[:idx])

    def update_hist(self, idx: int):
        self._axes[1].cla()
        self._axes[1].hist(self._X[:, :idx].reshape(-1), bins=self._bins)
        self._axes[1].set_title('histogram of all "simple random walks" values')
        self._axes[1].set_xlabel("X")
        self._axes[1].set_ylabel("distribution")
        self._axes[1].set_xlim([self._bins.min(), self._bins.max()])

    def update(self, _: Any):
        idx = int(self._time_slider.val)
        self.update_lines(idx)
        self.update_hist(idx)
        self._fig.canvas.draw_idle()
        # plt.savefig('{:05d}.png'.format(idx),
        #             facecolor='w', edgecolor='w',
        #             format='png', transparent=False,
        #             bbox_inches='tight', pad_inches=0.0)
