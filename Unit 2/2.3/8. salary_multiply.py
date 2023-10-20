"""
Author: Darrien Guan
Date: September 21, 2023
Description: Calculates the salary for a person's whose salary starts a 1 cent and multiplies by 2 every day.
"""

# global constants
PENNY_VALUE = 0.01

def earnings(days):
    '''Calculates salary of person starting with $0.01 and multiplies by 2 every day.'''

    # Starting salary
    total_earnings = 0.01
    previous_day_total = 0.01
    
    print('''
Day    |   Salary
--------------------------------''')
    # Multiplies total earnings by 2 every day.
    for day_number in range(days+1):
        print("| %4s | $%20.2f |" % (day_number,((total_earnings*2)-previous_day_total)))
        total_earnings *= 2
        previous_day_total = total_earnings
    
    return total_earnings

def main():
    '''mainline logic'''

    # Asks user for number of day for salary.
    number_of_days = earnings(int(input("Enter the number of days: ")))

    # Displays total salary at the end of the last day.
    print("The total earnings is: $" + str(number_of_days))

main()