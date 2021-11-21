# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
extra_payment_start_month = 1
extra_payment_end_month = 12
extra_payment = 1000
total_paid = 0.0
month = 0

print (f'{"Mon":>3} {"Payment":>12} {"Total paid":>12} {"Principal":>12}')
print(f'{month:>3} {0:>12,.2f} {total_paid:>12,.2f} {principal:>12,.2f}')

while principal > 0:
    month += 1
    if month >= extra_payment_start_month and month <= extra_payment_end_month:
        current_payment = payment + extra_payment
    else: current_payment = payment

    if principal < current_payment:
        current_payment = principal * (1+rate/12)

    principal = principal * (1+rate/12) - current_payment
    total_paid = total_paid + current_payment
    
    print(f'{month:>3} {current_payment:>12,.2f} {total_paid:>12,.2f} {principal:>12,.2f}')

print('==========================================')
print(f'Total paid: {total_paid:,.2f}\nMonths: {month:>7}')