import matplotlib.pyplot as plt
import numpy as np


def _draw_basis(ax):
    x = [1, 0, 0]
    y = [0, 1, 0]
    z = [0, 0, 1]
    ax.quiver(0, 0, 0, x[0], x[1], x[2], color='r', label='X-Basis')
    ax.quiver(0, 0, 0, y[0], y[1], y[2], color='g', label='Y-Basis')
    ax.quiver(0, 0, 0, z[0], z[1], z[2], color='b', label='Z-Basis')


def _draw_pose_vector(ax, clr, position, orientation_quaternion):
    ax.quiver(position[0], position[1], position[2],
              orientation_quaternion[1], orientation_quaternion[2], orientation_quaternion[3],
              color=plt.cm.coolwarm(clr), label='Start Pose', length=1.0, normalize=True)


def draw_poses(poses):
    fig = plt.figure(figsize=(12, 12))
    ax = fig.add_subplot(111, projection='3d')
    _draw_basis(ax)

    colors = np.linspace(0.1, 1, len(poses))
    for idx, (position, orientation_quaternion) in enumerate(poses):
        print(f"drawing pose {idx}: position={position}\torientation{orientation_quaternion}")
        _draw_pose_vector(ax, colors[idx], position, orientation_quaternion)

    ax.set_xlim([-5, 5])
    ax.set_ylim([-5, 5])
    ax.set_zlim([-5, 5])
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.show()