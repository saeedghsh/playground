#!/usr/bin/env python
""" Generation of chaotic processes via logistic map"""

from __future__ import print_function

import argparse

from chaos.logisticmap import LogisticMap
from chaos.plotting import SlidingFigure


def main(length: int, count: int):
    """instantiating the LogisticMap and the plotting object

    Parameters
    ----------
    length : int
        The length of each processes
    count : int
        The numebr of processes
    """

    LM = LogisticMap(r=0.0, length=length, count=count)
    _ = SlidingFigure(LM)


if __name__ == "__main__":
    PARSER = argparse.ArgumentParser(
        description="number and temopral length of processes",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    PARSER.add_argument(
        "--count",
        dest="count",
        type=int,  # nargs=1,
        action="store",
        default=100,
        help="number of the chaotic processes",
    )
    PARSER.add_argument(
        "--length",
        dest="length",
        type=int,  # nargs=1,
        action="store",
        default=60,
        help="[temporal] length of the chaotic processes",
    )
    ARGS = PARSER.parse_args()

    main(ARGS.length, ARGS.count)
