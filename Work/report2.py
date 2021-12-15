#!/usr/local/bin/python python3
# report.py
#
# Exercise 2.4
from pprint import pprint
from fileparse import parse_csv

def read_portfolio_tuple(filename):
    '''Read a file into a list of tuples'''
    portfolio = parse_csv(filename, select=[0, 1, 2], types=[str, int, float], has_headers=False)
    return portfolio


def read_portfolio_dict(filename):
    '''Read file into a list of dictionaries'''
    portfolio = parse_csv(filename, select=['name', 'shares', 'price'], types=[str, int, float])
    return portfolio


def read_prices(filename):
    '''Read file into a dictionary'''
    prices = parse_csv(filename, types=[str, float], has_headers=False)
    prices_dict = { price[0]: price[1] for price in prices }
    return prices_dict


def compute_portfolio(portfolio, prices):
    s = sum([holding['shares'] * holding['price'] for holding in portfolio])
    current_s = 0
    for holding in portfolio:
        try:
            current_s += holding['shares'] * prices[holding['name']]
        except KeyError:
            current_s += holding['shares'] * holding['price']
    gain = current_s - s
    return gain


def print_report(portfolio, prices):
    headers = ('Name', 'Shares', 'Price', 'Curr Price', 'Change')
    print(f'{headers[0]:>12s} {headers[1]:>12s} {headers[2]:>12s} '
    f'{headers[3]:>12s} {headers[4]:>12s}')
    print(('-' * 12 + ' ') * len(headers))
    
    for holding in portfolio:
        h_price_f = f'${holding["price"]:.2f}'
        try:
            p_price_f = f'${prices[holding["name"]]:.2f}'
            change = holding["shares"] * (prices[holding["name"]] - holding["price"])
            change_f = f'${change: ,.2f}'.replace('$-', '-$')
            print(f'{holding["name"]:>12s} {holding["shares"]:>12d} '
                f'{h_price_f:>12} {p_price_f:>12} '
                f'{change_f:>12}')
            gain = compute_portfolio(portfolio, prices)
        except KeyError:
            print(f'{holding["name"]:>12s} {holding["shares"]:>12d} '
                f'{h_price_f:>12} {"N/A":>12s} {"N/A":>12s}')
    print(('-' * 12 + ' ') * len(headers))
    print(f'{"Gain" if gain>=0 else "Loss"} of {gain:,.02f}$')
    print((('=' * 13) * len(headers))[:-1])


def portfolio_report(portfolio_file, prices_file):
    portfolio = read_portfolio_dict(portfolio_file)
    prices = read_prices(prices_file)
    print_report(portfolio, prices)


def main(argv):
    if len(argv) != 3:
        raise SystemExit(f'Usage: {argv[0]} ' 'portfolio file, prices file')
    portfolio_report(argv[1], argv[2])
    # portfolio_report('Data/portfolio.csv',
    #                 'Data/prices.csv')

if __name__ == '__main__':
    import sys
    main(sys.argv)


