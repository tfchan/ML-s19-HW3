#!python3
"""Sequential estimator of the mean and variance."""
from argparse import ArgumentParser
import hw3_1a


class SequentialEstimator:
    """Sequential estimator for mean and variance."""

    def __init__(self):
        """Initialize member variables."""

    def _update_mean(self, sample):
        """Update mean with sample."""

    def _update_var(self, sample):
        """Update var with sample."""

    def add_sample(self, sample):
        """Add sample to update estimations."""

    def get_estimations(self):
        """Return current estimations."""


def main():
    """Perform main task of the program."""
    parser = ArgumentParser(
        description='Sequential estimator of the mean and variance')
    parser.add_argument('mean', type=float,
                        help='Gaussian mean of number to be guessed')
    parser.add_argument('variance', type=float,
                        help='Gaussian variance of number to be guessed')
    args = parser.parse_args()


if __name__ == '__main__':
    main()
