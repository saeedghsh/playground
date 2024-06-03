"""Lorenz Attractor"""

import argparse
import sys
from typing import Sequence

from libs.lorenz.lorenz import LorenzParameters, LorenzSystem, TimeLine
from libs.lorenz.plotting import plot_lorenz_attractor


def _parse_arguments(argv: Sequence[str]) -> argparse.Namespace:  # pragma: no cover
    parser = argparse.ArgumentParser(description="Lorenz Attractor")
    parser.add_argument("-s", "--time-start", type=int, default=0)
    parser.add_argument("-e", "--time-end", type=int, default=100)
    parser.add_argument("-c", "--time-points-count", type=int, default=10000)
    parser.add_argument("-i", "--initial-points", type=float, nargs="+", default=[0.1, 0.0, 0.0])
    parser.add_argument("--sigma", type=float, default=10.0)
    parser.add_argument("--rho", type=float, default=28.0)
    parser.add_argument("--beta", type=float, default=8.0 / 3.0)
    return parser.parse_args(argv)


def _main(argv: Sequence[str]):  # pragma: no cover
    args = _parse_arguments(argv)
    lorenz = LorenzSystem(
        time_line=TimeLine(args.time_start, args.time_end, args.time_points_count),
        parameters=LorenzParameters(args.sigma, args.rho, args.beta),
        initial_points=args.initial_points,
    )
    solution_points = lorenz.solve()
    plot_lorenz_attractor(solution_points)


if __name__ == "__main__":
    sys.exit(_main(sys.argv[1:]))
