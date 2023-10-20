"""
Author: Darrien Guan
Date: October 11, 2023
Discription: Program asks user for their least favourite fruit and checks whether it is in the groceries list. If it is, it removes it.
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

def remove_fruit(user_input_fruit):
    '''removes inputted fruit from list'''

    # reads groceries files 
    with open("groceries.txt", "r") as groceries_file:
        lines = groceries_file.readlines()
    
    # rewrites each line as long as fruit name is not present.
    with open("groceries.txt", "w") as groceries_file:
        for line in lines:
            if user_input_fruit not in line:
                groceries_file.write(line)
        
def main():
    '''mainline logic'''

    # Ask user for favourite fruit.
    user_input_fruit = input("Enter your least favourite fruit: ")

    # Calls fruit_presence function with user_input_fruit and displays message if present or not.
    if not fruit_presence(user_input_fruit):
        print("Your least favourite fruit is not in the list.")
    else:
        # Calls add_fruit function and adds user_input_fruit.
        remove_fruit(user_input_fruit)
        print("Your least favourite fruit was removed from the groceries list.")

main()