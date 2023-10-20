"""
Author: Darrien Guan
Date: October 11, 2023
Discription: Program handles exceptions caused by divide by zero errors.
"""

def main():
    '''main logic'''

    # Repeats loop unless there is no divide by zero error.
    while True:

        # Exception handling in case of error.
        try:
            # Ask users for inputs
            numerator = int(input("Enter a numerator: "))
            denominator = int(input("Enter a denominator: "))

            # prints dividen
            print(numerator/denominator)
            break

        except ZeroDivisionError:
            print("Can not divide by zero.")

main()