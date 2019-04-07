#!python3
"""Sequential estimator of the mean and variance."""
from argparse import ArgumentParser
import hw3_1a


class SequentialEstimator:
    """Sequential estimator for mean and variance."""

    def __init__(self):
        """Initialize member variables."""
        self._curr_mean = 0
        self._prev_mean = 0
        self._curr_m2 = 0
        self._prev_m2 = 0
        self._n_sample = 0

    def _update_mean(self, sample):
        """Update mean with sample."""
        self._curr_mean = (self._prev_mean
                           + (sample - self._prev_mean) / self._n_sample)

    def _update_m2(self, sample):
        """Update m2 with sample."""
        self._curr_m2 = (self._prev_m2
                         + ((sample - self._prev_mean)
                            * (sample - self._curr_mean)))

    def add_sample(self, sample):
        """Add sample to update estimations."""
        self._n_sample += 1
        self._prev_mean = self._curr_mean
        self._prev_m2 = self._curr_m2
        self._update_mean(sample)
        self._update_m2(sample)

    @property
    def mean(self):
        """Getter of current mean."""
        return self._curr_mean

    @property
    def variance(self):
        """Getter of current variance."""
        return self._curr_m2 / (self._n_sample - 1) if self.n_sample > 1 else 0

    @property
    def n_sample(self):
        """Getter of number of sample."""
        return self._n_sample

    def get_estimations(self):
        """Return current estimations."""
        return (self.mean, self.variance, self.n_sample)


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
