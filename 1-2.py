import math
import sys


def print_line():
    print("----------------------------------------")


print("Adding 50 + 50:")
print(50 + 50)
print("Subtracting 100 - 10:")
print(100 - 10)
print_line()

print("30+*6 (interpreting this as 30 + 6, as the original is a syntax error):")
print(30 + 6)
print("6 ^ 6 (bitwise exclusive OR):")
print(6 ^ 6)
print("6 ** 6 (6 raised to the 6th power):")
print(6 ** 6)
print("6+6+6+6+6+6:")
print(6+6+6+6+6+6)
print_line()

print("Hello World")
print("Hello World : 10")
print_line()

# payment calculator
if (len(sys.argv) != 4):
    print("Can't calculate payment! Usage: \"py 1-2.py <principal> <interest rate> <number of months>\" ")
else:
    try:
        principal = int(sys.argv[1])  # index 0 is the script
        rate = int(sys.argv[2]) * 0.01
        months = int(sys.argv[3])
        total = 0
        rate_per_month = rate / 12
        # https://en.wikipedia.org/wiki/Compound_interest#Exact_formula_for_monthly_payment
        payment = (principal * rate_per_month) / \
            (1 - (1 / (1 + rate_per_month) ** months))
        payment = math.ceil(payment)
        print("Monthly payment for principal " + str(principal) + ", annual interest rate " +
              str(rate * 100) + "%, and payment period of " + str(months) + " months:")
        print(payment)

    except ValueError:
        print("Can't calculate payment! Usage: \"py 1-2.py <principal> <interest rate> <number of months>\" ")
