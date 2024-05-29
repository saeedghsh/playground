"""Collatz Conjecture"""

import sys
from typing import Sequence
import argparse
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np


def _parse_arguments(argv: Sequence[str]) -> argparse.Namespace:  # pragma: no cover
    parser = argparse.ArgumentParser(description="Hornet Field entry point")
    parser.add_argument("-s", "--start", type=int, default=1)
    parser.add_argument("-e", "--end", type=int, default=100)
    return parser.parse_args(argv)


def _collatz_rule(n: int) -> int:
    return n * 3 + 1 if n % 2 == 1 else n // 2


def _generate_sequence(initial_number: int) -> Sequence[int]:
    n = initial_number
    sequence = [n]
    while n != 1:
        n = _collatz_rule(n)
        sequence.append(n)
    return sequence


def _plot_sequences_as_timeseries_animated(
    sequences: Sequence[Sequence[int]], time_delay: int = 200
):
    def init():
        ax.set_xlim(0, max(len(seq) for seq in sequences) - 1)
        ax.set_ylim(0, max(max(seq) for seq in sequences))
        return lines

    def animate(i):
        # fade out previous sequences
        for j in range(i):
            lines[j].set_alpha(np.exp(-0.1 * (i - j)))
        # draw a new sequence
        y = sequences[i]
        x = list(range(max_length - len(y), max_length))
        lines[i].set_data(x, y)
        lines[i].set_alpha(1)
        plt.title(f"Collatz Sequences - start value = {y[0]}")
        return lines

    max_length = max(len(s) for s in sequences)
    fig, ax = plt.subplots(figsize=(10, 6))
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


def _main(argv: Sequence[str]):
    args = _parse_arguments(argv)
    sequences = []
    if not args.start <= args.end:
        raise ValueError("end must be greater than or equal to start")
    for n in range(args.start, args.end + 1):
        sequences.append(_generate_sequence(n))
    _plot_sequences_as_timeseries_animated(sequences, time_delay=10)


if __name__ == "__main__":
    sys.exit(_main(sys.argv[1:]))
