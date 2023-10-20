"""Author: Darrien Guan
Date: September 14, 2023
Description: Modified code from question 6 in 1.7 to change mainline function. 
"""

def show_data(name = "Ms.Huynh", age = 40): 
    '''This function takes the parameters name and age and formats it into a message.'''

    # prints greeting and age message.
    print ("Hello", name, "you are", age, "years old! ")

def main():
    '''mainline logic: This function executes the mainline function'''

    show_data()
main()
