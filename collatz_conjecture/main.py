"""Collatz Conjecture"""

from functools import lru_cache
import sys
from typing import Sequence
import argparse


from plotter import plot_sequences_as_timeseries_animated
from utils import memory_usage_guard


@lru_cache(maxsize=None)
def _collatz_rule(n: int) -> int:
    return n * 3 + 1 if n % 2 == 1 else n // 2


def _generate_sequence(initial_number: int) -> Sequence[int]:
    n = initial_number
    sequence = [n]
    while n != 1:
        n = _collatz_rule(n)
        sequence.append(n)
    return sequence


def _parse_arguments(argv: Sequence[str]) -> argparse.Namespace:  # pragma: no cover
    parser = argparse.ArgumentParser(description="Collatz Conjecture")
    parser.add_argument("-s", "--start", type=int, default=1)
    parser.add_argument("-e", "--end", type=int, default=100)
    return parser.parse_args(argv)


@memory_usage_guard(threshold=500)
def _main(argv: Sequence[str]):
    args = _parse_arguments(argv)
    sequences = []
    if not args.start <= args.end:
        raise ValueError("end must be greater than or equal to start")
    for n in range(args.start, args.end + 1):
        sequences.append(_generate_sequence(n))
    plot_sequences_as_timeseries_animated(sequences, time_delay=10)


if __name__ == "__main__":
    sys.exit(_main(sys.argv[1:]))
