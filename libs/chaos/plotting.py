"""Functionalities for plotting chaotic processes

SlidingFigure: An object to plot the "logistic map" curve and
    processes, with interactive control of the "r" parameters of the
    "logistic map"
"""

import matplotlib.pyplot as plt
import matplotlib.widgets
from scipy import fftpack

from libs.chaos.logistic_map import LogisticMap


class LogisticMapFigure:
    # pylint: disable=missing-class-docstring
    # pylint: disable=missing-function-docstring
    # pylint: disable=too-many-instance-attributes
    # pylint: disable=too-few-public-methods
    def __init__(self, logistic_map: LogisticMap):
        self._lm = logistic_map

        self._fig = plt.figure(figsize=(18, 8))
        self._axes = [
            plt.subplot2grid((9, 4), (0, 0), rowspan=8, colspan=1),  # logistic_map
            plt.subplot2grid((9, 4), (8, 0), rowspan=1, colspan=4),  # slider
            plt.subplot2grid((9, 4), (0, 1), rowspan=4, colspan=3),  # chaotic processes
            plt.subplot2grid((9, 4), (4, 1), rowspan=4, colspan=3),  # frequency spectrum
        ]
        self._plot_logistic_map(self._axes[0])
        self._plot_cobweb(self._axes[0])
        self._plot_chaotic_processes(self._axes[2])
        self._plot_frequency_spectrum(self._axes[3])
        self._r_slider = matplotlib.widgets.Slider(
            self._axes[1], "r", 0.0, 4.0, valinit=self._lm.r, valstep=0.2
        )
        self._r_slider.on_changed(self.update)

        self._fig.tight_layout()
        plt.show()

    def _plot_logistic_map(self, axis):
        self._curve_plot = axis.plot(self._lm.xy[:, 0], self._lm.xy[:, 1], label="logistic map")[0]
        axis.plot([0, 1], [0, 1], "k", label="linear")
        axis.set_title("logistic map vs. linear")
        axis.set_xlabel("x[t-1]")
        axis.set_ylabel("x[t]")
        axis.axis("equal")
        axis.legend(loc="upper left", fancybox=True, shadow=False, framealpha=0.6)

    def _plot_cobweb(self, axis):
        self._cobweb_plot = axis.plot(
            self._lm.cobweb[:, 0], self._lm.cobweb[:, 1], "r", alpha=0.7, label="cobweb"
        )[0]

    def _plot_chaotic_processes(self, axis):
        self._processes_plot = axis.plot(self._lm.x, "k", linewidth=0.3, alpha=0.6)
        title = (
            "{:d} chaotic processes (with random initial points) generated from the logistic map"
        )
        axis.set_title(title.format(self._lm.x.shape[1]))
        axis.set_ylim([0, 1])
        axis.set_xlabel("t")
        axis.set_ylabel("x[t]")

    def _plot_frequency_spectrum(self, axis):
        x = fftpack.fft(self._lm.x[:, 0])
        self._spectrum_plot = axis.plot(x, "k", linewidth=0.3, alpha=0.6)[0]
        axis.set_title("frequency spectrum")
        axis.set_ylim([x.real.min() - 1, x.real.max() + 1])
        axis.set_xlabel("f")
        axis.set_ylabel("spectrum")

    def update(self, _):
        self._lm.r = self._r_slider.val
        self._curve_plot.set_ydata(self._lm.xy[:, 1])
        self._cobweb_plot.set_data(self._lm.cobweb[:, 0], self._lm.cobweb[:, 1])

        for i, p in enumerate(self._processes_plot):
            p.set_ydata(self._lm.x[:, i])

        x = fftpack.fft(self._lm.x[:, 0])
        self._spectrum_plot.set_ydata(x)
        self._spectrum_plot.axes.set_ylim([x.real.min() - 1, x.real.max() + 1])

        self._fig.canvas.draw_idle()

        # # for saving plots and creating animated gif
        # plt.savefig('{:.5f}'.format(self._lm.r).replace('.', '') + '.png',
        #             facecolor='w', edgecolor='w',
        #             format='png', transparent=False,
        #             bbox_inches='tight', pad_inches=0.0)
