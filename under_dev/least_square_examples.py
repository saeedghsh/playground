# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=unbalanced-tuple-unpacking
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


def linear():
    x = np.array([1, 2, 3, 4, 5])
    y = np.array([2, 3, 5, 7, 11])
    coefficients = np.polyfit(x, y, 1)  # 1 for linear
    slope, intercept = coefficients
    y_fit = slope * x + intercept
    # print(f"Coefficients: {coefficients}")
    return x, y, y_fit, "linear"


def polynomial():
    x = np.array([0, 1, 2, 3, 4, 5])
    y = np.array([1, 3, 7, 13, 21, 31])
    coefficients = np.polyfit(x, y, 2)
    y_fit = np.polyval(coefficients, x)
    # print(f"Coefficients: {coefficients}")
    return x, y, y_fit, "polynomial"


def exponential():
    """
    The exponential model has the form:
    y = a * e ** (b*x)

    To linearize this, we can take the natural logarithm of both sides:
    ln(y) = ln(a)+ b * x
    """
    x = np.array([1, 2, 3, 4, 5])
    y = np.array([2.7, 7.4, 20.1, 54.6, 148.4])
    log_y = np.log(y)
    coefficients = np.polyfit(x, log_y, 1)
    b, log_a = coefficients
    a = np.exp(log_a)
    y_fit = a * np.exp(b * x)
    # print(f"a: {a}, b: {b}")
    return x, y, y_fit, "exponential"


def logarithmic():
    """
    y = a * ln(x) + b
    """
    x = np.array([1, 2, 3, 4, 5])
    y = np.array([0.5, 1.7, 2.6, 3.5, 4.2])
    log_x = np.log(x)
    coefficients = np.polyfit(log_x, y, 1)
    a, b = coefficients
    y_fit = a * log_x + b
    # print(f"a: {a}, b: {b}")
    return x, y, y_fit, "logarithmic"


def power_law():
    """
    y = a * x ** b
    """
    x = np.array([1, 2, 3, 4, 5])
    y = np.array([2.3, 4.1, 7.6, 12.4, 19.5])
    log_x = np.log(x)
    log_y = np.log(y)
    coefficients = np.polyfit(log_x, log_y, 1)
    b, log_a = coefficients
    a = np.exp(log_a)
    y_fit = a * x**b
    # print(f"a: {a}, b: {b}")
    return x, y, y_fit, "power_law"


def rational():
    x = np.array([1, 2, 3, 4, 5])
    y = np.array([1.8, 1.3, 1.0, 0.8, 0.7])

    def rational_func(x, a0, a1, b0, b1):
        return (a0 + a1 * x) / (b0 + b1 * x)

    params, _ = curve_fit(rational_func, x, y, p0=[1, 1, 1, 1])
    a0, a1, b0, b1 = params
    y_fit = rational_func(x, a0, a1, b0, b1)
    # print(f"a0: {a0}, a1: {a1}, b0: {b0}, b1: {b1}")
    return x, y, y_fit, "rational"


def sinusoidal():
    x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    y = np.array([0, 0.84, 0.91, 0.14, -0.76, -0.99, -0.28, 0.66, 0.98, 0.41, -0.54])

    def sinusoidal_func(x, a, b, c, d):
        return a * np.sin(b * x + c) + d

    params, _ = curve_fit(sinusoidal_func, x, y, p0=[1, 1, 0, 0])
    a, b, c, d = params
    y_fit = sinusoidal_func(x, a, b, c, d)
    # print(f"a: {a}, b: {b}, c: {c}, d: {d}")
    return x, y, y_fit, "sinusoidal"


def custom_non_linear():
    x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    y = np.array([1, 0.8, 0.3, 0.4, 0.8, 1.5, 2.3, 3.5, 4.8, 6.4, 8.1])

    def custom_func(x, a, b, c):
        return a * np.exp(-b * x) + c * x**2

    params, _ = curve_fit(custom_func, x, y, p0=[1, 1, 1])
    a, b, c = params
    y_fit = custom_func(x, a, b, c)
    # print(f"a: {a}, b: {b}, c: {c}")
    return x, y, y_fit, "custom_non_linear"


def plot(axis, x, y, y_fit, model_name: str):
    axis.scatter(x, y, label="Data Points")
    axis.plot(x, y_fit, label=model_name, color="red")
    axis.set_xlabel("x")
    axis.set_ylabel("y")
    axis.legend()


def main():
    _, axes = plt.subplots(2, 4, figsize=(24, 12))
    axes = axes.flatten()
    models = [
        polynomial,
        linear,
        exponential,
        logarithmic,
        power_law,
        rational,
        sinusoidal,
        custom_non_linear,
    ]
    for axis, model in zip(axes, models):
        x, y, y_fit, model_name = model()
        plot(axis, x, y, y_fit, model_name)
    plt.tight_layout()
    plt.show()


main()
