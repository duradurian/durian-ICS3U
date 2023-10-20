"""
Author: Darrien Guan
Date: September 27, 2023
Description: Scalable multiplication table generator with 10 rows/colums as constant.
"""

# Global constants
MAX_MULTIPLE = 10

def generate_multiplication_table(columns_rows_quantity):
    '''Generates variabled number of multiples using nested for loops.'''

    row_list = ""
    multiple_iteration = 0

    # Displays horizontal is colums.
    print("     Columes")

    # Nested for loop multiplication.
    for term_1 in range(1, columns_rows_quantity+1):

        for term_2 in range(1, columns_rows_quantity+1):
            multiple_iteration += 1
            row_list += "%3i" % (term_1*term_2) + " "

            if multiple_iteration % MAX_MULTIPLE == 0:
                # Displays row of multiples.
                print("Row: ", row_list)
                row_list = ""


def main():
    '''mainline logic'''

    # Call generate_multiplication_table with number of rows and colums required.
    generate_multiplication_table(MAX_MULTIPLE)

main()