import argparse
from scipy.stats import binom
import sys


def compute_sample_size_proportion_binomial(start_n: int, 
                                            end_n: int, 
                                            step_n: int, 
                                            lower: float, 
                                            expected: float, 
                                            alpha: float, 
                                            beta: float, 
                                            print_details: bool=False) -> None:
    for n in range(start_n, end_n, step_n):
        b1 = binom(n, lower)
        b2 = binom(n, expected)
        b2_beta_quartile = int(b2.ppf(beta))
        if sum([b1.pmf(x) for x in range(b2_beta_quartile, n+1)]) <= alpha:
            print(n, b2_beta_quartile, sum([b1.pmf(x) for x in range(b2_beta_quartile, n+1)]))
        if print_details:
            print(n, b2_beta_quartile, sum([b1.pmf(x) for x in range(b2_beta_quartile, n+1)]))
            

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Sample size estimation script')
    parser.add_argument("-n_start", "--n_start", type=int, required=True,
                        help='start/smallest value of sample size to evaluate')
    parser.add_argument("-n_end", "--n_end", type=int, required=True,
                        help='end/biggest value of sample size to evaluate')
    parser.add_argument("-n_step", "--n_step", type=int, required=True,
                        help='step value of incremental sample sizes to evaluate')
    parser.add_argument("-lower", "--lower", type=float, required=True,
                        help='lower threshold defining hypothesis test')
    parser.add_argument("-expected", "--expected", type=float, required=True,
                        help='proportion one is expected to find in sample')
    parser.add_argument("-alpha", "--alpha", type=float, default=.05,
                        help='statistical significance for hypothesis test')
    parser.add_argument("-beta", "--beta", type=float, default=.05,
                        help='1 - statistical power')
    parser.add_argument("-debug", "--debug", type=bool, default=False,
                        help='Debug: print all p-values')
    args = parser.parse_args()

    try:
        compute_sample_size_proportion_binomial(args.n_start, args.n_end, args.n_step,
                                                args.lower, args.expected, args.alpha, args.beta, args.debug)
    except:
        sys.exit('Script completed with errors')
    sys.exit('Script completed successfully')
