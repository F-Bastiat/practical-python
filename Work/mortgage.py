# mortgage.py
#
# Exercise 1.7
from datetime import datetime as dt
from dateutil.relativedelta import relativedelta as rd


month = dt.strptime('2021-10-03', '%Y-%m-%d')
advance_m = 80000
advance_f = 50500
advance =  advance_m + advance_f
principal = 576100.0
_principal = principal
rate = 0.0449
periods = 360
insurance_rate = 0.0035
payment_after_7 = 2681.27
extra_payment_cal_m = [
    {'from_month': 1, 'to_month': 1, 'extra': 0},
    {'from_month': 3, 'to_month': 12, 'extra': 10000},
    {'from_month': 13, 'to_month': 24, 'extra': 10000},
    {'from_month': 25, 'to_month': 360, 'extra': 12000}
]
extra_payment_cal_f = [
    {'from_month': 1, 'to_month': 1, 'extra': 0},
    {'from_month': 3, 'to_month': 12, 'extra': 5000},
    {'from_month': 13, 'to_month': 24, 'extra': 5000},
    {'from_month': 25, 'to_month': 360, 'extra': 6000}
]
extra_payment = 0.0
bonus_cal_m = [
    {'month': 2, 'bonus': 25000},
    {'month': 5, 'bonus': 20000},
    {'month': 15, 'bonus': 20000}
]
bonus_cal_f = [
    {'month': 1, 'bonus': 21000},
    {'month': 2, 'bonus': 10000},
    {'month': 10, 'bonus': 40000},
    {'month': 22, 'bonus': 40000},
    {'month': 34, 'bonus': 40000}
]
bonus = 0.0
total_paid_m = 0.0
total_paid_f = 0.0
total_paid = 0.0
total_rates = 0.0
period = 0

print(f'{"Nr":>3} {"Mon":>10} {"Rate":>12} {"Extra M":>12} {"Extra F":>12} {"Extra":>12} {"Bonus M":>12} {"Bonus F":>12}', end=" ")
print(f'{"Bonus":>12} {"Payment":>12} {"Interest":>12} {"Princip.rate":>12} {"Total paid":>12} {"Principal":>12}')
print('------------------------------------------------------------------------------------------------------------------', end="")
print('--------------------------------------------------------')
print(f'{period:>3} {month:%Y-%m-%d} {0:>12,.2f} {0:>12,.2f} {0:>12,.2f} {0:>12,.2f} {0:>12,.2f} {0:>12,.2f}', end=" ")
print(f'{0:>12,} {0:>12,.2f} {0:>12,.2f} {0:>12,.2f} {total_paid:>12,.2f} {principal:>12,.2f}')

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
        interest = 139.07
    elif period == 85:
        interest = 1519.02
    else: 
        interest = principal * rate / 12

    if period <= 84:
        payment = payment_first_7
    else:
        payment = payment_after_7

    extra_payment_m = max([e['extra'] for e in extra_payment_cal_m if period >= e['from_month'] and period <= e['to_month']], default=0)*1.0
    extra_payment_f = max([e['extra'] for e in extra_payment_cal_f if period >= e['from_month'] and period <= e['to_month']], default=0)*1.0
    extra_payment = extra_payment_m + extra_payment_f
    if extra_payment > principal - payment:
        extra_payment = principal * (1+rate/12) - payment
        extra_payment_m = (principal * (1+rate/12) - payment) / 2
        extra_payment_f = (principal * (1+rate/12) - payment) / 2

    bonus_m = max([e['bonus'] for e in bonus_cal_m if period == e['month']], default=0)*1.0
    bonus_f = max([e['bonus'] for e in bonus_cal_f if period == e['month']], default=0)*1.0
    bonus = bonus_m + bonus_f
    if bonus > principal - payment - extra_payment:
        bonus = principal * (1+rate/12) - payment - extra_payment
        bonus_m = (principal * (1+rate/12) - payment - extra_payment) / 2
        bonus_f = (principal * (1+rate/12) - payment - extra_payment) / 2

    current_payment = payment + extra_payment + bonus
    principal_rate = payment - interest
    principal = principal - principal_rate - extra_payment - bonus
    total_paid_m = total_paid_m + extra_payment_m + bonus_m
    total_paid_f = total_paid_f + extra_payment_f + bonus_f + payment
    total_paid = total_paid + current_payment
    total_rates = total_rates + payment
    
    print(f'{period:>3} {month:%Y-%m-%d} {payment:>12,.2f} {extra_payment_m:>12,.2f} {extra_payment_f:>12,.2f} {extra_payment:>12,.2f} {bonus_m:>12,.2f}', end=" ")
    print(f'{bonus_f:>12,.2f} {bonus:>12,.2f} {current_payment:>12,.2f} {interest:>12,.2f} {principal_rate:>12,.2f} {total_paid:>12,.2f} {principal:>12,.2f}')

print('==================================================================================================================================================', end="")
print('========================')
print(f'Total paid: {total_paid:>16,.2f}')
print(f'Credit cost: {total_paid - _principal:>15,.2f}')
print(f'Months: {period:>17}')
print(f'Total rates: {total_rates:>15,.2f}')
print(f'Total paid M: {total_paid_m+advance_m:>14,.2f} | {(total_paid_m+advance_m) / (total_paid+advance):.2%}')
print(f'Total paid F: {total_paid_f+advance_f:>14,.2f} | {(total_paid_f+advance_f) / (total_paid+advance):.2%}')
print(f'Outstanding: {(max(total_paid_m+advance_m, total_paid_f+advance_f) - min(total_paid_m+advance_m, total_paid_f+advance_f))/2:>15,.2f}')