#!python3
"""Baysian Linear regression."""
from argparse import ArgumentParser


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


if __name__ == '__main__':
    main()
