#!/usr/bin/env python
"""Main script to launch examples from."""

from __future__ import print_function

import argparse

from chaos.logisticmap import LogisticMap
from chaos.plotting import LogisticMapFigure


def main_logisticmap(args: argparse.Namespace) -> None:
    """instantiating the LogisticMap and the plotting object

    Parameters
    ----------
    args.length : int
        The length of each processes
    args.count : int
        The numebr of processes
    """

    logisticmap = LogisticMap(r=0.0, length=args.length, count=args.count)
    _ = LogisticMapFigure(logisticmap)


def parse_argument() -> argparse.Namespace:
    """Main Parser"""
    parser = argparse.ArgumentParser(
        description="Main Parser",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    subparsers = parser.add_subparsers()

    logisticmap_parser = subparsers.add_parser("logisticmap")
    logisticmap_parser.set_defaults(func=main_logisticmap)
    logisticmap_parser.add_argument(
        "--count",
        dest="count",
        type=int,  # nargs=1,
        action="store",
        default=100,
        help="number of the chaotic processes",
    )
    logisticmap_parser.add_argument(
        "--length",
        dest="length",
        type=int,  # nargs=1,
        action="store",
        default=60,
        help="[temporal] length of the chaotic processes",
    )

    arguments = parser.parse_args()
    return arguments


def main() -> None:
    arguments = parse_argument()
    arguments.func(arguments)


if __name__ == "__main__":
    main()
