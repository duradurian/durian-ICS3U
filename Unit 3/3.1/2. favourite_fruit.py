"""
Author: Darrien Guan
Date: October 11, 2023
Discription: Program asks user for their favourite fruit and checks whether it is in the groceries list. If not, it adds it to the list.
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

def add_fruit(favourite_fruit):
    '''Adds inputted favourite fruit to the end of txt file.'''
    
    # open text file and writes fruit in addition to new line
    with open("groceries.txt", "a") as groceries:
        groceries.write(favourite_fruit + "\n")

    # Closes file
    groceries.close()

def main():
    '''mainline logic'''

    # Ask user for favourite fruit.
    user_input_fruit = input("Enter your favourite fruit: ")

    # Calls fruit_presence function with user_input_fruit and displays message if present or not.
    if fruit_presence(user_input_fruit):
        print("Yes, your favourite fruit is in the groceries list.")
    else:
        # Calls add_fruit function and adds user_input_fruit.
        add_fruit(user_input_fruit)
        print("Your favourite fruit was added to the groceries list.")

main()