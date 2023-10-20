"""Author: Darrien Guan
Date: September 14, 2023
Description: Mainline function executes times_time() function to multiply input by 10.
"""

def times_ten(a):
    '''Function multiplies input by 10 then outputs the product.'''

    a = a*10

    #displays the value of a
    print(a)

def main():
    '''mainline logic'''
    
    num = float(input("Insert a number: "))
    times_ten(num)

main()