"""
Author: Darrien Guan
Date: Oct 23
Discription: Removes all negative numbers in a list.
Reason for original error: Remove function removes all items in the list that 
have the same value as the parameter of the remove function, not remove
value in the index.
"""

def remove_negs(num_list):
    '''removes all negative numbers in a list'''

    new_list = []

    # Adds only positive or zero in new_list.
    for i in range(len(num_list)):
        if num_list[i] > 0:
            new_list.append(num_list[i])

    return new_list

def main():
    '''mainlogic'''

    # Demo of rewritten function with example num list.
    num_list = [-1,-2,-3,1,2,3]
    print(remove_negs(num_list))

main()