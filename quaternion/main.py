from quaternion import (
    apply_transform,
    normalize_quaternion,
    euler_to_quat,
    interpolate_position_linear,
    interpolate_orientation_slerp,
    compose_dual_quaternion,
    decompose_dual_quaternion_to_pose,
    dual_quaternion_multiply,
    dual_quaternion_interpolation,
)
from visualization import draw_poses


def print_pose(poses):
    for title, (position, orientation) in poses:
        print(f"\n{title}")
        print(f"\tPosition (or translation): {position}")
        print(f"\tOrientation (Quaternion): {orientation}")

# TODO: write unit test

# Issue/bug:
# * when: start_orientation = euler_to_quat([0, 0, 0])
# * then: the rotation of it will not take effect, i.e. the end pose will have the same orienation
# * then: also the plotting failes to plot it! is it a but in quiver?

# Issue/bug:
# * when: rotation_quaternion = euler_to_quat([0, 90, 180])
# * then: the interpolation is not smooth! there is a jump in the middle

# Issue/bug:
# * The whole dual quaternion stuff doesn't seem to work.

start_position = [1.0, 1.0, 1.0]
start_orientation = euler_to_quat([1, 0, 0])
start_pose = [start_position, start_orientation]

translation_vector = [1, 1, 1]
rotation_quaternion = euler_to_quat([45, 45, 90])

mode = ["quaternion", "dual_quaternion"][0]
interpolate = False
interpolate_steps = 10

if mode == "quaternion":
    end_position, end_orientation = apply_transform(
        start_position, start_orientation, translation_vector, rotation_quaternion
    )
    end_pose = [end_position, end_orientation]
    poses = [start_pose, end_pose]

    if interpolate:
        orientations = interpolate_orientation_slerp(start_orientation, end_orientation, interpolate_steps)
        positions = interpolate_position_linear(start_position, end_position, interpolate_steps)
        poses = [[p, o] for p, o in zip(positions, orientations)]


if mode == "dual_quaternion":
    start_pose_dq = compose_dual_quaternion(*start_pose)
    transformation_dq = compose_dual_quaternion(translation_vector, rotation_quaternion)
    end_pose_dq = dual_quaternion_multiply(transformation_dq, start_pose_dq)
    end_pose_ = decompose_dual_quaternion_to_pose(end_pose_dq)
    poses = [start_pose, end_pose_]
    if interpolate:
        poses = []
        for i in range(1, interpolate_steps+1):
            step = i / (interpolate_steps+1.0)
            orientation, position = dual_quaternion_interpolation(start_pose_dq, end_pose_dq, interpolate_steps)
            poses.append([position, orientation])


# starts from blue, and moves to red
draw_poses(poses)
