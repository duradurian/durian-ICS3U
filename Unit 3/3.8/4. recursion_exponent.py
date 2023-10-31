"""
Author: Darrien Guan
Date: October 26, 2023
Discription: Function evaluates base (x) to the power (y) using recursion
"""

def pow(x, y):
    '''returns n to the power of y'''
    
    # returns 1 if y is 0 since it's a basic law of math.
    if y == 0:
        return 1
    
    # Multiplies x by x, y many times
    return x*pow(x, y-1)

def main():
    '''mainlogic'''
    
    # Ask user for input
    base = int(input("Enter the base of an exponent: "))
    power = int(input("Enter the power of an exponent: "))
    
    # Display results
    print(pow(base,power))
    
main()