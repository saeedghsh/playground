"""Collatz Conjecture"""

import sys
from typing import Sequence
import argparse
import matplotlib.pyplot as plt


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


def _plot_sequences_as_timeseries(sequences: Sequence[Sequence[int]]):
    plt.figure(figsize=(20, 15))
    max_length = max(len(s) for s in sequences)
    for y in sequences:
        x = list(range(max_length - len(y), max_length))
        plt.plot(x, y, marker="o", linestyle="-")
    plt.title("Collatz Sequences")
    plt.xlabel("Step")
    plt.ylabel("Value")
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
    _plot_sequences_as_timeseries(sequences)


if __name__ == "__main__":
    sys.exit(_main(sys.argv[1:]))
