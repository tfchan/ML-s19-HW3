#!python3
"""Polynomial basis linear model data generator."""
from argparse import ArgumentParser
import numpy as np
import hw3_1a


def polynomial(noise_var, weights, n=1):
    """Generate n polynomial data."""
    basis = len(weights)
    noise = hw3_1a.normal(0, noise_var, n)
    x = np.random.uniform(-1, 1, (n))
    x_powered = np.zeros((n, basis))
    for power in range(basis):
        x_powered[:, power] = x ** power
    y = x_powered @ weights + noise
    return y


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

    values = polynomial(args.a, args.w, args.n_data)
    print(*values, sep='\n')


if __name__ == '__main__':
    main()
