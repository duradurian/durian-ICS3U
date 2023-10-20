"""
Author: Darrien Guan
Date: September 27, 2023
Description: Calculates the float sum of the pattern 1/10 + 2/9... + 10/1
"""

# Constants variables
NUMBER_OF_ITERATIONS = 10

def main():
    '''mainline logic'''

    series_sum = 0
    
    # Iterates series_sum for number of iterations constant.
    for i in range(NUMBER_OF_ITERATIONS):
        numerator = i+1
        denominator = NUMBER_OF_ITERATIONS-i

        series_sum += numerator/denominator
    
    # Displays summation.
    print("The sum of the fractions are:", series_sum)

main()