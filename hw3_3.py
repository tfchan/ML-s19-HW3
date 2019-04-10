#!python3
"""Baysian Linear regression."""
from argparse import ArgumentParser


class BaysianLinearRegressor():
    """Online Baysian linear regression."""

    def __init__(self, n_basis, noise_var, prior):
        """Initializations."""
        self._n_sample = 0
        self._n_basis = n_basis
        self._noise_var = noise_var
        self._prior = prior
        self._posterior = None

    def add_sample(self, x, y):
        """Add a sample (x,y) for training."""


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


if __name__ == '__main__':
    main()
