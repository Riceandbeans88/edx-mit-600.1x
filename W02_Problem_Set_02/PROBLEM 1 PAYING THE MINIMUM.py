__author__ = 'Aaron Echavarria'

'''
PROBLEM 1: PAYING THE MINIMUM  (10/10 points)
Write a program to calculate the credit card balance after one year if a person only pays the minimum monthly payment required by the credit card company each month.

The following variables contain values as described below:

balance - the outstanding balance on the credit card

annualInterestRate - annual interest rate as a decimal

monthlyPaymentRate - minimum monthly payment rate as a decimal

For each month, calculate statements on the monthly payment and remaining balance, and print to screen something of the format:


Month: 1
Minimum monthly payment: 96.0
Remaining balance: 4784.0
Be sure to print out no more than two decimal digits of accuracy - so print

Remaining balance: 813.41
instead of

Remaining balance: 813.4141998135
Finally, print out the total amount paid that year and the remaining balance at the end of the year in the format:

Total paid: 96.0
Remaining balance: 4784.0
A summary of the required math is found below:

    Monthly interest rate= (Annual interest rate) / 12.0
    Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
    Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
    Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)

The code you paste into the following box should not specify the values for
the variables balance,
annualInterestRate,
or monthlyPaymentRate -
our test code will define those values before testing your submission.
'''

# Paste your code into this box
total_amt_paid = 0
month = 0
for month in range(1,13):
  min_payment = monthlyPaymentRate * balance
  balance = balance - min_payment
  balance += (annualInterestRate / 12.0) * balance
  total_amt_paid += min_payment
  print 'Month:',month
  print 'Minimum monthly payment:',round(min_payment,2)
  print 'Remaining balance:',round(balance,2)


print 'Total paid:', round(total_amt_paid,2)
print 'Remaining balance:', round(balance,2)