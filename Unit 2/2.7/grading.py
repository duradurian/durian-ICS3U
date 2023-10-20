"""
Author: Darrien Guan
Date: Oct 4
Disc: Module for calcualting grades and averages.
"""

def calc_average(grade1, grade2, grade3, grade4, grade5):
    '''Averages 5 grades.'''
    return round(((grade1+grade2+grade3+grade4+grade5)/5),1)

def determine_grade(test_score):
    '''Returns test score in letter form given presentage.'''

    # Redundancy in case score isn't an integer.
    test_score = int(test_score)

    # Returns test score in accordance with the score integer.
    if test_score >= 90 and test_score <= 100:
        return "A"
    elif test_score >= 80 and test_score <= 89:
        return "B"
    elif test_score >= 70 and test_score <= 79:
        return "C"
    elif test_score >= 60 and test_score <= 69:
        return "D"
    elif test_score < 60:
        return "F"
    else:
        return "A++"
