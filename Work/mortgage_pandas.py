# mortgage.py
#
# Exercise 1.7
from datetime import datetime as dt
import pandas as pd
from tabulate import tabulate
from dateutil.relativedelta import relativedelta as rd

pd.options.display.float_format = '{:,.2f}'.format
pd.options.display.width = 0


month = dt.strptime('2021-11-03', '%Y-%m-%d')
principal = 576100.0
_principal = principal
rate = 0.0449
periods = 360
insurance_rate = 0.0035
payment_after_7 = 2681.27
extra_payment_calendar = [
    {'from_month': 2, 'to_month': 2, 'extra': 10000.0},
    {'from_month': 3, 'to_month': 12, 'extra': 15000.0},
    {'from_month': 13, 'to_month': 24, 'extra': 18000.0},
    {'from_month': 25, 'to_month': 360, 'extra': 20000.0}
]
extra_payment = 0.0
bonus_calendar = [
    {'month': 2, 'bonus': 35000.0},
    {'month': 9, 'bonus': 30000.0},
    {'month': 21, 'bonus': 35000.0},
    {'month': 33, 'bonus': 40000.0}
]
bonus = 0.0
total_paid = 0.0
period = 0
cols=['Mon', 'Rate', 'Extra', 'Bonus', 'Payment', 'Interest', 'Principal rate', 'Total paid', 'Principal']
df = pd.DataFrame(columns=cols)

df = df.append({
        # 'Nr': period,
        'Mon': dt.strftime(month, '%Y-%m-%d'),
        'Rate': 0.0,
        'Extra': 0.0,
        'Bonus': 0.0,
        'Payment': 0.0,
        'Interest': 0.0,
        'Principal rate': 0.0,
        'Total paid': total_paid,
        'Principal': principal
    }, ignore_index=True)

for period in range(periods):
    if principal > 0:
        payment_first_7 = (rate / 12 * principal) / (1 - (1 + rate / 12) ** (period - periods))
        payment_after_7 = payment_first_7
    else:
        break
    
    period += 1
    month = month + rd(months=1)
    interest = principal * rate / 12

    if period == 1:
        interest = 1807.9
    elif period == 85:
        interest = 1519.02
    else: 
        interest = principal * rate / 12

    if period <= 84:
        payment = payment_first_7
    else:
        payment = payment_after_7

    extra_payment = max([e['extra'] for e in extra_payment_calendar if period >= e['from_month'] and period <= e['to_month']], default=0)
    if extra_payment > principal - payment:
        extra_payment = principal * (1+rate/12) - payment

    bonus = max([e['bonus'] for e in bonus_calendar if period == e['month']], default=0)
    if bonus > principal - payment - extra_payment:
        bonus = principal * (1+rate/12) - payment - extra_payment

    current_payment = payment + extra_payment + bonus
    principal_rate = payment - interest
    principal = principal - principal_rate - extra_payment - bonus
    total_paid = total_paid + current_payment
    
    df = df.append({
        # 'Nr': period,
        'Mon': dt.strftime(month, '%Y-%m-%d'),
        'Rate': payment,
        'Extra': extra_payment,
        'Bonus': bonus,
        'Payment': current_payment,
        'Interest': interest,
        'Principal rate': principal_rate,
        'Total paid': total_paid,
        'Principal': principal
    }, ignore_index=True)

print(f'Total paid: {total_paid:>16,.2f}\nCredit cost: {total_paid - _principal:>15,.2f}\nMonths: {period:>17}')

df.to_csv('Scadentar_Credit.csv')
df.to_excel('Scadentar_Credit.xlsx')

print(df)
# print(tabulate(df, headers=cols, tablefmt='psql'))