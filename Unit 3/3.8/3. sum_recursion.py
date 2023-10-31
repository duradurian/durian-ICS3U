"""
Author: Darrien Guan
Date: October 26, 2023
Discription: Function returns the sum of all numbers leading up to input number, starting from 1.
"""

def summation(n):
    '''Returns the sum of all numbers leading up to input number, starting from 1.'''
    
    # Auto returns 0 if n is 0 to prevent infinite loop.
    if n == 0:
        return 0
    
    # Return the sum of all numbers from n to 1.
    return n + summation(n-1)

def main():
    '''main logic'''
    
    # Ask user for input
    input_number = int(input("Enter a number to summate: "))
    
    # Display result of summation
    print(summation(input_number))
    
main()