#!python3
"""Bayesian Linear regression."""
from argparse import ArgumentParser
import numpy as np
import matplotlib.pyplot as plt
import hw3_1b


class BayesianLinearRegressor():
    """Online Bayesian linear regression."""

    def __init__(self, n_basis, noise_var, prior):
        """Initializations."""
        self._n_sample = 0
        self._n_basis = n_basis
        self._noise_var = noise_var
        self._noise_para = 1 / noise_var
        self._prior_m = None
        self._prior_cv = None
        self._posterior_m = np.zeros((n_basis, 1))
        self._posterior_cv = prior * np.identity(n_basis)
        self._predict_var = 0

    def add_sample(self, x, y):
        """Add a sample (x,y) for training."""
        self._n_sample += 1
        self._prior_cv = self._posterior_cv
        self._prior_m = self._posterior_m
        x_basis = np.array([x**i for i in range(self._n_basis)])
        prior_cv_inv = np.linalg.inv(self._prior_cv)
        self._posterior_cv = np.linalg.inv(prior_cv_inv
                                           + (self._noise_para
                                              * np.outer(x_basis, x_basis)))
        self._posterior_m = (self._posterior_cv
                             @ (prior_cv_inv @ self._prior_m
                                + self._noise_para * np.outer(x_basis, y)))
        pred_dist = self.predict(x)
        self._predict_var = pred_dist[1]
        return pred_dist

    def predict(self, x):
        """Predict corresponding y of x."""
        x_basis = np.array([x**i for i in range(self._n_basis)])
        predict_mean = self._prior_m.flatten() @ x_basis
        predict_var = (self._noise_var
                       + x_basis @ self._prior_cv @ x_basis)
        return predict_mean, predict_var

    def is_converge(self):
        """Return converged or not."""
        threshold = 0.005
        return (self._predict_var - self._noise_var < threshold
                and self._n_sample > 0)

    @property
    def mean(self):
        """Getter of posterior mean."""
        return self._posterior_m

    @property
    def convariance(self):
        """Getter of posterior covariance."""
        return self._posterior_cv


def plot_curve(x, y, var, loc, data_points=None, title=''):
    """Plot a curve of weights, with its variance curve."""
    ax = plt.subplot(2, 2, loc)
    ax.set_title(title)
    ax.plot(x, y, 'k-')
    ax.plot(x, y + var, 'r-')
    ax.plot(x, y - var, 'r-')
    if not (data_points is None):
        points = np.array(data_points)
        ax.plot(points[:, 0], points[:, 1], 'c.')


def main():
    """Perform main task of the program."""
    parser = ArgumentParser(
        description='Bayesian Linear regression using online learning')
    parser.add_argument('b', type=int,
                        help='Precision of initial prior')
    parser.add_argument('a', type=float, help='Variance of normal in noise')
    parser.add_argument('w', type=float, nargs='+',
                        help='Coefficients of each basis')
    args = parser.parse_args()

    plt.figure()
    x = np.arange(-2, 2, 0.05)
    x_basis = np.array(
        [[x_point**i for i in range(len(args.w))] for x_point in x])
    y = x_basis @ args.w
    plot_curve(x, y, args.a, 1, title='Ground truth')

    regressor = BayesianLinearRegressor(len(args.w), args.a, args.b)
    data_points = np.empty((0, 2))
    while not regressor.is_converge():
        data_point = hw3_1b.polynomial(args.a, args.w, return_x=True)[0]
        data_points = np.vstack((data_points, [data_point[0], data_point[1]]))
        print(f'Add data point {data_point}:\n')
        pred_dist = regressor.add_sample(*data_point)
        print('Posterior mean:', *regressor.mean, sep='\n', end='\n\n')
        print('Posterior covariance:', *regressor.convariance, sep='\n',
              end='\n\n')
        print(f'Predictive distribution ~ N{pred_dist}')
        print('--------------------------------------------------------------')
        if data_points.shape[0] == 10:
            y = np.array([regressor.predict(x1) for x1 in x])
            plot_curve(x, y[:, 0], y[:, 1], 3, data_points=data_points,
                       title='After 10 incomes')
        elif data_points.shape[0] == 50:
            y = np.array([regressor.predict(x1) for x1 in x])
            plot_curve(x, y[:, 0], y[:, 1], 4, data_points=data_points,
                       title='After 50 incomes')
    y = np.array([regressor.predict(x1) for x1 in x])
    plot_curve(x, y[:, 0], y[:, 1], 2, data_points=data_points,
               title='Predict result')
    plt.show()


if __name__ == '__main__':
    main()
