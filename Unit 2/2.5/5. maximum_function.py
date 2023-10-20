"""
Author: Darrien Guan
Date: September 29, 2023
Description: Displays the greatest of three inputted numbers.
"""

def maximum(num_1, num_2, num_3):
    '''returns the float greatest of the three parameters'''
    
    # Compares all numbers to each other and returns greatest one.
    if num_1 > num_2 and num_1 > num_3:
        return num_1
    elif num_2 > num_3:
        return num_2
    else:
        return num_3
    
def main():
    '''mainline logic'''
    
    # Get user inputs 
    num_1 = float(input("Enter the first number: "))
    num_2 = float(input("Enter the second number: "))
    num_3 = float(input("Enter the third number: "))
    
    # Calls maximum function and displays the greatest.
    print("The greatest number is:", maximum(num_1,num_2, num_3))
    
main()