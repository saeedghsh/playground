#!/usr/bin/env python
"""
Generation of chaotic processes (e.g. population growth) via logistic map
"""

from __future__ import print_function
import argparse

import chaos.logisticmap
import chaos.plotting

if __name__ == "__main__":
    PARSER = argparse.ArgumentParser(description='number and temopral length of processes')
    PARSER.add_argument('--count', dest='count', type=int,# nargs=1,
                        action='store', default=1000,
                        help='Number of [chaotic] processes')
    PARSER.add_argument('--length', dest='length', type=int, #nargs=1,
                        action='store', default=50,
                        help='length (time) of [chaotic] processes')
    ARGS = PARSER.parse_args()

    LM = chaos.logisticmap.LogisticMap(r=0.0, length=ARGS.length, count=ARGS.count)
    SF = chaos.plotting.SlidingFigure(LM)


