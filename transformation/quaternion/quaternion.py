from math import sqrt
import numpy as np


def normalize_quaternion(quaternion):
    """The importance of normalization is for the rotation not to include any scaling.
    Normalizing the translation quaternion will result in changin the magnitude of translation"""
    norm = sqrt(sum([q**2 for q in quaternion]))
    if norm == 0:
        return quaternion
    return [q / norm for q in quaternion]


def quat_conjugate(quaternion):
    return [quaternion[0], -quaternion[1], -quaternion[2], -quaternion[3]]


def quat_to_euler(quaternion):
    """Convert a quaternion to Euler angles (roll, pitch, yaw) in degrees.

    Args:
        quaternion (numpy.ndarray): A quaternion in the form [w, x, y, z].

    Returns:
        numpy.ndarray: Euler angles (roll, pitch, yaw) in degrees.
    """
    w, x, y, z = quaternion
    # Roll (x-axis rotation)
    roll = np.arctan2(2 * (w * x + y * z), 1 - 2 * (x**2 + y**2))
    # Pitch (y-axis rotation)
    pitch = np.arcsin(2 * (w * y - z * x))
    # Yaw (z-axis rotation)
    yaw = np.arctan2(2 * (w * z + x * y), 1 - 2 * (y**2 + z**2))
    return np.degrees(roll), np.degrees(pitch), np.degrees(yaw)


def euler_to_quat(euler_angles):
    """Convert Euler angles (roll, pitch, yaw) in degrees to a quaternion.

    Args:
        euler_angles (numpy.ndarray): Euler angles (roll, pitch, yaw) in degrees.

    Returns:
        numpy.ndarray: A quaternion in the form [w, x, y, z].
    """
    roll, pitch, yaw = np.radians(euler_angles)
    cy = np.cos(yaw * 0.5)
    sy = np.sin(yaw * 0.5)
    cp = np.cos(pitch * 0.5)
    sp = np.sin(pitch * 0.5)
    cr = np.cos(roll * 0.5)
    sr = np.sin(roll * 0.5)

    w = cr * cp * cy + sr * sp * sy
    x = sr * cp * cy - cr * sp * sy
    y = cr * sp * cy + sr * cp * sy
    z = cr * cp * sy - sr * sp * cy

    return normalize_quaternion([w, x, y, z])


def quat_to_matrix(quaternion):
    """Convert a quaternion to a 3x3 rotation matrix.

    Args:
        quaternion (numpy.ndarray): A quaternion in the form [w, x, y, z].

    Returns:
        numpy.ndarray: A 3x3 rotation matrix.
    """
    w, x, y, z = quaternion
    rotation_matrix = np.array(
        [
            [1 - 2 * (y**2 + z**2), 2 * (x * y - w * z), 2 * (x * z + w * y)],
            [2 * (x * y + w * z), 1 - 2 * (x**2 + z**2), 2 * (y * z - w * x)],
            [2 * (x * z - w * y), 2 * (y * z + w * x), 1 - 2 * (x**2 + y**2)],
        ]
    )
    return rotation_matrix


def matrix_to_quat(rotation_matrix):
    """Convert a 3x3 rotation matrix to a quaternion.

    Args:
        rotation_matrix (numpy.ndarray): A 3x3 rotation matrix.

    Returns:
        numpy.ndarray: A quaternion in the form [w, x, y, z].
    """
    r11, r12, r13 = rotation_matrix[0]
    r21, r22, r23 = rotation_matrix[1]
    r31, r32, r33 = rotation_matrix[2]

    trace = r11 + r22 + r33

    if trace > 0:
        s = 0.5 / np.sqrt(trace + 1.0)
        w = 0.25 / s
        x = (r32 - r23) * s
        y = (r13 - r31) * s
        z = (r21 - r12) * s
    elif r11 > r22 and r11 > r33:
        s = 2.0 * np.sqrt(1.0 + r11 - r22 - r33)
        w = (r32 - r23) / s
        x = 0.25 * s
        y = (r12 + r21) / s
        z = (r13 + r31) / s
    elif r22 > r33:
        s = 2.0 * np.sqrt(1.0 + r22 - r11 - r33)
        w = (r13 - r31) / s
        x = (r12 + r21) / s
        y = 0.25 * s
        z = (r23 + r32) / s
    else:
        s = 2.0 * np.sqrt(1.0 + r33 - r11 - r22)
        w = (r21 - r12) / s
        x = (r13 + r31) / s
        y = (r23 + r32) / s
        z = 0.25 * s

    return normalize_quaternion([w, x, y, z])


def quat_multiply(quaternion1, quaternion2):
    w1, x1, y1, z1 = quaternion1
    w2, x2, y2, z2 = quaternion2
    result = [
        w1 * w2 - x1 * x2 - y1 * y2 - z1 * z2,
        w1 * x2 + x1 * w2 + y1 * z2 - z1 * y2,
        w1 * y2 - x1 * z2 + y1 * w2 + z1 * x2,
        w1 * z2 + x1 * y2 - y1 * x2 + z1 * w2,
    ]
    return normalize_quaternion(result)


def apply_transform(start_position, start_orientation, translation, rotation_quaternion):
    rotation_quaternion = normalize_quaternion(rotation_quaternion)
    end_orientation_quaternion = quat_multiply(
        rotation_quaternion, quat_multiply(start_orientation, quat_conjugate(rotation_quaternion))
    )
    end_orientation_quaternion = normalize_quaternion(end_orientation_quaternion)
    end_position = [p + t for p, t in zip(start_position, translation)]
    return end_position, end_orientation_quaternion


def translation_as_quaternion(translation_vector):
    return [1.0] + [0.5 * t for t in translation_vector]


def quaternion_to_translation(quaternion):
    return [2 * q for q in quaternion[1:4]]


def slerp(q1, q2, t):
    """Spherical Linear Interpolation

    The most commonly used method for interpolating rotations with quaternions.
    Slerp ensures a smooth and shortest path interpolation between two quaternions on a unit sphere.

    Slerp ensures that the interpolated orientations maintain a constant angular velocity and
    follow the shortest path on the unit quaternion sphere, making it suitable for smooth and
    continuous rotation animations.

    The t parameter in Slerp (Spherical Linear Interpolation) represents the interpolation parameter.
    It is a scalar value that determines how much of the rotation is blended between two quaternions.
    The t parameter typically varies from 0.0 to 1.0, where:
    * t = 0.0 corresponds to the starting quaternion (q1).
    * t = 1.0 corresponds to the ending quaternion (q2).
    * t values between 0.0 and 1.0 represent intermediate rotations along the shortest path between q1 and q2.
    """
    q1 = normalize_quaternion(q1)
    q2 = normalize_quaternion(q2)

    q1 = np.array(q1)
    q2 = np.array(q2)
    dot_product = np.dot(q1, q2)

    # If the dot product is negative, it means the rotations are not in the same direction.
    # negating one of them (while represent the same end orientation) ensures they represent
    # rotations in the same direction.
    if dot_product < 0.0:
        q1[0] = -q1[0]  # Negate only the first element
        dot_product = -dot_product

    if dot_product > 0.995:  # Threshold for linear interpolation
        result = q1 + t * (q2 - q1)
        return normalize_quaternion(result)

    angle = np.arccos(dot_product)
    sin_angle = np.sin(angle)

    weight1 = np.sin((1 - t) * angle) / sin_angle
    weight2 = np.sin(t * angle) / sin_angle

    result = q1 * weight1 + q2 * weight2
    return normalize_quaternion(result)


def interpolate_orientation_slerp(q1, q2, steps):
    """Return a list of orientations from q1 to q2 (inclusive) with interpolated steps in between

    steps: the number of intermediate steps.
    The number of returned orientation, including start and end, is steps + 2
    """
    orientations = [q1]
    for i in range(1, steps + 1):
        step = i / (steps + 1.0)
        intermediate_orientation = slerp(q1, q2, step)
        orientations.append(intermediate_orientation)
    orientations.append(q2)
    return orientations


def interpolate_position_linear(p1, p2, steps):
    """Return a list of positions from p1 to p2 (inclusive) with interpolated steps in between

    steps: the number of intermediate steps.
    The number of returned positions, including start and end, is steps + 2
    """
    translation = [p2_ - p1_ for p1_, p2_ in zip(p1, p2)]
    positions = [p1]
    for i in range(1, steps + 1):
        step = i / (steps + 1.0)
        intermediate_position = [p + step * t for p, t in zip(p1, translation)]
        positions.append(intermediate_position)
    positions.append(p2)
    return positions


# ----------------------------------------------------------------------------------
# ------------------------------------------------------------------ Dual Quaternion
# ----------------------------------------------------------------------------------
def normalize_dual_quaternion(dq):
    """Only normalize the rotation part"""
    Dq, Tq = dq
    return [normalize_quaternion(Dq), Tq]


def compose_dual_quaternion(translation_vector=None, rotation_quaternion=None):
    """Return dual quaternion from rotation quaternion and translation vector"""
    if translation_vector is None:
        tran_q = [0.0, 0.0, 0.0, 0.0]
    else:
        tran_q = [0.0] + translation_as_quaternion(translation_vector)[1:4]

    if rotation_quaternion is None:
        rot_q = [1.0, 0.0, 0.0, 0.0]
    else:
        rot_q = rotation_quaternion

    return [rot_q, tran_q]


def decompose_dual_quaternion_to_pose(dual_quaternion):
    """This function litterally does nothing!"""
    Dq = dual_quaternion[0]  # position: real part
    Tq = dual_quaternion[1]  # orientation: dual part
    position = quaternion_to_translation(Dq)
    return position, Tq


def dual_quaternion_multiply(dq1, dq2):
    Dq1, Tq1 = dq1
    Dq2, Tq2 = dq2
    Dq = [
        Dq1[0] * Dq2[0] - Dq1[1] * Dq2[1] - Dq1[2] * Dq2[2] - Dq1[3] * Dq2[3],
        Dq1[0] * Dq2[1] + Dq1[1] * Dq2[0] + Dq1[2] * Dq2[3] - Dq1[3] * Dq2[2],
        Dq1[0] * Dq2[2] - Dq1[1] * Dq2[3] + Dq1[2] * Dq2[0] + Dq1[3] * Dq2[1],
        Dq1[0] * Dq2[3] + Dq1[1] * Dq2[2] - Dq1[2] * Dq2[1] + Dq1[3] * Dq2[0],
    ]
    Tq = [
        Dq1[0] * Tq2[0]
        + Dq2[0] * Tq1[0]
        - Dq1[1] * Tq2[1]
        - Dq2[1] * Tq1[1]
        - Dq1[2] * Tq2[2]
        - Dq2[2] * Tq1[2]
        - Dq1[3] * Tq2[3]
        - Dq2[3] * Tq1[3],
        Dq1[0] * Tq2[1]
        + Dq2[0] * Tq1[1]
        + Dq1[1] * Tq2[0]
        + Dq2[1] * Tq1[0]
        + Dq1[2] * Tq2[3]
        + Dq2[2] * Tq1[3]
        - Dq1[3] * Tq2[2]
        - Dq2[3] * Tq1[2],
        Dq1[0] * Tq2[2]
        + Dq2[0] * Tq1[2]
        - Dq1[1] * Tq2[3]
        - Dq2[1] * Tq1[3]
        + Dq1[2] * Tq2[0]
        + Dq2[2] * Tq1[0]
        + Dq1[3] * Tq2[1]
        + Dq2[3] * Tq1[1],
        Dq1[0] * Tq2[3]
        + Dq2[0] * Tq1[3]
        + Dq1[1] * Tq2[2]
        + Dq2[1] * Tq1[2]
        - Dq1[2] * Tq2[1]
        - Dq2[2] * Tq1[1]
        + Dq1[3] * Tq2[0]
        + Dq2[3] * Tq1[0],
    ]
    return [normalize_quaternion(Dq), Tq]


def dual_quaternion_interpolation(dq1, dq2, t):
    """Return an interpolation between two dual quaternion

    Decomposes the dual quaternion to rotation and translation and interpolate separately"""
    Dq1, Tq1 = dq1
    Dq2, Tq2 = dq2
    result_Dq = slerp(Dq1, Dq2, t)
    result_Tq = (1 - t) * Tq1 + t * Tq2
    return [result_Dq, result_Tq]  # orientation, position


def decompose_dual_quaternion(dq):
    """Return screw parameters resulting from the decomposition of the input dual quaternion"""
    Dq, Tq = dq  # Dq: rotation, Tq: translation
    norm_Dq = np.linalg.norm(Dq)
    screw_axis = Dq[1:] / norm_Dq
    screw_angle = 2 * np.arctan2(norm_Dq, Dq[0])
    return screw_axis, screw_angle, Tq


def interpolate_screw_parameters(screw_params1, screw_params2, t):
    """Return an interpolation between input screw parameters"""
    interpolated_screw_axis = (1 - t) * screw_params1[0] + t * screw_params2[0]
    interpolated_screw_angle = (1 - t) * screw_params1[1] + t * screw_params2[1]
    interpolated_translation = (1 - t) * screw_params1[2] + t * screw_params2[2]
    return interpolated_screw_axis, interpolated_screw_angle, interpolated_translation


def reconstruct_dual_quaternion(screw_axis, screw_angle, translation):
    """Retunr a dual quaternion reconstructed from the input screw paramters"""
    half_screw_angle = 0.5 * screw_angle
    Dq = [np.cos(half_screw_angle)] + list(np.sin(half_screw_angle) * screw_axis)
    Tq = 0.5 * np.quaternion(0.0, *translation) * Dq
    return [Dq, Tq]


def sclerp(dq1, dq2, t):
    """Return an interpolation between two dual quaternion using Screw LERP"""
    screw_params1 = decompose_dual_quaternion(dq1)
    screw_params2 = decompose_dual_quaternion(dq2)
    interpolated_screw_params = interpolate_screw_parameters(screw_params1, screw_params2, t)
    interpolated_dual_quaternion = reconstruct_dual_quaternion(*interpolated_screw_params)
    return interpolated_dual_quaternion
