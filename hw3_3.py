#!python3
"""Baysian Linear regression."""
from argparse import ArgumentParser
import numpy as np
# import hw3_1b


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

    def add_sample(self, x, y):
        """Add a sample (x,y) for training."""
        x_basis = np.array([x**i for i in range(self._n_basis)])
        prior_cv_inv = np.linalg.inv(self._prior_cv)
        self._posterior_cv = np.linalg.inv(prior_cv_inv
                                           + (self._noise_para
                                              * np.outer(x_basis, x_basis)))
        self._posterior_m = (self._posterior_cv
                             @ (prior_cv_inv @ self._prior_m
                                + self._noise_para * np.outer(x_basis, y)))
        self._prior_cv = self._posterior_cv
        self._prior_m = self._posterior_m

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
    regressor.add_sample(-0.64152, 0.19039)
    regressor.add_sample(0.07122, 1.63175)
    regressor.add_sample(-0.19330, 0.24507)
    # data_point = hw3_1b.polynomial(args.a, args.w)
    # regressor.add_sample(*hw3_1b.polynomial(args.a, args.w))


if __name__ == '__main__':
    main()
