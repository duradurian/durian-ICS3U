"""
Author: Darrien Guan
Date: September 29, 2023
Description: Checks numbers 1 to 100 if they're primes.
"""

# GLOBAL CONSTANTS
NUMBER_RANGE = 100

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
    
    # Loops that checks if all numbers from 1 to NUMBER_RANGE is a prime.
    for i in range(NUMBER_RANGE + 1):
        if is_prime(i):
            print(i)
            
main()