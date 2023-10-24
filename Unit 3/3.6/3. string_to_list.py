"""
Author: Darrien Guan
Date: Oct 24
Discription: Function that converts string to list.
"""

def string_to_list(input_string):
    '''Converts string to formatted list. Split using >'''

    new_list = []
    temp_item = ""

    for i in range(len(input_string)):
        
        if input_string[i] != ">":
            temp_item += input_string[i]

        else: 
            new_list += [temp_item]
            temp_item = ""

    if len(temp_item) > 0:
        new_list += [temp_item]

        
    return new_list

def main():
    '''main logic'''

    # Example string.
    my_string = "cookies>milk>fudge>cake>ice cream"

    # Display and call string_to_list function.
    print(string_to_list(my_string))

main