"""
Author: Darrien Guan
Date: September 21, 2023
Description: Calculates the average of 10 numbers.
"""

def average_ten():
    '''Calculate sthe average of 10 user inputted numbers.'''

    # Sum of all inputted numbers.
    total_number = 0

    # For loop with 10 iterations.
    for i in range(10):
        user_input = float(input("Enter a number: "))
        total_number += user_input

    return total_number/10

def main():
    '''Mainline logic.'''

    # Displays average of 10 inputted numbers.
    print("The average of the 10 numbers are", average_ten())

main()