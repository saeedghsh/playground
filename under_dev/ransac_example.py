# pylint: disable=missing-module-docstring
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import RANSACRegressor, LinearRegression


def _generate_synthetic_data(n_inliers: int = 100, n_outliers: int = 20):
    np.random.seed(42)
    x_inliers = np.linspace(0, 10, n_inliers).reshape(-1, 1)
    y_inliers = 2 * x_inliers.squeeze() + 1 + np.random.normal(size=n_inliers)
    x_outliers = np.random.uniform(0, 10, size=(n_outliers, 1))
    y_outliers = np.random.uniform(-20, 20, size=n_outliers)
    x = np.vstack((x_inliers, x_outliers))
    y = np.concatenate((y_inliers, y_outliers))
    return x, y


def _plot(x, y, inlier_mask, outlier_mask, line_x, line_y_ransac):
    plt.figure(figsize=(10, 6))
    plt.scatter(x[inlier_mask], y[inlier_mask], color="yellowgreen", marker=".", label="Inliers")
    plt.scatter(x[outlier_mask], y[outlier_mask], color="gold", marker="x", label="Outliers")
    plt.plot(line_x, line_y_ransac, color="cornflowerblue", linewidth=2, label="RANSAC regressor")
    plt.legend(loc="lower right")
    plt.xlabel("Input")
    plt.ylabel("Response")
    plt.title("RANSAC Regression Example")
    plt.show()


x, y = _generate_synthetic_data()

# Step 2: Apply RANSAC
ransac = RANSACRegressor(
    estimator=LinearRegression(), min_samples=0.5, residual_threshold=5, random_state=42
)
ransac.fit(x, y)
inlier_mask = ransac.inlier_mask_
outlier_mask = np.logical_not(inlier_mask)


line_x = np.arange(x.min(), x.max())[:, np.newaxis]
line_y_ransac = ransac.predict(line_x)
_plot(x, y, inlier_mask, outlier_mask, line_x, line_y_ransac)
