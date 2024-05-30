#!/usr/bin/env python
from __future__ import print_function
import mayavi.mlab


class Visualizer:
    def __init__(self, title: str = "Figure"):
        self._figure = mayavi.mlab.figure(figure=title, size=(1080, 1080))

    def orientation_axes(self):
        """display axis indicator"""
        mayavi.mlab.orientation_axes(figure=self._figure)

    def deinit(self):
        mayavi.mlab.close()

    @property
    def figure(self):
        return self._figure
