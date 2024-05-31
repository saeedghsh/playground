#!/usr/bin/env python
"""A playground for conversion and visualization of transformations"""

import argparse
import sys
from typing import Sequence

from visualization.coordinate_frame import CoordinateFrame
from visualization.visualizer import Visualizer


def _parse_arguments(argv: Sequence[str]) -> argparse.Namespace:  # pragma: no cover
    parser = argparse.ArgumentParser(
        description="Transformation Playground",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    return parser.parse_args(argv)


def _main(argv: Sequence[str]):
    _ = _parse_arguments(argv)
    vis = Visualizer("example")
    reference_frame = CoordinateFrame(name="ref_frame", color_map="white")
    reference_frame.draw(figure=vis.figure)
    vis.orientation_axes()
    # vis.close()


if __name__ == "__main__":
    sys.exit(_main(sys.argv[1:]))
