#!python3
"""Univariate Gaussian data generator."""
from argparse import ArgumentParser


def main():
    """Perform main task of the program."""
    parser = ArgumentParser(description='Univariate Gaussian data generator')
    parser.add_argument('mean', type=float, help='Gaussian mean')
    parser.add_argument('variance', type=float, help='Gaussian variance')
    parser.add_argument('-n', '--n_data', type=int, default=1,
                        help='Number of data to generate')
    args = parser.parse_args()


if __name__ == '__main__':
    main()
