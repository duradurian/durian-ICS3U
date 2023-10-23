"""
Author: Darrien Guan
Date: Oct 23
Discription: Function that reverses list.
"""

def total(input_list):
    '''Sums the total of all numerical values in list.'''

    num_sum = 0

    # Attempts to sum all values in list. If non-numerical, it passes.
    for i in range(len(input_list)):
        try:
            num_sum += input_list[i]
        except:
            pass

    return num_sum

def main():
    '''main logic'''

    # Example list and display demo
    example_list = ["dog", 3, 4, "cat"]
    print(total(example_list))

main()