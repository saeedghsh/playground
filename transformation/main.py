#!/usr/bin/env python
"""A playground for conversion and visulization of transformations"""

from __future__ import print_function

import argparse

from visualization.coordinate_frame import CoordinateFrame
from visualization.visulizer import Visualizer


def argument_parser():
    parser = argparse.ArgumentParser(
        description="Transformation Playground",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = argument_parser()

    # instantiate a figure of mayavi
    vis = Visualizer("example")

    # draw reference frame (default pose is identity)
    reference_frame = CoordinateFrame(name="ref_frame", color_map="white")
    reference_frame.draw(figure=vis.figure)

    # display axis indicator
    vis.orientation_axes()

    # close mayavi window
    # vis.deinit()
