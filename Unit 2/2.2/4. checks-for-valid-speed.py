"""Author: Darrien Guan
Date: September 20, 2023
Description: Checks if speed is within the range 0-200
"""

# Asks user for speed.
speed = float(input("Enter a speed: "))

# If else statement that checks wheter numbers are within 9 to 51 or not.
if speed > 200 or speed < 0:
    print("Invalid speed.")
else:
    print("Valid speed.")