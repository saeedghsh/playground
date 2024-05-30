#!/usr/bin/env python
"""Main script to launch examples from."""

import sys
import argparse
from typing import Sequence
from chaos.logisticmap import LogisticMap
from chaos.plotting import LogisticMapFigure


def _main_logisticmap(args: argparse.Namespace) -> None:
    logisticmap = LogisticMap(r=0.0, length=args.length, count=args.count)
    _ = LogisticMapFigure(logisticmap)


def _parse_arguments(argv: Sequence[str]) -> argparse.Namespace:  # pragma: no cover
    parser = argparse.ArgumentParser(
        description="Main Parser",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    subparsers = parser.add_subparsers()
    logisticmap_parser = subparsers.add_parser("logisticmap")
    logisticmap_parser.set_defaults(func=_main_logisticmap)
    logisticmap_parser.add_argument(
        "-c", "--count", type=int, default=100, help="number of the processes"
    )
    logisticmap_parser.add_argument(
        "-l", "--length", type=int, default=60, help="length of the processes"
    )
    return parser.parse_args(argv)


def _main(argv: Sequence[str]):
    args = _parse_arguments(argv)
    args.func(args)


if __name__ == "__main__":
    sys.exit(_main(sys.argv[1:]))
