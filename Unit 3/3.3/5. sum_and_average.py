"""
Author: Darrien Guan
Date: October 11, 2023
Discription: Prints the sum and average of numbers in numbers.txt and ignores non-numerical values.
"""

def main():

    number_of_numerics = 0
    number_sum = 0

    with open("numbers.txt", "r") as content:

        # Trys to convert all lines in numbers.txt to float.
        for line in content:
            try:
                number_sum += float(line)
                number_of_numerics += 1

            # exception for anything that is not numeric
            except: print("Text found: #", str(line))
            
    print("The average of the numeric values is:", number_sum/number_of_numerics)
    print("The sum of all numerical values is: ", number_sum)

main()