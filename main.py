#!/usr/bin/env python
""" Generation of chaotic processes via logistic map"""

from __future__ import print_function

import argparse

from chaos.logisticmap import LogisticMap
from chaos.plotting import SlidingFigure


def main_logisticmap(args: argparse.Namespace):
    """instantiating the LogisticMap and the plotting object

    Parameters
    ----------
    args.length : int
        The length of each processes
    args.count : int
        The numebr of processes
    """

    LM = LogisticMap(r=0.0, length=args.length, count=args.count)
    _ = SlidingFigure(LM)


if __name__ == "__main__":
    PARSER = argparse.ArgumentParser(
        description="number and temopral length of processes",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    SUBPARSERS = PARSER.add_subparsers()

    LOGISTICMAP_PARSER = SUBPARSERS.add_parser("logisticmap")
    LOGISTICMAP_PARSER.set_defaults(func=main_logisticmap)
    LOGISTICMAP_PARSER.add_argument(
        "--count",
        dest="count",
        type=int,  # nargs=1,
        action="store",
        default=100,
        help="number of the chaotic processes",
    )
    LOGISTICMAP_PARSER.add_argument(
        "--length",
        dest="length",
        type=int,  # nargs=1,
        action="store",
        default=60,
        help="[temporal] length of the chaotic processes",
    )

    ARGS = PARSER.parse_args()
    ARGS.func(ARGS)
