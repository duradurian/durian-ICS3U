"""
Author: Darrien Guan
Date: September 27, 2023
Description: Prompts user to enter a number and validates input.
"""

def number_validation(integer_input):
    '''validates if number is within 1 to 10.'''

    # Verifies if integer_input is within 1 to 10, if not, prompts user again.
    while True:
        if integer_input <= 10 and integer_input >= 1:
            print("The inputted integer is valid.")
            return True
        else:
            print("The inputted integer is not a valid input.")
            integer_input = int(input("Enter a number in the range of 1 to 10: "))

def main():
    '''mainline logic'''

    # Asks user for input number, calls number_validation() with input.
    integer_input = int(input("Enter a number in the range of 1 to 10: "))
    number_validation(integer_input)

main()

