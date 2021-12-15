#!/usr/local/bin/python python3
# pcost.py
#
# Exercise 1.27
from report2 import read_portfolio_dict

def portfolio_cost(filename):
    portfolio = read_portfolio_dict(filename)
    total_cost = sum([ holding['shares']*holding['price'] for holding in portfolio ])
    print('Total cost', total_cost)


def main(argv):
    if len(argv) != 2:
        raise SystemExit(f'Usage: {argv[0]} ' 'portfolio file')
    portfolio_cost(argv[1])


if __name__ == '__main__':
    import sys
    main(sys.argv)


# portfolio_cost('Data/missing.csv')
# portfolio_cost('Data/portfoliodate.csv')