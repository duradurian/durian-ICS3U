"""
Author: Darrien Guan
Date: September 29, 2023
Description: Creates a table of fahrenheit to celsius conversions, scalable.
"""

# GLOBAL CONSTANTS
MIN_TEMPERATURE_F = int(input("Enter the table's minimum fahrenheit: "))
MAX_TEMPERATURE_F = int(input("Enter the table's minimum fahrenheit: "))

def fahrenheit_to_celcius(fahrenheit):
    '''Returns fahrenheit to celcius conversion float value.'''
    return float((fahrenheit-32) * (5/9))

def temperature_table():
    '''Displays table of fahrenheit to celcius conversion from 0 f to NUMBER_OF_ROWS f.'''
    
    print("Fahrenheit | Celcius")
    for i in range(MIN_TEMPERATURE_F, MAX_TEMPERATURE_F+1):
        print("%10s | %.2f" % (i, fahrenheit_to_celcius(i)))
        
def main():
    '''mainline logic'''
    
    # Call temperature table function.
    temperature_table()

main()