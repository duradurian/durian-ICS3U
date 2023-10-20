"""
Author: Darrien Guan
Date: October 11, 2023
Discription: Program asks user for their favourite fruit and checks whether it is in the groceries list.
"""

def fruit_presence(user_input_fruit):
    '''Checks each line and sees if user_input_fruit is present'''

    # open text file
    groceries_list = open("groceries.txt", "r")

    # checks each line in the text file for fruit.
    for line in groceries_list:
        if user_input_fruit in line:

            # Closes file and returns true if the fruit is present
            groceries_list.close()
            return True
    
    # Returns false if True wasn't returned.
    return False
        
def main():
    '''mainline logic'''

    # Ask user for favourite fruit.
    user_input_fruit = input("Enter your favourite fruit: ")

    # Calls fruit_presence function with user_input_fruit and displays message if present or not.
    if fruit_presence(user_input_fruit):
        print("Yes, your favourite fruit is in the groceries list.")
    else:
        print("No, your favourite fruit is not in the groceries list.")

main()