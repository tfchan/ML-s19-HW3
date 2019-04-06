#!python3
"""Sequential estimator of the mean and variance."""
from argparse import ArgumentParser


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
