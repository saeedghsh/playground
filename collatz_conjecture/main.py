"""Collatz Conjecture"""

from functools import lru_cache, wraps
import sys
from typing import Sequence
import argparse
import time
import psutil

from plotter import plot_sequences_as_timeseries_animated


def memory_usage_decorator(threshold: int):
    """A decorator to detect over-usage of a function to prevent crash.
    threshold is in MB."""

    def memory_usage_mb(process: psutil.Process) -> int:
        """Return memory usage in MB"""
        memory_info = process.memory_info()
        return memory_info.rss // 1024**2

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            process = psutil.Process()
            result = func(*args, **kwargs)
            memory_usage = memory_usage_mb(process)
            if memory_usage > threshold:
                print(f"Memory usage exceeded {threshold} MB. Exiting to prevent crash.")
                sys.exit(1)

            return result

        return wrapper

    return decorator


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


@memory_usage_decorator(threshold=500)
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
