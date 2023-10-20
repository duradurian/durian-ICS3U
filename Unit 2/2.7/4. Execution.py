"""
Author: Darrien Guan
Date: Oct 4
Disc: Calculates grades and averages then displays them.
"""

import grading

def main():
    '''Mainline logic'''

    # Asks user for input
    score_1 = int(input("Enter the 1st score in precent: "))
    score_2 = int(input("Enter the 2nd score in precent: "))
    score_3 = int(input("Enter the 3rd score in precent: "))
    score_4 = int(input("Enter the 4th score in precent: "))
    score_5 = int(input("Enter the 5th score in precent: "))

    # Prints average grade and calls calc_average
    print("The average grade is %.1f percent" % grading.calc_average(score_1,score_2,score_3,score_4,score_5))

    # Prints the letter grade for each grade
    for i in [score_1,score_2,score_3,score_4,score_5]:
        print("The grade for " + str(i) + "%" + " is " + grading.determine_grade(i))

main()