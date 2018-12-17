# problem 1
# Write a program to calculate the credit card balance after one year if a person only pays the minimum monthly payment required by the credit card company each month.
# The following variables contain values as described below: balance - the outstanding balance on the credit card, annualInterestRate - annual interest rate as a decimal,
# monthlyPaymentRate - minimum monthly payment rate as a decimal
# For each month, calculate statements on the monthly payment and remaining balance. At the end of 12 months, print out the remaining balance.
# Be sure to print out no more than two decimal digits of accuracy
# So your program only prints out one thing: the remaining balance at the end of the year in the format: Remaining balance: 4784.0
month = 1
while month <= 12:
  up_bal = balance - (monthlyPaymentRate * balance)
  balance = up_bal + (1/12 * annualInterestRate * up_bal)
  month += 1
print("Remaining balance: ", round(balance, 2))

# problem 2
# Now write a program that calculates the minimum fixed monthly payment needed in order pay off a credit card balance within 12 months.
# By a fixed monthly payment, we mean a single number which does not change each month, but instead is a constant amount that will be paid each month.
# In this problem, we will not be dealing with a minimum monthly payment rate.
# The program should print out one line: the lowest monthly payment that will pay off all debt in under 1 year, for example: Lowest Payment: 180
# Assume that the interest is compounded monthly according to the balance at the end of the month (after the payment for that month is made).
# The monthly payment must be a multiple of $10 and is the same for all months. Notice that it is possible for the balance to become negative using this payment scheme.
min_pay = 0
temp_bal = balance

while temp_bal > 0:
  month = 1
  min_pay += 10
  temp_bal = balance
  while month <= 12:
    up_bal = temp_bal - min_pay
    temp_bal = up_bal + (1/12 * annualInterestRate * up_bal)
    month += 1

print("Lowest payment: ", min_pay)

# problem 3
# Using Bisection Search to Make the Program Faster
# Write a program that uses these bounds and bisection search (for more info check out the Wikipedia page on bisection search) to find the smallest
# monthly payment to the cent (no more multiples of $10) such that we can pay off the debt within a year.
# Try it out with large inputs, and notice how fast it is (try the same large inputs in your solution to Problem 2 to compare!).
# Produce the same return value as you did in Problem 2.
epsilon = 0.1
min = balance / 12
max = (balance * (1 + annualInterestRate) ** 12) / 12
guess = (min + max) / 2


while True:
    temp_balance = balance
    for month in range(1, 13):
        temp_balance -= guess
        temp_balance += temp_balance * (annualInterestRate / 12)

    if temp_balance > 0 and temp_balance <= epsilon:
        print('Lowest Payment:', round(guess, 2))
        break
    elif temp_balance > epsilon:
        min = guess
    elif temp_balance < epsilon:
        max = guess

    guess = (min + max) / 2
