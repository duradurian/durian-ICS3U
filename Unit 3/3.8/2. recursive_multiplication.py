"""
Author: Darrien Guan
Date: October 26, 2023
Discription: multiplies another number by another number using recursion
"""

def multiply(x, y):
    '''multiplies two numbers using recursion'''
    
    # If x or y is zero, it returns 0
    if x == 0 or y == 0:
        return 0
    
    # Return value with repeated addition of x-1 to y
    return y + multiply(x-1,y)

def main():
    '''main logic'''
    
    # sample numbers
    x = 9
    y = 6
    
    # Output sample results
    print(multiply(x,y))
    
main()