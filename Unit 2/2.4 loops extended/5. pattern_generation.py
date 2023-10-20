"""
Author: Darrien Guan
Date: September 27, 2023
Description: Pattern generator.
"""

# Global constants
TRIANGLE_PATTERN_ITERATIONS = 6
RECTANGLE_PATTERN_ITERATIONS = 3
RECTANGLE_PATTERN_ROW_COUNT = 8

def triangle_pattern_gen(tri_first_term):
    '''Generate triangle pattern.'''

    # Generates text based on astricks_quantity in for loop.
    for astrisks_quantity in range(tri_first_term,0 , -1):
        print(astrisks_quantity*"* ")

def rectangle_pattern_gen(rec_first_term):
    '''Generate rectangle pattern.'''

    # Generates rows with astricks based on RECTANGLE_PATTERN_ITERATIONS.
    for astrisks_quantity in range(rec_first_term):
        print("* " * RECTANGLE_PATTERN_ROW_COUNT)

def main():
    '''mainline logic'''

    # Call triangle generation function
    triangle_pattern_gen(TRIANGLE_PATTERN_ITERATIONS)

    # Display space between calls.
    print("")

    # Call rectangle generation function
    rectangle_pattern_gen(RECTANGLE_PATTERN_ITERATIONS)

main()