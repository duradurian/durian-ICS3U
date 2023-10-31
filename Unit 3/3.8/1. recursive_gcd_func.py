"""
Author: Darrien Guan
Date: October 26, 2023
Discription: Finds GCD of two numbers using recursion.
"""

def gcd(n, m):
    '''finds gcd of number using recursion'''
    
    if n == 0:
        return m
    
    elif n > 0:
        return gcd(n,m % n)
    
def main():
    '''main logic'''
    
    # Sample numbers
    n = 10
    m = 20
    
    print(gcd(n,m))
    
main()