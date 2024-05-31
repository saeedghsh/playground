# pylint: disable=missing-module-docstring
import mayavi.mlab  # pylint: disable=import-error


class Visualizer:
    # pylint: disable=missing-class-docstring
    # pylint: disable=missing-function-docstring
    def __init__(self, title: str = "Figure"):
        self._figure = mayavi.mlab.figure(figure=title, size=(1080, 1080))

    def orientation_axes(self):
        """display axis indicator"""
        mayavi.mlab.orientation_axes(figure=self._figure)

    def close(self):
        mayavi.mlab.close()

    @property
    def figure(self):
        return self._figure
