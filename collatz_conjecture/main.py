"""Collatz Conjecture"""

import sys
from typing import Sequence
import argparse

from utils import memory_guard_decorator

from collatz_sequence import CollatzSequences
from plotter import plot_sequences_as_timeseries_animated


def _parse_arguments(argv: Sequence[str]) -> argparse.Namespace:  # pragma: no cover
    parser = argparse.ArgumentParser(description="Collatz Conjecture")
    parser.add_argument("-s", "--start", type=int, default=1)
    parser.add_argument("-e", "--end", type=int, default=100)
    return parser.parse_args(argv)


@memory_guard_decorator(threshold=500)
def _main(argv: Sequence[str]):
    args = _parse_arguments(argv)
    collatz_sequences = CollatzSequences(args.start, args.end)
    plot_sequences_as_timeseries_animated(collatz_sequences.sequences, time_delay=10)


if __name__ == "__main__":
    sys.exit(_main(sys.argv[1:]))
