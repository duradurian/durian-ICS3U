"""
Author: Darrien Guan
Date: Oct 23
Discription: Multiplies each element in list by 2.
"""

def double_it(number_list):
    '''Doubles each numerical value in a list.'''

    # Multiplies each element in list by 2
    for i in range(len(number_list)):
        number_list[i] = number_list[i]*2

    # Returns new number_list
    return number_list

def main():
    '''main logic'''

    # Example number list + display sample output example number list.
    number_list = [1,2,3,4]
    print(double_it(number_list))

main()