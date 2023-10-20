"""
Author: Darrien Guan
Date: September 29, 2023
Description: Rolls dice 100 times and summarizes results.
"""

import random

# GLOBAL CONSTANTS
NUMBER_OF_ROLLS = 1000

def dice_simulation():
    '''Returns a random value from 1 to 6, like a die.'''
    return random.randint(1,6)

def main():
    '''mainline logics'''
    
    # Number of numbers 1 to 6 rolled.
    number_of_1 = 0
    number_of_2 = 0
    number_of_3 = 0
    number_of_4 = 0
    number_of_5 = 0
    number_of_6 = 0
    
    # Runs dice_simulation function for NUMBER_OF_ROLLS times.
    for i in range(1, NUMBER_OF_ROLLS + 1):
        dice_roll = dice_simulation()
        
        # Adds to list of number of times rolled variables.
        if dice_roll == 1:
            number_of_1 += 1
        elif dice_roll == 2:
            number_of_2 += 1
        elif dice_roll == 3:
            number_of_3 += 1
        elif dice_roll == 4:
            number_of_4 += 1
        elif dice_roll == 5:
            number_of_5 += 1
        elif dice_roll == 6:
            number_of_6 += 1
            
    # Displays how many times each dice value was rolled.
    print('''FINAL RESULTS
          Number of 1's: %i
          Number of 2's: %i
          Number of 3's: %i
          Number of 4's: %i
          Number of 5's: %i
          Number of 6's: %i''' % (number_of_1, number_of_2, number_of_3, number_of_4, number_of_5, number_of_6))

main()
    