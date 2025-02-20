# # pylint: disable=missing-module-docstring
# # pylint: disable=missing-class-docstring
# # pylint: disable=missing-function-docstring
# from types import SimpleNamespace
# from typing import Callable, List
# import numpy as np
# import matplotlib.pyplot as plt
# from scipy.optimize import minimize
# from scipy.special import gammaln
# from sklearn.datasets import make_classification


# def solve_mle(nll: Callable, data: np.ndarray, initial_params: list, bounds: List[tuple]):
#     result = minimize(
#         nll,
#         initial_params,
#         args=(data,),
#         method="L-BFGS-B",
#         bounds=bounds,
#     )
#     mle_params = result.x
#     return mle_params


# def generate_distribution_data(distribution: str, params: SimpleNamespace) -> np.ndarray:
#     np.random.seed(0)
#     size = 1000
#     if distribution == "normal":
#         mean, sigma = params.mean, params.sigma
#         data = np.random.normal(loc=mean, scale=sigma, size=size)
#     elif distribution == "exponential":
#         lambda_ = params.lambda_
#         data = np.random.exponential(scale=1 / lambda_, size=size)
#     elif distribution == "poisson":
#         lambda_ = params.lambda_
#         data = np.random.poisson(lam=lambda_, size=size)
#     else:
#         raise ValueError(f"Unsupported distribution: {distribution}")
#     return data


# def generate_logistic_regression_data():
#     np.random.seed(0)
#     x, y = make_classification(
#         n_samples=100,
#         n_features=1,
#         n_informative=1,
#         n_redundant=0,
#         n_clusters_per_class=1,
#         random_state=0,
#     )
#     x = x.flatten()
#     return x, y


# def negative_log_likelihood_normal_distribution(params, data):
#     n = len(data)
#     mu, sigma = params
#     likelihood = (
#         -n / 2 * np.log(2 * np.pi)
#         - n / 2 * np.log(sigma**2)
#         - 1 / (2 * sigma**2) * np.sum((data - mu) ** 2)
#     )
#     return -likelihood  # Return negative because we minimize


# def negative_log_likelihood_exponential_distribution(params, data):
#     n = len(data)
#     lambda_ = params[0]
#     likelihood = n * np.log(lambda_) - lambda_ * np.sum(data)
#     return -likelihood  # Return negative because we minimize


# def negative_log_likelihood_poisson_distribution(params, data):
#     lambda_ = params[0]
#     # Use scipy.special.gammaln to compute the log of the factorial to avoid issues with large numbers and broadcasting.
#     log_likelihood = np.sum(data * np.log(lambda_) - lambda_ - gammaln(data + 1))
#     return -log_likelihood  # Return negative because we minimize


# def logistic(x, beta_0, beta_1):
#     return 1 / (1 + np.exp(-(beta_0 + beta_1 * x)))


# def negative_log_likelihood_logistic_regression(params, x, y):
#     beta_0, beta_1 = params
#     likelihood = y * np.log(logistic(x, beta_0, beta_1)) + (1 - y) * np.log(
#         1 - logistic(x, beta_0, beta_1)
#     )
#     return -np.sum(likelihood)  # Return negative because we minimize


# def plot_result_normal_distribution(axis, data, mu_mle, sigma_mle):
#     # print(f"Estimated mean (mu): {mu_mle}")
#     # print(f"Estimated standard deviation (sigma): {sigma_mle}")
#     axis.hist(data, bins=30, density=True, alpha=0.6, color="g", label="Data Histogram")
#     xmin, xmax = axis.get_xlim()
#     x = np.linspace(xmin, xmax, 100)
#     p = 1 / (sigma_mle * np.sqrt(2 * np.pi)) * np.exp(-((x - mu_mle) ** 2) / (2 * sigma_mle**2))
#     axis.plot(x, p, "k", linewidth=2, label="Fitted Normal Distribution")
#     axis.set_xlabel("Value")
#     axis.set_ylabel("Frequency")
#     axis.legend()


# def plot_result_exponential_distribution(axis, data, lambda_mle):
#     # print(f"Estimated rate parameter (lambda): {lambda_mle}")
#     axis.hist(data, bins=30, density=True, alpha=0.6, color="g", label="Data Histogram")
#     xmin, xmax = axis.get_xlim()
#     x = np.linspace(xmin, xmax, 100)
#     p = lambda_mle * np.exp(-lambda_mle * x)
#     axis.plot(x, p, "k", linewidth=2, label="Fitted Exponential Distribution")
#     axis.set_xlabel("Value")
#     axis.set_ylabel("Frequency")
#     axis.legend()


# def plot_result_poisson_distribution(axis, data, lambda_mle):
#     # print(f"Estimated rate parameter (lambda): {lambda_mle}")
#     axis.hist(
#         data,
#         bins=np.arange(data.min(), data.max() + 1) - 0.5,
#         density=True,
#         alpha=0.6,
#         color="g",
#         label="Data Histogram",
#     )
#     # Calculate the Poisson PMF for the fitted parameter
#     x = np.arange(data.min(), data.max() + 1)
#     poisson_pmf = (
#         np.exp(-lambda_mle) * (lambda_mle**x) / np.array([np.math.factorial(i) for i in x])
#     )
#     axis.plot(x, poisson_pmf, "k", linewidth=2, label="Fitted Poisson Distribution")
#     axis.set_xlabel("Number of Events")
#     axis.set_ylabel("Probability")
#     axis.legend()


# def plot_result_logistic_regression(axis, x, y, beta_0_mle, beta_1_mle):
#     # print(f"Estimated parameters: beta_0 = {beta_0_mle}, beta_1 = {beta_1_mle}")
#     axis.scatter(x, y, label="Data Points")
#     x_vals = np.linspace(x.min(), x.max(), 100)
#     y_vals = logistic(x_vals, beta_0_mle, beta_1_mle)
#     axis.plot(x_vals, y_vals, label="Fitted Logistic Curve", color="red")
#     axis.set_xlabel("X")
#     axis.set_ylabel("Probability")
#     axis.legend()


# def example_normal_distribution():
#     data = generate_distribution_data(
#         distribution="normal", params=SimpleNamespace(mean=5.0, sigma=2.0)
#     )
#     initial_params = [0, 1]
#     bounds = [(-np.inf, np.inf), (0.0001, np.inf)]
#     nll = negative_log_likelihood_normal_distribution
#     mle_params = solve_mle(nll, data, initial_params, bounds)
#     mu_mle, sigma_mle = mle_params
#     return data, mu_mle, sigma_mle


# def example_poisson_distribution():
#     data = generate_distribution_data(distribution="poisson", params=SimpleNamespace(lambda_=3.0))
#     initial_params = [1]
#     bounds = [(0.0001, np.inf)]
#     nll = negative_log_likelihood_poisson_distribution
#     mle_params = solve_mle(nll, data, initial_params, bounds)
#     lambda_mle = mle_params[0]
#     return data, lambda_mle


# def example_exponential_distribution():
#     data = generate_distribution_data(
#         distribution="exponential", params=SimpleNamespace(lambda_=2.0)
#     )
#     initial_params = [1]
#     bounds = [(0.0001, np.inf)]
#     nll = negative_log_likelihood_exponential_distribution
#     mle_params = solve_mle(nll, data, initial_params, bounds)
#     lambda_mle = mle_params[0]
#     return data, lambda_mle


# def example_logistic_regression():
#     x, y = generate_logistic_regression_data()
#     initial_params = [0, 0]
#     result = minimize(
#         negative_log_likelihood_logistic_regression, initial_params, args=(x, y), method="L-BFGS-B"
#     )
#     beta_0_mle, beta_1_mle = result.x
#     return x, y, beta_0_mle, beta_1_mle


# def main():
#     examples = [
#         (example_exponential_distribution, plot_result_exponential_distribution),
#         (example_poisson_distribution, plot_result_poisson_distribution),
#         (example_normal_distribution, plot_result_normal_distribution),
#         (example_logistic_regression, plot_result_logistic_regression),
#     ]
#     _, axes = plt.subplots(1, len(examples), figsize=(20, 10))
#     axes = axes.flatten()
#     for axis, (example, plotter) in zip(axes, examples):
#         out = example()
#         plotter(axis, *out)

#     plt.tight_layout()
#     plt.show()


import matplotlib.pyplot as plt

# main()
import numpy as np
from hmmlearn import hmm

# Define the HMM parameters
n_components = 2
n_features = 3
startprob = np.array([0.6, 0.4])
transmat = np.array([[0.7, 0.3], [0.4, 0.6]])
emissionprob = np.array([[0.2, 0.4, 0.4], [0.5, 0.4, 0.1]])

# Generate sample data from the HMM
np.random.seed(42)
model = hmm.MultinomialHMM(n_components=n_components, n_trials=1)
model.startprob_ = startprob
model.transmat_ = transmat
model.emissionprob_ = emissionprob

# Generate a sample sequence from the model
X, Z = model.sample(1000)

# Fit a new HMM model to the generated data
model_fit = hmm.MultinomialHMM(n_components=n_components, n_trials=1, n_iter=100, tol=0.01)
model_fit.fit(X)

# Print the estimated parameters
print("Estimated start probabilities: ", model_fit.startprob_)
print("Estimated transition matrix: ", model_fit.transmat_)
print("Estimated emission probabilities: ", model_fit.emissionprob_)

# Visualize the true and estimated transition matrices
fig, ax = plt.subplots(1, 2, figsize=(12, 5))

ax[0].matshow(transmat, cmap="viridis")
ax[0].set_title("True Transition Matrix")
for (i, j), val in np.ndenumerate(transmat):
    ax[0].text(j, i, f"{val:.2f}", ha="center", va="center", color="white")

ax[1].matshow(model_fit.transmat_, cmap="viridis")
ax[1].set_title("Estimated Transition Matrix")
for (i, j), val in np.ndenumerate(model_fit.transmat_):
    ax[1].text(j, i, f"{val:.2f}", ha="center", va="center", color="white")

plt.show()
