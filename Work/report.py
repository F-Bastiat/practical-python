# report.py
#
# Exercise 2.4
import csv
from pprint import pprint

def read_portfolio_tuple(filename):
    '''Read file into a list of tuples'''
    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            try:
                holding = (row[0], int(row[1]), float(row[2]))
                portfolio.append(holding)
            except:
                TypeError(f'Incorrect data type on row:\n{row}')
    return portfolio


def read_portfolio_dict(filename):
    '''Read file into a list of dictionaries'''
    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for i, row in enumerate(rows):
            holding = dict(zip(headers, row))
            try:
                holding['shares'] = int(holding['shares'])
                holding['price'] = float(holding['price'])
                portfolio.append(holding)
            except:
                TypeError(f'Incorrect data type on row {i}:\n{row}')
    return portfolio


def read_prices(filename):
    '''Read file into a dictionary'''
    prices = {}

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except:
                TypeError(f'Incorrect data type on row:\n{row}')
    return prices


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


portfolio_report('Data/portfolio.csv',
                 'Data/prices.csv')
