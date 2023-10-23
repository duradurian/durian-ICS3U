"""
Author: Darrien Guan
Date: Oct 23
Discription: Function that reverses list.
"""

def reverse_list(input_list):
    '''Function reverses list. Algorithm based, no built in functions!'''

    new_list = []

    # Uses length of input list and appends the reverse index
    for i in range(len(input_list)):
        new_list.append(input_list[-i-1])

    return new_list

def main():
    '''Main logic'''

    # Example list and display demo of reverse_list function
    animals = ["dog", "cat", "bear"]
    print(reverse_list(animals))

main()