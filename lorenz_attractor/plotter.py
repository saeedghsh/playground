# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


def plot_lorenz_attractor(solution_points: np.ndarray):
    fig = plt.figure()
    ax: Axes3D = fig.add_subplot(111, projection="3d")
    ax.plot(solution_points[0], solution_points[1], solution_points[2])
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.set_title("Lorenz Attractor")
    plt.show()
