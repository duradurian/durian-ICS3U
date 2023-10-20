"""
Author: Darrien Guan
Date: September 29, 2023
Description: Checks if user inputted number is a prime.
"""

def is_prime(input_number):
    '''Function checks if prime using trial division.'''
    
    # Returns false if it's 1
    if input_number == 1:
        return False
    
    # Returns false if number is divisible by a number between 2 and itself.
    for i in range(2, input_number):
        if input_number % i == 0:
            return False
    
    # Returns True if the loop completes without finding any divisors. 
    return True
    
def main():
    '''mainline logic'''
    
    # Asks user for input integer while input is not 0.
    while True:
        input_number = int(input("Enter an integer: "))
        
        if input_number == 0:
            break
        
        # Displays whether input_number is a prime or not.
        if is_prime(input_number):
            print("The inputted number is a prime.")
            
        else: print("The inputted number is not a prime.")
            
main()