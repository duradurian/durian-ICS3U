"""
Author: Darrien Guan
Date: September 20, 2023
Description: Calculates BMI and displays BMI meaning
"""

def bmi(weight, height):
    '''Function calculates using the formula kg/m^2 and prints BMI'''

    # calculates BMI using kg/m^2
    calculate_bmi = weight/height**2

    # displays calculated BMI
    print("Your BMI is %.2f in kg/m^2" % calculate_bmi)

    # Prints BMI meaning with ranges.
    if calculate_bmi <= 24.9 and calculate_bmi > 18.5:
        print("You have an optimal weight.")
    elif calculate_bmi <= 18.5:
        print("You are underweight.")
    elif calculate_bmi >= 25 and calculate_bmi <= 29.9:
        print("You are overweight.")
    elif calculate_bmi > 30:
        print("You are obese.")
    else: print("Unable to display your BMI status.")

def main():
    '''mainlogic: function takes weight in kg and height in meters and calls bmi() function'''

    weight = float(input("What is your weight in kg?: "))
    height = float(input("What is your height in meters?: "))
    bmi(weight,height)
main()