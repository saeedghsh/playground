#!/usr/bin/env python
"""Simple Random Walk"""

import argparse
import sys
from typing import Sequence

from libs.stochastic_processes.plotting import SlidingFigure
from libs.stochastic_processes.random_walk import SimpleRandomWalk


def _parse_arguments(argv: Sequence[str]) -> argparse.Namespace:  # pragma: no cover
    parser = argparse.ArgumentParser(description="Random Walk")
    parser.add_argument("-c", "--count", type=int, default=3, help="Number processes")
    parser.add_argument("-l", "--length", type=int, default=100, help="length (time) of processes")
    return parser.parse_args(argv)


def _main(argv: Sequence[str]):
    args = _parse_arguments(argv)
    random_walks = [SimpleRandomWalk(args.length) for _ in range(args.count)]
    _ = SlidingFigure(random_walks)


if __name__ == "__main__":
    sys.exit(_main(sys.argv[1:]))
