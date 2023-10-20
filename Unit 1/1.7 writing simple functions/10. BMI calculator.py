"""
Author: Darrien Guan
Date: September 14, 2023
Description: Calculates BMI given a person's weight in kg and height in m.
"""

def bmi(weight, height):
    '''Function calculates using the formula kg/m^2 and prints BMI'''

    # calculates BMI using kg/m^2
    calculate_bmi = weight/height**2

    # displays calculated BMI
    print("Your BMI is %.2f in kg/m^2" % calculate_bmi)

def main():
    '''mainlogic: function takes weight in kg and height in meters and calls bmi() function'''

    weight = float(input("What is your weight in kg?: "))
    height = float(input("What is your height in meters?: "))
    bmi(weight,height)
main()