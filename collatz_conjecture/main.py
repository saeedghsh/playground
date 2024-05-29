"""Collatz Conjecture"""

import sys
from typing import Sequence
import argparse

from utils import memory_usage_guard
from collatz_sequence import generate_sequences
from plotter import plot_sequences_as_timeseries_animated


def _parse_arguments(argv: Sequence[str]) -> argparse.Namespace:  # pragma: no cover
    parser = argparse.ArgumentParser(description="Collatz Conjecture")
    parser.add_argument("-s", "--start", type=int, default=1)
    parser.add_argument("-e", "--end", type=int, default=100)
    return parser.parse_args(argv)


@memory_usage_guard(threshold=500)
def _main(argv: Sequence[str]):
    args = _parse_arguments(argv)
    sequences = generate_sequences((args.start, args.end))
    plot_sequences_as_timeseries_animated(sequences, time_delay=10)


if __name__ == "__main__":
    sys.exit(_main(sys.argv[1:]))
