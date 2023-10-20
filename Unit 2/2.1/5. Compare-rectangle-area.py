"""Author: Darrien Guan
Date: September 19, 2023
Description: Compares area of rectangle.
"""

def compare_rectangle_area(length_1, width_1, length_2, width_2):
    '''Function calculates the area of both rectangles then compares their area.'''

    # Converts lengths and widths to area.
    area_1 = length_1*width_1
    area_2 = length_2*width_2

    # Compares area of first and second rectangle then prints out corresponding statement.
    if area_1 == area_2:
        print("The first and second rectangle have the same area.")
    
    elif area_1 > area_2:
        print("The first rectangle has a greater area than the second.")

    elif area_1 < area_2:
        print("The second rectangle has a greater area than the first.")

    else:
        print("Error")



def main():
    '''mainline logic'''

    # Asks user for length and width for first rectangle
    length_1 = float(input("Enter the second rectangle's length: "))
    width_1 = float(input("Enter the second rectangle's length: "))

    # Asks user for length and width for second rectangle
    length_2 = float(input("Enter the second rectangle's length: "))
    width_2 = float(input("Enter the second rectangle's length: "))

    # Call compare_rectangle_area function
    compare_rectangle_area(length_1, width_1, length_2, width_2)

main()