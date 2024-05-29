"""Plotting utils"""

from typing import Sequence
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np


def plot_sequences_as_timeseries_animated(
    sequences: Sequence[Sequence[int]], time_delay: int = 200
):
    def init():
        ax.set_xlim(0, max(len(s) for s in sequences) - 1)
        ax.set_ylim(0, max(max(s) for s in sequences))
        marker.set_data([], [])
        return lines + [marker]

    def animate(i):
        # fade out previous sequences
        for j in range(i):
            lines[j].set_alpha(np.exp(-0.1 * (i - j)))
        # draw a new sequence
        y = sequences[i]
        x = list(range(max_length - len(y), max_length))
        lines[i].set_data(x, y)
        lines[i].set_alpha(1)
        # mark the position of the initial value on the y-axis
        marker.set_data([0], [y[0]])
        return lines + [marker]

    max_length = max(len(s) for s in sequences)
    fig, ax = plt.subplots(figsize=(10, 6))

    # Marker for the first entry of each sequence
    (marker,) = ax.plot([], [], "rx", markersize=12)
    lines = [ax.plot([], [], marker="o", linestyle="-", alpha=0)[0] for _ in sequences]

    _ = animation.FuncAnimation(
        fig,
        animate,
        frames=len(sequences),
        init_func=init,
        interval=time_delay,
        blit=True,
        repeat=False,
    )

    ax.set_xlabel("Step")
    ax.set_ylabel("Value (in logarithmic scale)")
    ax.set_yscale("log")
    plt.title("Collatz Sequences")
    plt.grid(True)
    plt.tight_layout()
    plt.show()
