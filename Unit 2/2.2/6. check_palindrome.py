"""
Author: Darrien Guan
Date: September 20, 2023
Description: Checks if 5 digit integer is a palindrome
"""

# Asks user for potential 5 digit palindrome
input_integer = int(input("Enter a 5 digit integer: "))

# Gets number of each place value
ten_thousands = input_integer // 10000 % 10
thousands = input_integer // 1000 % 10
hundreds = input_integer // 100 % 10
tens = input_integer // 10 % 10
ones = input_integer // 1 % 10

# Checks if corresponding numbers are matching and displays result.
if ten_thousands == ones and thousands == tens:
    print("The inputted number is a 5 digit palindrome.")

else:
    print("The inputted digit number is not a palindrome.")