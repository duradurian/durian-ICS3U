"""
Author: Darrien Guan
Date: Oct 23
Discription: Rewrite of double preceedings function which multiplies each item in the preceeding by 2.
"""

def double_preceeding(values):
    '''Doubles preceeding item in a list and past it one index back.'''

    new_list = []

    # Adds zero if list is not empty, then it adds each value in values's index by 2.
    if values != []:

        new_list.append(0)

        for i in range(len(values)-1):
            new_list.append(values[i]*2)

        return new_list

def main():
    '''mainline logic'''

    # Demo of new function
    number_list = [1, 3, 7, 11]
    print(double_preceeding(number_list))

main()