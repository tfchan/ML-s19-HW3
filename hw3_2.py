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
        return self.m2_to_var(self._curr_m2, self._n_sample)

    @property
    def n_sample(self):
        """Getter of number of sample."""
        return self._n_sample

    @staticmethod
    def m2_to_var(m2, n_sample):
        """Convert m2 to variance."""
        return m2 / (n_sample - 1) if n_sample > 1 else 0

    def get_estimations(self):
        """Return current estimations."""
        return (self.mean, self.variance, self.n_sample)

    def is_converge(self):
        """Return estimation is converged or not."""
        threshold = 0.0001
        mean_conv = abs(self._prev_mean - self._curr_mean) < threshold
        curr_var = self.variance
        prev_var = self.m2_to_var(self._prev_m2, self._n_sample - 1)
        var_conv = abs(prev_var - curr_var) < threshold
        return mean_conv and var_conv


def main():
    """Perform main task of the program."""
    parser = ArgumentParser(
        description='Sequential estimator of the mean and variance')
    parser.add_argument('mean', type=float,
                        help='Gaussian mean of number to be guessed')
    parser.add_argument('variance', type=float,
                        help='Gaussian variance of number to be guessed')
    args = parser.parse_args()

    print(f'Data point source function: N({args.mean}, {args.variance})')
    estimator = SequentialEstimator()
    while not estimator.is_converge() or estimator.n_sample == 0:
        sample = float(hw3_1a.normal(args.mean, args.variance))
        print(f'Add data point: {sample}')
        estimator.add_sample(sample)
        print(f'Mean = {estimator.mean}\tVariance = {estimator.variance}')
        print()


if __name__ == '__main__':
    main()
