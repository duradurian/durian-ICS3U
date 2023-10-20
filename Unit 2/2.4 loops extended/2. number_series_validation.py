"""
Author: Darrien Guan
Date: September 27, 2023
Description: Asks user for number inputs and sorts largest to greatest.
"""

def positive_num_validation(input_num):
    '''Checks if number is positive.'''
    
    if input_num >= 0:
        return True
    else: return False

def main():
    '''Mainline logic'''

    # Negative infinity and positive infinity floats for unlimited positive input range.
    min_val = float('inf')
    max_val = float('-inf')

    # Checks whether inputted number is less or greater  than current min/max value.
    while True:
        num_input = int(input("Enter a number: "))
        if not positive_num_validation(num_input):
            break
        elif num_input > max_val:
            max_val = num_input
        elif num_input < min_val:
            min_val = num_input

    # Displays result.
    print("The minimum value of the inputted values is", min_val)
    print("The maximum value of the inputted values is", max_val)

main()