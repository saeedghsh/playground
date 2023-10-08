#!/usr/bin/env python
"""
Simple Random Walk - main script
"""

from __future__ import print_function
import argparse

from SimpleRandomWalk.SimpleRandomWalk import SimpleRandomWalk
from SimpleRandomWalk.plotting import SlidingFigure

if __name__ == "__main__":
    PARSER = argparse.ArgumentParser(
        description='number and temopral length of processes')
    PARSER.add_argument('--count', dest='count', type=int,  # nargs=1,
                        action='store', default=3,
                        help='Number of stochastic processes')
    PARSER.add_argument('--length', dest='length', type=int,  # nargs=1,
                        action='store', default=100,
                        help='length (time) of stochastic processes')
    ARGS = PARSER.parse_args()

    RANDOM_WALKS = [SimpleRandomWalk(ARGS.length) for _ in range(ARGS.count)]
    FIGURE = SlidingFigure(RANDOM_WALKS)
