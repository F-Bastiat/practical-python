# mortgage.py
#
# Exercise 1.7
from datetime import datetime as dt
from dateutil.relativedelta import relativedelta as rd


month = dt.strptime('2021-11-03', '%Y-%m-%d')
principal = 576100.0
_principal = principal
rate = 0.0449
periods = 360
insurance_rate = 0.0035
payment_after_7 = 2681.27
extra_payment_calendar = [
    {'from_month': 2, 'to_month': 12, 'extra': 10000},
    {'from_month': 13, 'to_month': 24, 'extra': 12000},
    {'from_month': 25, 'to_month': 360, 'extra': 15000}
]
extra_payment = 0.0
bonus_calendar = [
    {'month': 2, 'bonus': 40000},
    {'month': 9, 'bonus': 30000},
    {'month': 21, 'bonus': 35000},
    {'month': 33, 'bonus': 40000}
]
bonus = 0.0
total_paid = 0.0
period = 0

print (f'{"Nr":>3} {"Mon":>10} {"Rate":>12} {"Extra":>12} {"Bonus":>12} {"Payment":>12} {"Interest":>12} {"Princip.rate":>12} {"Total paid":>12} {"Principal":>12}')
print('----------------------------------------------------------------------------------------------------------------------')
print(f'{period:>3} {month:%Y-%m-%d} {0:>12,.2f} {0:>12,.2f} {0:>12,} {0:>12,.2f} {0:>12,.2f} {0:>12,.2f} {total_paid:>12,.2f} {principal:>12,.2f}')

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
    
    print(f'{period:>3} {month:%Y-%m-%d} {payment:>12,.2f} {extra_payment:>12,.2f} {bonus:>12,.2f} {current_payment:>12,.2f} {interest:>12,.2f} {principal_rate:>12,.2f} {total_paid:>12,.2f} {principal:>12,.2f}')

print('======================================================================================================================')
print(f'Total paid: {total_paid:>16,.2f}\nCredit cost: {total_paid - _principal:>15,.2f}\nMonths: {period:>17}')