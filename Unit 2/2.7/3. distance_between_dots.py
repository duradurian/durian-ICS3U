"""
Author: Darrien Guan
Date: Oct 4
Disc: Calculates distance between two dots.
"""

import math

def distance_dots(x1, x2, y1, y2):
    '''calculates distance between 4 coordinate points.'''
    return math.sqrt((x2-x1)**2+(y2-y1)**2)

def main():
    '''Mainline logic'''

    # Asks user for coordinates of two point.
    x1 = float(input("Enter x for point 1: "))
    y1 = float(input("Enter y for point 1: "))
    x2 = float(input("Enter x for point 2: "))
    y2 = float(input("Enter y for point 2: "))

    print("The distance between the two dots is %.2f" % distance_dots(x1,x2,y1,y2))

main()
