"""Collatz Conjecture"""

import argparse
import sys
from typing import Sequence

from collatz import CollatzSequences
from plotter import plot_sequences_as_graph, plot_sequences_as_timeseries_animated
from utils import memory_guard_decorator


def _parse_arguments(argv: Sequence[str]) -> argparse.Namespace:  # pragma: no cover
    parser = argparse.ArgumentParser(description="Collatz Conjecture")
    parser.add_argument("-s", "--start", type=int, default=1)
    parser.add_argument("-e", "--end", type=int, default=100)
    parser.add_argument("-p", "--plot", choices=["timeseries", "graph"], default="timeseries")
    return parser.parse_args(argv)


@memory_guard_decorator(threshold=500)
def _main(argv: Sequence[str]):
    args = _parse_arguments(argv)
    collatz_sequences = CollatzSequences(args.start, args.end)
    if args.plot == "timeseries":
        plot_sequences_as_timeseries_animated(collatz_sequences.sequences, time_delay=10)
    elif args.plot == "graph":
        plot_sequences_as_graph(collatz_sequences)
    else:
        print(f"selected plotting mode is not supported: {args.plot}")


if __name__ == "__main__":
    sys.exit(_main(sys.argv[1:]))
