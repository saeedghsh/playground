""""""

import matplotlib.pyplot as plt
import numpy as np


def line_intersection(line1, line2):
    x1, y1 = line1[0]
    x2, y2 = line1[1]
    x3, y3 = line2[0]
    x4, y4 = line2[1]

    # Calculate slopes
    m1 = (y2 - y1) / (x2 - x1) if x2 != x1 else np.inf
    m2 = (y4 - y3) / (x4 - x3) if x4 != x3 else np.inf

    # Check for parallel lines
    if m1 == m2:
        return None  # Parallel lines, no intersection

    # Calculate intersection point
    if m1 == np.inf:
        x_intersect = x1
        y_intersect = m2 * (x1 - x3) + y3
    elif m2 == np.inf:
        x_intersect = x3
        y_intersect = m1 * (x3 - x1) + y1
    else:
        x_intersect = (y3 - y1 + m1 * x1 - m2 * x3) / (m1 - m2)
        y_intersect = m1 * (x_intersect - x1) + y1

    return np.array([x_intersect, y_intersect])


def cross_ratio(points: np.ndarray) -> float:
    a, b, c, d = points
    return np.dot(c - a, b - d) / np.dot(c - b, d - a)


def draw_point_text(axis, point, text, color):
    axis.scatter(point[0], point[1], color=color, label=text)
    axis.text(point[0] + 0.1, point[1] + 0.1, text, fontsize=12, color=color)


def draw_line_text(axis, line, text, color, linestyle="-", text_place="first"):
    axis.plot(line[:, 0], line[:, 1], color=color, linestyle=linestyle, label=text)
    if text_place == "first":
        x, y = line[0, :]
    elif text_place == "second":
        x, y = line[1, :]
    else:
        return
    axis.text(x + 0.1, y + 0.1, text, fontsize=12, color=color)


if __name__ == "__main__":
    print("hello")


##### construction
l = np.array([5, 10])
p = np.array([2, 0])
q = np.array([4, 0])
r = np.array([6, 0])
s = np.array([8, 0])

line_1 = np.array([[0, 5], [10, 5]])
line_2 = np.array([[0, 2], [10, 4]])
line_lp = np.array([l, p])
line_lq = np.array([l, q])
line_lr = np.array([l, r])
line_ls = np.array([l, s])

a1 = line_intersection(line_1, line_lp)
b1 = line_intersection(line_1, line_lq)
c1 = line_intersection(line_1, line_lr)
d1 = line_intersection(line_1, line_ls)

a2 = line_intersection(line_2, line_lp)
b2 = line_intersection(line_2, line_lq)
c2 = line_intersection(line_2, line_lr)
d2 = line_intersection(line_2, line_ls)


##### computations
print(cross_ratio(np.array([a1, b1, c1, d1])))
print(cross_ratio(np.array([a2, b2, c2, d2])))


##### visualization
fig, axis = plt.subplots(figsize=(18, 12))

draw_line_text(axis, line_1, text="line 1", color="black", linestyle="-")
draw_line_text(axis, line_2, text="line 2", color="black", linestyle="-")

draw_line_text(axis, line_lp, text="line_lp", color="blue", linestyle="--", text_place=None)
draw_line_text(axis, line_lq, text="line_lq", color="blue", linestyle="--", text_place=None)
draw_line_text(axis, line_lr, text="line_lr", color="blue", linestyle="--", text_place=None)
draw_line_text(axis, line_ls, text="line_ls", color="blue", linestyle="--", text_place=None)


draw_point_text(axis, l, "l", "blue")
draw_point_text(axis, p, "p", "blue")
draw_point_text(axis, q, "q", "blue")
draw_point_text(axis, r, "r", "blue")
draw_point_text(axis, s, "s", "blue")

draw_point_text(axis, a1, "a1", "red")
draw_point_text(axis, b1, "b1", "red")
draw_point_text(axis, c1, "c1", "red")
draw_point_text(axis, d1, "d1", "red")
draw_point_text(axis, a2, "a2", "red")
draw_point_text(axis, b2, "b2", "red")
draw_point_text(axis, c2, "c2", "red")
draw_point_text(axis, d2, "d2", "red")


axis.axis("equal")
plt.show()
