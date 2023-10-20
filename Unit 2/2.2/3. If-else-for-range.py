"""Author: Darrien Guan
Date: September 20, 2023
Description: Sees if number is in or outside range of 9 to 51
"""

# Asks user for number.
number = float(input("Enter a number: "))

# If else statement that checks wheter numbers are within 9 to 51 or not.
if number > 51 or number < 9:
    print("Invalid points.")
else:
    print("Valid points.")