#!python3
"""Baysian Linear regression."""
from argparse import ArgumentParser
import numpy as np
import hw3_1b


class BaysianLinearRegressor():
    """Online Baysian linear regression."""

    def __init__(self, n_basis, noise_var, prior):
        """Initializations."""
        self._n_sample = 0
        self._n_basis = n_basis
        self._noise_var = noise_var
        self._noise_para = 1 / noise_var
        self._prior_m = np.zeros((n_basis, 1))
        self._prior_cv = prior * np.identity(n_basis)
        self._posterior_m = None
        self._posterior_cv = None
        self._predict_var = 0

    def add_sample(self, x, y):
        """Add a sample (x,y) for training."""
        self._n_sample += 1
        x_basis = np.array([x**i for i in range(self._n_basis)])
        prior_cv_inv = np.linalg.inv(self._prior_cv)
        self._posterior_cv = np.linalg.inv(prior_cv_inv
                                           + (self._noise_para
                                              * np.outer(x_basis, x_basis)))
        self._posterior_m = (self._posterior_cv
                             @ (prior_cv_inv @ self._prior_m
                                + self._noise_para * np.outer(x_basis, y)))
        pred_dist = self.predict(x)
        self._prior_cv = self._posterior_cv
        self._prior_m = self._posterior_m
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


def main():
    """Perform main task of the program."""
    parser = ArgumentParser(
        description='Baysian Linear regression using online learning')
    parser.add_argument('b', type=int,
                        help='Precision of initial prior')
    parser.add_argument('a', type=float, help='Variance of normal in noise')
    parser.add_argument('w', type=float, nargs='+',
                        help='Coefficients of each basis')
    args = parser.parse_args()

    regressor = BaysianLinearRegressor(len(args.w), args.a, args.b)
    while not regressor.is_converge():
        data_point = hw3_1b.polynomial(args.a, args.w, return_x=True)
        print(f'Add data point {data_point[0]}:\n')
        pred_dist = regressor.add_sample(*data_point[0])
        print('Posterior mean:', *regressor.mean, sep='\n', end='\n\n')
        print('Posterior covariance:', *regressor.convariance, sep='\n',
              end='\n\n')
        print(f'Predictive distribution ~ N{pred_dist}')
        print('--------------------------------------------------------------')


if __name__ == '__main__':
    main()
