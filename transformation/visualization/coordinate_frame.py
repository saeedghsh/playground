# pylint: disable=missing-module-docstring
from typing import Tuple

import mayavi.mlab  # pylint: disable=import-error
import mayavi.modules  # pylint: disable=import-error
import numpy


class CoordinateFrame:
    # pylint: disable=missing-class-docstring
    def __init__(
        self,
        pose: numpy.ndarray = numpy.eye(4),
        name: str = "coordinate_frame",
        color_map: str = "rgb",
    ):
        self._pose = pose
        self._name = name
        self._colors = self._scalar_colors(color_map)
        self._origin, self._axes = self._coordinate_frame_from_pose(pose)
        self._coordinate_frame: mayavi.modules.vectors.Vectors

    def __repr__(self):
        s = "Coordinate frame with pose:\n{s}"
        return s.format(numpy.array2string(self._pose))

    @staticmethod
    def _scalar_colors(color_map: str):
        """three sets of colors (rgba channels) for the three axes"""
        if color_map == "rgb":
            colors = numpy.array(
                [
                    [255, 0, 0, 255],
                    [0, 255, 0, 255],
                    [0, 0, 255, 255],
                ]
            ).astype(numpy.uint8)
        elif color_map == "white":
            colors = (numpy.ones((3, 4)) * 255).astype(numpy.uint8)
        else:
            print("Warning: color_map is not recognizable, setting to white")
            colors = (numpy.ones((3, 4)) * 255).astype(numpy.uint8)

        return colors

    @staticmethod
    def _coordinate_frame_from_pose(
        pose: numpy.ndarray,
    ) -> Tuple[numpy.ndarray, numpy.ndarray]:
        """represent a given 6D pose as a coordinate frame

        * pose is represented as a 4x4 transformation matrix
        * coordinate frame is composed of origin point and basis axes
          - origin: (3, 3) array, representing the xyz coordinates of the
            origin point, tiled in three rows to match the shape of axes
          - axes: (3, 3) array, each row representing the basis axes x-y-z
            axes = [x_axis, y_axis, z_axis]
            where each axis is:
            axis = [x_coordinate, y_coordinate, z_coordinate]
        """
        origin = pose[0:3, 3]
        rotate = pose[:3, :3]
        axes = numpy.array(
            [
                numpy.dot(rotate, numpy.array([1, 0, 0])),
                numpy.dot(rotate, numpy.array([0, 1, 0])),
                numpy.dot(rotate, numpy.array([0, 0, 1])),
            ]
        )
        origin = numpy.tile(origin, (3, 1))
        return origin, axes

    def draw(self, figure: mayavi.core.scene.Scene):
        """Draw a coordinate frame (XYZ axes) in the figure

        draws the basis of a coordinate frame (x, y, and z axes)

        * figure: an instance of mayavi.mlab.figure to draw on
        * self._coordinate_frame: a single instance of mayavi.mlab.quiver3d,
          with three traits for x, y and z
        """
        args = {
            "line_width": 3,
            "scale_factor": 1,
            "figure": figure,
            "name": self._name,
        }
        self._coordinate_frame = mayavi.mlab.quiver3d(
            *(self._origin.T),
            *(self._axes.T),
            scalars=[0, 1, 2],
            **args,
        )
        self._coordinate_frame.glyph.color_mode = "color_by_scalar"
        self._coordinate_frame.module_manager.scalar_lut_manager.lut.table = self._colors

    def update(self, pose: numpy.ndarray):
        """Update a previously drawn coordinate frame

        for coordinate_frame see self.draw.__doc__
        for pose see self.coordinate_frame_from_pose.__doc__
        """
        self._pose = pose
        self._origin, self._axes = self._coordinate_frame_from_pose(pose)
        x, y, z = self._origin[:, 0], self._origin[:, 1], self._origin[:, 2]
        u, v, w = self._axes[:, 0], self._axes[:, 1], self._axes[:, 2]
        self._coordinate_frame.mlab_source.trait_set(x, y, z, u, v, w)
