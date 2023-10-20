"""Author: Darrien Guan
Date: September 19, 2023
Description: Converts integers 1-10 to roman numeral.
"""

def roman_numeral(integer_input):
    '''Function converts integer in the range of 1-10 to roman numeral.'''

    # Converts integers 1-10 to roman numeral, if out of range, it displays and error.
    if integer_input == 1:
        numeral = "I"
    elif integer_input == 2:
        numeral = "II"
    elif integer_input == 3:
        numeral = "III"
    elif integer_input == 4:
        numeral = "IV"
    elif integer_input == 5:
        numeral = "V"
    elif integer_input == 6:
        numeral = "VI"
    elif integer_input == 7:
        numeral = "VII"
    elif integer_input == 8:
        numeral = "VIII"
    elif integer_input == 9:
        numeral = "IX"
    elif integer_input == 10:
        numeral = "X"
    else: 
        numeral = "Error: Integer out of range."

    # Displays the value of numeral
    print(numeral)

def main():
    '''Mainline logic'''

    # Asks user for integer input.
    integer_input = int(input("Enter an integer 1-10: "))

    # Calls roman_numeral() function.
    roman_numeral(integer_input)

main()