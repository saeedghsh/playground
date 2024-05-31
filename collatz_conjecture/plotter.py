"""Plotting utils"""

from typing import Dict

import matplotlib
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
from matplotlib import animation

from collatz_sequence import CollatzSequences

BACKEND = ["Agg", "TkAgg", "Qt5Agg"][2]
matplotlib.use(BACKEND)


def plot_sequences_as_timeseries_animated(
    collatz_sequences: CollatzSequences, time_delay: int = 200
):
    """Animate the plotting of sequences as time series."""
    sequences: Dict[int, list] = collatz_sequences.sequences

    def init():
        ax.set_xlim(0, max(len(s) for s in sequences.values()) - 1)
        ax.set_ylim(1, max(max(s) for s in sequences.values()))
        marker.set_data([], [])
        return lines + [marker]

    def animate(i):
        init_value = i + 1
        # fade out previous sequences
        for j in range(init_value):
            lines[j].set_alpha(np.exp(-0.1 * (init_value - j)))
        # draw a new sequence
        y = sequences[init_value]
        x = list(range(max_length - len(y), max_length))
        lines[i].set_data(x, y)
        lines[i].set_alpha(1)
        # mark the position of the initial value on the y-axis
        marker.set_data([0], [y[0]])
        # plt.savefig(f"collatz_conjecture/images/frame_{i:03d}.png")
        # $ convert -delay 5 -loop 0 collatz_conjecture/images/*.png collatz_sequence.gif
        return lines + [marker]

    max_length = max(len(s) for s in sequences.values())
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


def plot_sequences_as_graph(collatz_sequences: CollatzSequences):
    # pylint: disable=missing-function-docstring
    graph: nx.DiGraph = collatz_sequences.graph
    layouts = {
        "spring_layout": nx.spring_layout(graph),
        "circular_layout": nx.circular_layout(graph),
        "random_layout": nx.random_layout(graph),
        "shell_layout": nx.shell_layout(graph),
        "spectral_layout": nx.spectral_layout(graph),
        "kamada_kawai_layout": nx.kamada_kawai_layout(graph),
        "planar_layout": nx.planar_layout(graph),
        "spiral_layout": nx.spiral_layout(graph),
    }

    _, axes = plt.subplots(2, 4, figsize=(16, 8))
    axes = axes.flatten()

    for ax, (layout_name, pos) in zip(axes, layouts.items()):
        nx.draw(
            graph,
            pos,
            ax=ax,
            with_labels=True,
            node_size=100,
            node_color="skyblue",
            font_size=5,
            font_color="black",
            arrows=True,
        )
        ax.set_title(layout_name)

    plt.tight_layout()
    plt.show()
