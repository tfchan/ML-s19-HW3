#!python3
"""Polynomial basis linear model data generator."""
from argparse import ArgumentParser


def main():
    """Perform main task of the program."""
    parser = ArgumentParser(
        description='Polynomial basis linear model data generator')
    parser.add_argument('a', type=float, help='Variance of normal in noise')
    parser.add_argument('w', type=float, nargs='+',
                        help='Coefficients of each basis')
    parser.add_argument('-n', '--n_data', type=int, default=1,
                        help='Number of data to generate')
    args = parser.parse_args()


if __name__ == '__main__':
    main()
